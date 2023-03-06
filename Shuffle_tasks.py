import random


tasks = []
while True:
    task = input('Введите задачу: ')
    if not task:
        break
    tasks.append(task)
random.shuffle(tasks)
for show_tasks in tasks:
    print(show_tasks)


        