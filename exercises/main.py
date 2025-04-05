from classes import OrderBook, Task

# Test code for parts 1 to 5

# ----- Part 1 ---------------------------
print(" --- Part 1 ---")
print()
t1 = Task("program hello world", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())
t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3)
print()
# ---------------------------------------


Task.reset_id_counter()


# ----- Part 2 ---------------------------
print(" --- Part 2 ---")
print()
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

for order in orders.all_orders():
    print(order)

print()

for programmer in orders.programmers():
    print(programmer)
print()
# ---------------------------------------


Task.reset_id_counter()


# ----- Part 3 (Additional test code) -----
print(" --- Part 3 ---")
orders = OrderBook()
print()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

for programmer, tasks in orders.programmers_tasks().items():
    print(f"{programmer}: {tasks}")
print()
# ---------------------------------------


Task.reset_id_counter()


# ----- Part 4 ---------------------------
print(" --- Part 4 ---")
print()
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

orders.mark_finished(1)
orders.mark_finished(2)

for order in orders.all_orders():
    print(order)
print()
# ---------------------------------------


Task.reset_id_counter()


# ----- Part 5 ---------------------------
print(" --- Part 5 ---")
print()
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status)
print()
# ---------------------------------------

Task.reset_id_counter()


# ----- Final application program for Parts 6 and 7 -----

def app():
    
    orders = OrderBook()

    def menu():
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def render_error():
        print("erroneous input")

    def add_order():
        description = input("description: ")
        programmer_workload = input("programmer and workload estimate: ")
        programmer_workload = programmer_workload.split(" ")
        programmer = programmer_workload[0]
        try:
            workload = int(programmer_workload[1])
        except:
            render_error()
            return
        orders.add_order(description, programmer, workload)
        print("added !")

    def list_finished_tasks():
        if len(orders.finished_orders()) > 0:
            for task in orders.finished_orders():
                print(task)
        else:
            print("no finished tasks")

    def list_unfinished_tasks():
        if len(orders.unfinished_orders()) > 0:
            for task in orders.unfinished_orders():
                print(task)
        else:
            print("no unfinished tasks")

    def mark_finished():
        try:
            id = int(input("id: "))
        except:
            render_error()
            return

        if id not in [task.id for task in orders.all_orders()]:
            render_error()
            return

        orders.mark_finished(id)
        print("marked as finished")

    def programmers():
        for programmer in orders.programmers():
            print(programmer)

    def programmer_status():
        programmer = input("programmer: ")
        if programmer not in orders.programmers():
            render_error()
            return
        finished, unfinished, finished_workload, unfinished_workload = orders.status_of_programmer(programmer)
        print(f"tasks: finished {finished} not finished {unfinished}, hours: done {finished_workload} scheduled {unfinished_workload}")

    
    menu()
    while True:
        print()
        try:
            command = int(input("command: "))
        except:
            command = -1
        if command == 0:
            break
        elif command == 1:
            add_order()
        elif command == 2:
             list_finished_tasks()
        elif command == 3:
            list_unfinished_tasks()
        elif command == 4:
             mark_finished()
        elif command == 5:
            programmers()
        elif command == 6:
            programmer_status()
        else:
            menu()

if __name__ == "__main__":

    app()
        