import os
import cv2
import gps
from ultralytics import YOLO
import mysql.connector

def update_coordinates_in_db(lat, lon):
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            host='localhost', 
            user='root',  
            password='######',
            database='######'  
        )

        cursor = connection.cursor()

        # SQL query to update the coordinates
        update_query = """UPDATE gps_loc
                          SET latitude = %s, longitude = %s"""
        data = (lat, lon)

        # Execute the query and commit the transaction
        cursor.execute(update_query, data)
        connection.commit()

        print("Coordinates updated successfully")

    except mysql.connector.Error as error:
        print("Failed to update coordinates: {}".format(error))

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()


# Function to get GPS location from local gps device 
def get_gps_location():
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    try:
        while True:
            report = session.next()
            if report['class'] == 'TPV':
                if hasattr(report, 'lat') and hasattr(report, 'lon'):
                    return report.lat, report.lon
    except KeyboardInterrupt:
        session.close()

VIDEOS_DIR = os.path.join('.', 'videos')

# Load the YOLO model
model = YOLO('weights/best.pt')  

threshold = 0.7
cap = cv2.VideoCapture(0) 
W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 30, (W, H))

while True:
    ret, frame = cap.read()

    if not ret:
        break
    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            lat, lon = get_gps_location()
            print("Pothole detected at Latitude:", lat, "Longitude:", lon)
            update_coordinates_in_db(lat, lon)

    out.write(frame)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
