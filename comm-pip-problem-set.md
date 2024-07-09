## Question Set 1:

- List all rosnodes that exist after running the publisher
	- Only the talker rosnode

- List all rostopics that are being present after running the publisher
	- Only the publisher's topic, which is 'topic'
 
- What command do I run to see what is being published to a topic?
	- The command is create_subscription 

- What would I change in the publisher to make it publish messages more frequently?
	- You would decrease timer_period.

- In terminal I run the python script for the subcriber and see information being printed. Does this mean it is publishing to a topic?
	- This means that the publisher is publishing information, and not the subscriber.

- What is the main benefit of a composed node? How might this help in drone autonomy applications?
	- The main benefit of a composed node is to combine different processess into a single task, which makes drone autonomy a lot simpler and easier to track. 
