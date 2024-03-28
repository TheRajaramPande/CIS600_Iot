# CIS600_Iot

IoT Data Visualization
This repository contains Python scripts for visualizing IoT (Internet of Things) data from multiple channels. The scripts are designed to load data from CSV files, preprocess timestamps, and generate visualizations using the pandas and matplotlib libraries.

Files:

feed_plotter3.py:

This script visualizes data from two separate channels. It loads data from CSV files, adjusts timestamps, and plots temperature, humidity, and CO2 levels over time for each channel.

Rajaram_Environment_Station_MainCode.py:

This script simulates the behavior of two IoT devices by generating random sensor data for temperature, humidity, and CO2 levels. It publishes the data to an MQTT broker using the Paho MQTT client library.
