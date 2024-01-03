# Implementation of FCFS
# https://www.geeksforgeeks.org/program-for-fcfs-cpu-scheduling-set-1/

# https://afteracademy.com/blog/what-is-burst-arrival-exit-response-waiting-turnaround-time-and-throughput/

# Given n processes with their burst times, the task is to find average waiting time 
# and average turn around time using FCFS scheduling algorithm. 

# In this, the process that comes first will be executed first and next process 
# starts only after the previous gets fully executed. Here we are considering 
# that arrival time for all processes is 0.

# 1-  Input the processes along with their burst time (bt).
# 2-  Find waiting time (wt) for all processes.
# 3-  As first process that comes need not to wait so 
#     waiting time for process 1 will be 0 i.e. wt[0] = 0.
# 4-  Find waiting time for all other processes i.e. for
#      process i -> 
#        wt[i] = bt[i-1] + wt[i-1] .
# 5-  Find turnaround time = waiting_time + burst_time 
#     for all processes.
# 6-  Find average waiting time = 
#                  total_waiting_time / no_of_processes.
# 7-  Similarly, find average turnaround time = 
#                  total_turn_around_time / no_of_processes.

# Turnaround time is a total of (Waiting time) + (CPU burst time) + (I/O time)
# Assume all processes are activated at time 0
# Assume that no process waits on I/O devices
# Waiting time time is accumlated while a process waits in the ready queue
# Response time is the first measure of waiting time from arrival at time 0 until the first time on the CPU.

class Scheduler():
    def __init__(self):
        print("Starting CPU Scheduler Sim...")

    # prints out process for FCFS
    def printProcess(self, cpu_Time, current_Burst, process, ready_Queue, process_Index, processes, process_Key, ioTime, finishProcess, conditional):

        print(f"Current CPU Time: {cpu_Time}")
        print(f"Running Process: {process} with a burst of {current_Burst}")
        print(f"Ready Queue: {ready_Queue}")
        print("CPU Burst time for each process in Ready Queue:")
        
        # itrerate through and print out process that are in line
        for y in range(len(ready_Queue)):
            # z = process
            z = ready_Queue[y]
            # will keep track of how far along in a specific subarray
            index = process_Index[z]
            # print out the x process and x index value of that process subarray
            print(z, ":", processes[z][index], end=" ")
        if conditional == 0:
            print("No process currently in Ready Queue...")
        else:
            print(" ")
            conditional = 0
        print("Processses in IO and tiem remaining for each:")
        # Iterate through the process to see if there is any active I/O waiting time
        for y in range(len(process_Key)):
            z = process_Key[y]
            if ioTime[z] > 0:
                # print out x process and x index value for I/o waiting time
                print(z, ":", ioTime[z], end=" ")
                conditional = 1
        if conditional == 0:
            print("No process currently in IO")
        else:
            print(" ")
            conditional = 0
        print(f"Finished processes: {finishProcess}")
        print("\n")

    # prints final result
    def finalResult(self, cpu_Time, cpu_TimeUse, time_Response, time_TurnAround, time_Wait, gantChart):
        print("\n")
        print("Final Results")
        print("*************************************")
        print("Total Time: ", (cpu_Time - 1))
        print("CPU Utilization: ", "{:.2f}%".format(((cpu_TimeUse - 1) / (cpu_Time - 1)) * 100))
        print("Time Response: ", time_Response)
        time_ResponseAverage = time_Response.values()
        print("Average Time Response: ", float(sum(time_ResponseAverage)/len(time_ResponseAverage)))
        print("Time Wait: ", time_Wait)
        time_waitAverage = time_Wait.values()
        print("Average Time wait: ", float(sum(time_waitAverage)/len(time_waitAverage)))
        print("Time Turnaround: ", time_TurnAround)
        time_TurnAroundAverage = time_TurnAround.values()
        print("Average Time TurnAround: ", float(sum(time_TurnAroundAverage)/len(time_TurnAroundAverage)))
        print("Printing Gant Chart...")
        print(self.make_GantChart(gantChart))
        print("Finished...")
        print("*************************************")

    # Calculate Tr, Tw, and IO_timer for FCFS
    def calculate(self, ioTime, time_Wait, process_Status, ready_Queue, last_Element, time_Response, cpu_Time):
        # Decrementing I/O waiting time
        for y in range(len(ioTime)):
            z = process_key[y]
            if ioTime[z] != 0:
                ioTime[z] = ioTime[z] - 1

        # increment time wait for process in ready queue
        for y in range(len(time_Wait)):
            z = process_key[y]
            if process_Status[z] == "start" or process_Status[z] == "ready":
                time_Wait[z] = time_Wait[z] + 1

        # sets to move any from completed IO state to ready state
        for y in range(len(ioTime)):
            z = process_key[y]
            if ioTime[z] == 0 and process_Status[z] == "IO":
                ready_Queue.append(z)
                process_Status[z] = "ready"
                print("\n")
                print("Current CPU Time: ", cpu_Time - 1)
                print(z, " has finished its IO and entered the ready Queue")
                print("\n")

        # calculate time respond
        if process_Status[last_Element] == "start":
            for y in range(len(process_Status)):
                z = process_key[y]
                if process_Status[z] == "start":
                    time_Response[z] = time_Response[z] + 1

    # sort and print gantchart
    def make_GantChart(self, gantchart):
        list1 = []
        for keys, values in gantchart.items():
            cur_vals = sorted(values)
            for number in cur_vals:
                list1.append((keys, number))
        list1 = sorted(list1, key=lambda x: x[1])
        print(list1)

    def first_Come(self):

        # define variables
        conditional = 1
        cpu_time_use = 0
        cpu_time = 0
        IoTime = {"P1":0, "P2":0, "P3":0, "P4":0, "P5":0, "P6":0, "P7":0, "P8":0}
        # Position in process
        process_index = {"P1":0, "P2":0, "P3":0, "P4":0, "P5":0, "P6":0, "P7":0, "P8":0}
        process_status = {"P1":"IO", "P2":"start", "P3":"start", "P4":"start", "P5":"start", "P6":"start", "P7":"start", "P8":"start"}
        ready_Queue = []
        time_response = {"P1": 0, "P2": 0, "P3": 0, "P4": 0, "P5": 0, "P6": 0, "P7": 0, "P8": 0}
        time_turn_around = {"P1": 0, "P2": 0, "P3": 0, "P4": 0, "P5": 0, "P6": 0, "P7": 0, "P8": 0}
        time_wait = {"P1":0, "P2":0, "P3":0, "P4":0, "P5":0, "P6":0, "P7":0, "P8":0}
        finishProcess = []
        gantchart = {"P1":[], "P2":[], "P3":[], "P4":[], "P5":[], "P6":[], "P7":[], "P8":[],"idle":[]}

        # Pre execution set up
        print("Current CPU time: ", cpu_time)
        ready_Queue = list(process_key)
        last_element = ready_Queue[-1]
        process_list = list(process_key)
        cpu_time += 1
        cpu_time_use += 1

        # sets up first process
        process =  ready_Queue[0]
        current_process = processes[process]
        current_process_index = process_index[process]
        current_burst = current_process[current_process_index]

        if current_process_index < (len(current_process) - 1):
            current_io = current_process[current_process_index + 1]
        else:
            current_io = 0
        process_status[process] = "bursting"
        del ready_Queue[0]

        gantchart[process].append(cpu_time - 1)

        # displays required info
        self.printProcess(cpu_time -1, current_burst, process, ready_Queue, process_index, processes, process_key, IoTime, finishProcess, conditional)

        # if there is still elements in the array keep the loop going
        while process_list:
            current_burst = current_burst - 1
            self.calculate(IoTime, time_wait, process_status, ready_Queue, last_element, time_response, cpu_time)

            cpu_time += 1
            cpu_time_use += 1

            # when burst finishes, processes move to IO and next process pulled from ready queue
            if current_burst == 0:
                print("\n")
                print("Context Switch")

                # if process finished
                if current_io == 0:
                    finishProcess.append(process)
                    print("Current CPU Time: ", cpu_time - 1)
                    print(process, "Last burst is finish and process is complete")
                    print("Currently removing", process)
                    print("\n\n\n")
                    process_list.remove(process)
                    time_turn_around[process] = cpu_time - 1
                    process_status[process] = "finished"
                else:
                    print("Current CPU Time: ", cpu_time - 1)
                    print(process, "CPU burst finish moving to IO for ", current_io, " time units")
                    print("\n\n\n")
                    IoTime[process] = current_io
                    process_status[process] = "IO"
                    process_index[process] += 2

                if not process_list:
                    break

                idle_time = cpu_time
                
                # idle handling
                while ready_Queue == []:
                    if current_burst == 0 and cpu_time == idle_time:
                        gantchart["idle"].append(idle_time - 1)
                    for y in range(len(process_key)):
                        z = process_key[y]
                        IoTime[z] = IoTime[z] - 1
                        if IoTime[z] == 0:
                            ready_Queue.append(z)
                            process_status[z] = "ready"
                            print("\n")
                            print("Context switch...")
                    cpu_time += 1
                    if not ready_Queue:
                        pass

                # sets up the next process
                process = ready_Queue[0]
                current_process = processes[process]
                current_process_index = process_index[process]
                current_burst = current_process[current_process_index]
                if current_process_index < (len(current_process) - 1):
                    current_io = current_process[current_process_index + 1]
                else:
                    current_io = 0
                process_status[process] = "bursting"
                del ready_Queue[0]

                gantchart[process].append(cpu_time - 1)

                # displays req info
                self.printProcess(cpu_time - 1, current_burst, process, ready_Queue, process_index, processes, process_key, IoTime, finishProcess, conditional)

        self.finalResult(cpu_time, cpu_time_use, time_response, time_turn_around, time_wait, gantchart)
                


processes = {"P1": (5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 4),
            "P2": (4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8),
            "P3": (8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6),
            "P4": (3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3),
            "P5": (16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4),
            "P6": (11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8),
            "P7": (14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10),
            "P8": (4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6)}
process_key = ("P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8")

cpu = Scheduler()
print("\nFirst come First Serve:")
cpu.first_Come()