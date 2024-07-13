Pothole Detection System

Welcome to the Pothole Detection System project! This repository contains the code and instructions for implementing a pothole detection system using YOLO (You Only Look Once) object detection algorithms, specifically YOLOv8n.

Overview

The Pothole Detection System aims to identify and locate potholes on road surfaces using state-of-the-art object detection models. Efficient pothole detection is crucial for road maintenance and safety.

Installation 

1.clone this repository 
git clone https://github.com/yourusername/pothole-detection-system.git
cd pothole-detection-system

2.install the required dependencies 
pip install -r requirements.txt

Usage 

1.Detection:
You can use "main.py" for detecting potholes on roads using a camera pointing towards road which then updates to the database(here i used mysql databse{you can change your credentials in the "update_coordinates_in_db" function}).

2.Visualization:
You can use "plot_map.py" for plotting potholes on map using the coordinates stored in the database whcih was previously updated by the "main.py" file.(I have shwon a sample map  whcih is "gps_map.html" which is stored in results folder).
![Screenshot from 2024-07-04 20-37-59](https://github.com/rupeshPabba/pothole_detection/assets/96829415/a16fa436-1af6-4ad8-9729-97ad2344e8ec)

Overview of database

![image](https://github.com/rupeshPabba/pothole_detection/assets/96829415/74211c6a-b943-47d6-a2a8-b718d74dab90)

Results

The project detecte ppotholes using YOLOv8n in detecting potholes, with better precision and recall metrics. Detailed results and performance metrics are documented in the results folder.

![results](https://github.com/rupeshPabba/pothole_detection/assets/96829415/13170001-69a7-4de3-aca4-ffb21e443882)

![Screenshot from 2024-07-04 20-42-38](https://github.com/rupeshPabba/pothole_detection/assets/96829415/2c3f9e82-dfc3-4f17-8447-2dd6fdc766b4)

