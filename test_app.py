import app

def setup_function():
    # Reset tasks list before each test
    app.tasks.clear()

def test_add_task():
    app.add_task("Buy milk")
    assert app.view_tasks() == ["Buy milk"]

def test_view_tasks_empty():
    assert app.view_tasks() == []

def test_remove_task_success():
    app.add_task("Clean room")
    removed = app.remove_task("Clean room")
    assert removed is True
    assert app.view_tasks() == []

def test_remove_task_not_found():
    app.add_task("Study")
    removed = app.remove_task("Exercise")
    assert removed is False
    assert app.view_tasks() == ["Study"]

def test_add_multiple_tasks():
    app.add_task("Task1")
    app.add_task("Task2")
    assert app.view_tasks() == ["Task1", "Task2"]
