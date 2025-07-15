import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import database

def test_complete_task():
    database.init_db()
    database.add_task("Tugas Selesai")
    tasks = database.get_all_tasks()
    task_id = next(task[0] for task in tasks if task[1] == "Tugas Selesai")
    database.complete_task(task_id)
    updated_tasks = database.get_all_tasks()
    completed = next(task for task in updated_tasks if task[0] == task_id)
    assert completed[2] == 1  # 1 berarti True di SQLite
