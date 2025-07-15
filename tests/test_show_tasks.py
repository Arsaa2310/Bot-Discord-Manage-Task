import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import database

def test_show_tasks():
    database.init_db()
    database.add_task("Tugas Show 1")
    database.add_task("Tugas Show 2")
    tasks = database.get_all_tasks()
    descriptions = [task[1] for task in tasks]
    assert "Tugas Show 1" in descriptions
    assert "Tugas Show 2" in descriptions
