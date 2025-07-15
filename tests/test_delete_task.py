import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import database

def test_delete_task():
    database.init_db()
    database.add_task("Tugas yang Akan Dihapus")
    tasks = database.get_all_tasks()
    task_id = next(task[0] for task in tasks if task[1] == "Tugas yang Akan Dihapus")
    database.delete_task(task_id)
    tasks_after = database.get_all_tasks()
    assert all(task[0] != task_id for task in tasks_after)
