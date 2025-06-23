# Designing a Traffic Signal Control System
---
## Requirements
- The traffic signal system should control the flow of traffic at an intersection with multiple roads.
- The system should support different types of signals, such as red, yellow, and green.
- The duration of each signal should be configurable and adjustable based on traffic conditions.
- The system should handle the transition between signals smoothly, ensuring safe and efficient traffic flow.
- The system should be able to detect and handle emergency situations, such as an ambulance or fire truck approaching the intersection.
- The system should be scalable and extensible to support additional features and functionality.

## Classes, Interfaces and Enumerations
- The Signal enum represents the different states of a traffic light: red, yellow, and green.
- The Road class represents a road in the traffic signal system, with properties such as ID, name, and an associated traffic light.
- The TrafficLight class represents a traffic light, with properties such as ID, current signal, and durations for each signal state. It provides methods to change the signal and notify observers (e.g., roads) about signal changes.
- The TrafficController class serves as the central controller for the traffic signal system. It follows the Singleton pattern to ensure a single instance of the controller. It manages the roads and their associated traffic lights, starts the traffic control process, and handles emergency situations.
- The TrafficSignalSystemDemo class is the main entry point of the application. - It demonstrates the usage of the traffic signal system by creating roads, traffic lights, assigning traffic lights to roads, and starting the traffic control process.

# Credits
-- https://github.com/ashishps1/awesome-low-level-design/tree/main/solutions/python/trafficsignalsystem