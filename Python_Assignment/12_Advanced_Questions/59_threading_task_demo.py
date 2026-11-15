# Question 9: Run multiple tasks using Python threading.

import threading
import time


def do_task(task_name, seconds):
    print(f"{task_name} started.")
    time.sleep(seconds)  
    print(f"{task_name} finished.")


first_thread = threading.Thread(target=do_task, args=("Task 1", 2))
second_thread = threading.Thread(target=do_task, args=("Task 2", 3))

# Start both threads.
first_thread.start()
second_thread.start()

# Wait until both threads finish.
first_thread.join()
second_thread.join()

print("All tasks are complete.")
