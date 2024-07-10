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

## Question Set 2:

- What needed to be added the launch file?
	- A namespace needed to be added to the launch files so that multiple different turtlesims could be run at the same time.

- With rqt_graph open, use the button in upper right corner to save an image of the graph and include it in this report. Which components in the graph indicates rosnodes and which indicate rostopics?

- Why do we need to run the command when and why do we need to source a bash file?

- Were there any steps that didn’t work or were particularly confusing? How did you work around them?

- Create a launch file for the subscriber and listener you made above.

