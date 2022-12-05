from enum import Enum

# Process States
class ProcessState(Enum):
    NEW = 1
    READY = 2
    RUNNING = 3
    WAITING = 4
    TERMINATED = 5
    SUSPENDED = 6


# Class for the process that is being simulated, can be used in both preemptive and non-preemptive scheduling
class Process:
    def __init__(self, name, arrival_time, clock_cycle):
        self.name = name
        self.arrival_time = arrival_time
        self.clock_cycle = clock_cycle
        self.remaining_time = clock_cycle
        self.waiting_time = 0
        self.turnaround_time = 0
        self.start_time = 0
        self.end_time = 0
        self.state = ProcessState.NEW

# App class that contains the main functions of the program
class App:
    def __init__(self):
        self.processes = []
        self.scheduler = None
    def get_int_input(self, message):
        while True:
            try:
                user_input = int(input(message))
            except ValueError:
                print("Invalid input. Please enter a number.")
            else:
                return user_input
    def get_str_input(self, message, not_empty=True):
        while True:
            try:
                user_input = str(input(message))
            except ValueError:
                print("Invalid input. Please enter a string.")
            else:
                if not_empty and user_input == "":
                    print("Invalid input. Please enter a valid string.")
                else:
                    return user_input
    def set_scheduler(self, scheduler_function):
        self.scheduler = scheduler_function
    def get_processes(self):
        self.processes = []
        num_processes = self.get_int_input("Enter the number of processes: ")
        for i in range(num_processes):
            name = self.get_str_input("Enter the name of process " + str(i + 1) + ": ")
            arrival_time = self.get_int_input("Enter the arrival time of process " + str(i + 1) + ": ")
            clock_cycle = self.get_int_input("Enter the clock cycle of process " + str(i + 1) + ": ")
            self.processes.append(Process(name, arrival_time, clock_cycle))
    def run(self):
        if self.scheduler is None:
            print("No scheduler has been set.")
            return
        self.scheduler(self.copy_processes())

    def copy_processes(self):
        return [Process(process.name, process.arrival_time, process.clock_cycle) for process in self.processes]

# Preeemptive scheduling algorithm - FIFO
def preemptive_fifo(processes):
    print("===================================")
    print("Preemptive FIFO Scheduling Algorithm")
    print("===================================")

    # sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)

    while True:
        has_running_process = False
        for p in processes:
            # check if process is new
            if p.state == ProcessState.NEW:
                # set process to ready
                p.state = ProcessState.READY
                # set start time
                p.start_time = p.arrival_time
                # set end time
                p.end_time = p.start_time + p.clock_cycle
            elif (p.state in [ProcessState.READY, ProcessState.WAITING]) and not has_running_process:
                # set state to running
                p.state = ProcessState.RUNNING
                has_running_process = True
            elif p.state == ProcessState.RUNNING:
                # set remaining time
                p.remaining_time = p.clock_cycle
                # set turnaround time
                p.turnaround_time = p.end_time - p.arrival_time
                # set waiting time
                p.waiting_time = p.turnaround_time - p.clock_cycle
                # set state to terminated
                p.state = ProcessState.TERMINATED
                has_running_process = False
            elif p.state == ProcessState.READY:
                # set state to waiting
                p.state = ProcessState.WAITING
            elif p.state == ProcessState.TERMINATED:
                continue
            print(f"Process {p.name}: {p.state.name}")

        # check if all processes are terminated
        if all(i.state == ProcessState.TERMINATED for i in processes):
            break
    # compute average turnaround time
    total_turnaround_time = 0
    for i in processes:
        total_turnaround_time += i.turnaround_time
    average_turnaround_time = total_turnaround_time / len(processes)
    print("Average Turnaround Time: " + str(average_turnaround_time))

def sjf_non_preemptive(processes):
    print("===================================")
    print("SJF Non-Preemptive Scheduling Algorithm")
    print("===================================")

    # sort processes by arrival time
    processes.sort(key=lambda x: x.clock_cycle)

    while True:
        has_running_process = False
        for p in processes:
            # check if process is new
            if p.state == ProcessState.NEW:
                # set process to ready
                p.state = ProcessState.READY
                # set start time
                p.start_time = p.arrival_time
                # set end time
                p.end_time = p.start_time + p.clock_cycle
            elif (p.state in [ProcessState.READY, ProcessState.WAITING]) and not has_running_process:
                # set state to running
                p.state = ProcessState.RUNNING
                has_running_process = True
            elif p.state == ProcessState.RUNNING:
                # set remaining time
                p.remaining_time = p.clock_cycle
                # set turnaround time
                p.turnaround_time = p.end_time - p.arrival_time
                # set waiting time
                p.waiting_time = p.turnaround_time - p.clock_cycle
                # set state to terminated
                p.state = ProcessState.TERMINATED
                has_running_process = False
            elif p.state == ProcessState.READY:
                # set state to waiting
                p.state = ProcessState.WAITING
            elif p.state == ProcessState.TERMINATED:
                continue
            print(f"Process {p.name}: {p.state.name}")

        # check if all processes are terminated
        if all(i.state == ProcessState.TERMINATED for i in processes):
            break

    # compute average turnaround time
    total_turnaround_time = 0
    for i in processes:
        total_turnaround_time += i.turnaround_time
    average_turnaround_time = total_turnaround_time / len(processes)
    print("Average Turnaround Time: " + str(average_turnaround_time))
app = App()

# Preemptive FIFO Simulation
app.get_processes()
app.set_scheduler(preemptive_fifo)
app.run()

# SJF Non-Preemptive Simulation
app.set_scheduler(sjf_non_preemptive)
app.run()
