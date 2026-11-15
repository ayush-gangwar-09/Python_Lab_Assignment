# Question 10: Run multiple tasks using asyncio.

import asyncio


async def do_task(task_name, seconds):
    print(task_name, "started.")
    await asyncio.sleep(seconds)
    print(task_name, "finished.")


async def main():
    # gather runs these asynchronous tasks together.
    await asyncio.gather(
        do_task("Task 1", 2),
        do_task("Task 2", 3),
        do_task("Task 3", 1)
    )

    print("All asynchronous tasks are complete.")


asyncio.run(main())
