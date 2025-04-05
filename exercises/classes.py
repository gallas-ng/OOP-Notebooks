# Classes for the OrderBook Application

class Task:
    """Class which models a single task in a software company’s list of tasks"""

    _task_status = {
        0: "NOT FINISHED",
        1: "FINISHED",
    }

    # counter for unique IDs
    _id_counter = 1  

    # The magic method __new__ is used to assign a unique ID foreach instance of Task class
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__id = cls._id_counter 
        cls._id_counter += 1
        return instance

    def __init__(self, description, programmer,workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.__status = 0  # Default status is "NOT FINISHED"

    # This method has been created for test purpose
    @classmethod
    def reset_id_counter(cls):
        """Reset the ID counter to 1"""
        cls._id_counter = 1
        
    @property
    def id(self):
        """Get the ID of a task"""
        return self.__id

    @property
    def status(self):
        """Get the status of a task"""
        return type(self)._task_status[self.__status]

    def __str__(self):
        """Return a string representation of the task."""
        return f"{self.id} : {self.description} ({self.workload} hours), programmer {self.programmer} {self.status}"

    def mark_finished(self):
        """Mark the task as finished."""
        self.__status = 1

    def is_finished(self):
        """Check if the task is finished."""
        return self.__status == 1
    

    
class OrderBook:
    """Class that collects all the tasks ordered from a software company"""

    def __init__(self):
        self.__orders = []

    def add_order(self, description, programmer, workload):
        """Add a new task to the order book."""
        task = Task(description, programmer, workload)
        self.__orders.append(task)

    def all_orders(self):
        """Return a list of all tasks."""
        return self.__orders
    
    def programmers(self):
        """Return a list of all programmers."""
        programmers = [task.programmer for task in self.__orders]
        return set(programmers) 
    
    def programmers_tasks(self):
        """Return a dictionary of programmers and the list of task identifiers that are assigned to them"""
        programmers_dict = {}
        for task in self.__orders:
            if task.programmer not in programmers_dict:
                programmers_dict[task.programmer] = []
            programmers_dict[task.programmer].append(task.id)
        return programmers_dict
    
    def mark_finished(self, task_id):
        """Mark a task as finished"""
        if task_id not in [task.id for task in self.__orders]:
            raise ValueError("Task with ID " + str(task_id) + " not found")
        
        for task in self.__orders:
            if task.id == task_id:
                task.mark_finished()
    
    def finished_orders(self):
        """Return all finished tasks in the orderbook"""
        return [task for task in self.__orders if task.is_finished() == True]

    def unfinished_orders(self):
        """Return all unfinished tasks in the orderbook"""
        return [task for task in self.__orders if task.is_finished() == False]
        
    def status_of_programmer(self, programmer):
        """Return  the number of finished and unfinished tasks for a programmer, along with the estimated hours"""
        finished = 0
        unfinished = 0
        finished_workload = 0
        unfinished_workload = 0

        if programmer not in self.programmers():
            raise ValueError("Programmer " + programmer + " not found")
        
        for task in self.__orders:
            if task.programmer == programmer:
                if task.is_finished():
                    finished += 1
                    finished_workload += task.workload
                else:
                    unfinished += 1
                    unfinished_workload += task.workload

        return (finished, unfinished, finished_workload, unfinished_workload)
    