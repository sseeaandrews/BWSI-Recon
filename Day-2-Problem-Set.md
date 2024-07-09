### Please answer the following questions and push your answers to your team's remote documents repository

For true/false question, if the statement is false, provide a description of why it is false.

- What are some of the difference between the a research and development drone vs other "commercial" or "toy" drones?
	- The research and development drone would likely need to have more sensors and computing power, while the priority of a commerical drone would be to make it cost efficient and cheap. 
- What are some current applications of autonomous drones? Can you think of any future applications as technology improves (e.g. faster, smaller, more efficient computers)?
	- Delivery
	- Search and rescue
	- Recon
	- Defense 
	- Photography
	- Surveillance
- Describe the difference between the Compute Board and Flight Controller. What purposes do each serve? What operating systems do each run?
	- The compute board does the more complex calculations, while the flight controller does lower level operations. The compute board runs Linux, while the flight controller runs NuttX. 
- Which communication architecture are we using to connect our computers to the drone: Peer2Peer or centralized? What about the remote control - drone communication?
	- To connect computers to the drone and connect the remote control to the drone, centralized commucation architecture is being used.
- True or False: For manual flight control, the remote control communicates with the drone over wifi.
	- False; the remote control communicates over radio.
- In order to know where the drone is in the world, it needs some form of positioning sensor/algorithms, otherwise it would be flying blind. What are the different types of positioning sensors available? Which do you think we are going to use during the class?
	- Barometer 
	- GPS
	- Lidar
	- Radar
- True or False: during our indoor flights, we can use the GPS sensor to estimate the drone's position in the world. 
	- True
- Are optical flow algorithms responsible for mapping the environment? If not, can you describe conceptually what optical flow does?
	- No; optical flow algorithms change in imagery in the environment by comparing frames of video.   
- Which potential sensors on a Drone enables 3D visual mapping? 
	- Lidar and radar
- How does the Compute Board communicate with the Flight Controller? 
	- The compute board and the flight controller communicate through MAVROS2
- What is PX4 and where is it running on the drone? 
	- PX4 is autopilot running on the flight controller. 
- Which of these best describes MAVLink: 1. an operating system used on the drone, 2. a sensor on the drone, 3. a communication protocol on the drone, 4. a programming language
	- 3. a communication protocol on the drone
- If I want to write a new, complex computer vision algorithm for the drone, should I add it to the Flight Controller firmware? if not, where should I add it and why?
	- The algorithm should be added to the compute board, which would be able to perform the complex calculations needed by the algorithm. 
