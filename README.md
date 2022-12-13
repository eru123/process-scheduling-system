# process-scheduling-system
Simulation of Process Scheduling in Operating Systems


## How the program works?
The program composed of 3 classes (which handles the state, the process, the schedular, the inputs and the other requirements to handle the simulation) and 2 functions (which handles the simulation algorithm and the output of the simulation).

ProcessState(Enum) which will be used for emulating different state of a CPU Process which in our case is NEW (state for new process that is not ready yet), READY (state for process that is ready to be executed), RUNNING (state for process that is currently running), WAITING (state for process that is waiting for some event to happen), TERMINATED (state for process that is terminated). Process class which will be used for creating a process object and ProcessScheduler class which will be used for scheduling the processes.