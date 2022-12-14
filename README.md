# process-scheduling-system
Simulation of Process Scheduling in Operating Systems


## How the program works?
The program is composed of 3 classes (which handles the state, the process, the schedular, the inputs and the other requirements to handle the simulation) and 2 functions (which handles the simulation algorithm and the output of the simulation). 

ProcessState(Enum) which will be used for emulating different state of a CPU Process which in our case is NEW (state for new process that is not ready yet), READY (state for process that is ready to be executed), RUNNING (state for process that is currently running), WAITING (state for process that is waiting for some event to happen), TERMINATED (state for process that is terminated). Process class will be used for creating a process object and ProcessScheduler class for scheduling the processes. App class which will be used for handling the inputs and creating the processes array and apply a scheduling algorithm on it. The 2 functions are the scheduler functions that will be used for the simulation algorithm and the output of the simulation. 

There are 2 scheduler functions that will be used for the simulation algorithm and the output of the simulation, the first one is the FCFS (First Come First Serve) also known as FIFO (First In First Out) which is will be used for scheduling the processes in the order that they are created, the second one is the SJF (Shortest Job First) which will be used for scheduling the processes in the order of their burst time, the process with the shortest burst time will be executed first. 

The FCFS scheduler function gets the processes array that contains CPU process as it's element, then it will sort the processes array by the arrival time of the processes, then it will loop through the processes array and perform specific action based on the state of the process, if the process state is NEW, then it will change the state of the process to READY, if the process state is READY, then it will change the state of the process to RUNNING, if the process state is RUNNING, then it will change the state of the process to TERMINATED, if the process state is WAITING, then it will change the state of the process to READY, if the process state is TERMINATED, then it will change the state of the process to TERMINATED, then it will return the processes array. The loop will continue until all the processes in the processes array are terminated. 

The SJF scheduler function is the same as the FCFS scheduler function, the only difference is that the processes array will be sorted by the burst time of the processes instead of the arrival time of the processes, then the loop will continue until all the processes in the processes array are terminated. 

 
 

To run the program, you need to create an instance of the App class, then to get the processes to simulate, you need to call the get_processes() method which will get and handle the inputs from the user, the information that the user will enter is the number of processes, the information of each process. After that, you need to call the set_scheduler(scheduler_function) method which will set the scheduler function that will be used for the simulation algorithm, the scheduler function is a function that will be used for the simulation algorithm and the output of the simulation. After that, you need to call the run() method which will run the simulation algorithm and the output of the simulation. 

 
 