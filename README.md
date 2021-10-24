# BetterBuzzes
![alt text](https://github.com/jperez306/BetterBuzzes/blob/main/images/logo.png)

# How it works
BetterBuzzes is a three part feeback loop:
1) Collect the information of student bus riding habits
2) Generate an accurate model and run simulations to oprimize user wait times
3) Implement these changes to the bus schedule

The information is collected by users joining imaginary lines for a bus though the app. When users get on the bus, the system will recieve the total wait time expereinced by the user, along with arival time to help it model the student body schedule patterns. 
From this data simulations are run to help 

# The algorithm in action

In this example 60 people, 30 who use stop A in the morning and 30 who use stop B, head to stop C for classes, then return are a more dispered rate back to their home stop.

Unoptimized bus stop volume:

![alt text](https://github.com/jperez306/BetterBuzzes/blob/main/images/31243241.png)

Optimized bus stop volume:

![alt text](https://github.com/jperez306/BetterBuzzes/blob/main/images/23143214.png)  

# Future goals
Our goal is to utilize Google Cloud to better collect the data and be able to run simulations in parallel. This would allow more complex aspects of the bus schedule, such as breaks for drivers, unexpected traffic, and multiple buses at select times to be accounted for in the simulations.

# Links
https://devpost.com/software/better-buzzes
https://github.com/hpark416/BetterBuzzes-1
