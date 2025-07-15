import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import database

def test_add_task():
    database.init_db()
    database.add_task("Tugas Baru")
    tasks = database.get_all_tasks()
    assert any(task[1] == "Tugas Baru" for task in tasks)
