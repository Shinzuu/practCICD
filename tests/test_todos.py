import pytest
from fastapi.testclient import TestClient
from src.main import app, todos as todos_list, Todo

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Todo API"}

def test_create_todo():
    # Clear todos before test
    todos_list.clear()
    
    # Test successful creation
    todo_data = {"id": 1, "title": "Test Todo", "description": "Test Description"}
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert len(todos_list) == 1
    
    # Test duplicate ID
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 400

def test_get_todos():
    # Clear and add test data
    todos_list.clear()
    test_todo = Todo(id=1, title="Test", description="Test")
    todos_list.append(test_todo)
    
    # Test get all todos
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == 1

def test_get_todo():
    # Clear and add test data
    todos_list.clear()
    test_todo = Todo(id=1, title="Test", description="Test")
    todos_list.append(test_todo)
    
    # Test get existing todo
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    
    # Test get non-existent todo
    response = client.get("/todos/999")
    assert response.status_code == 404

def test_update_todo():
    # Clear and add test data
    todos_list.clear()
    test_todo = Todo(id=1, title="Old Title", description="Old Description")
    todos_list.append(test_todo)
    
    # Test successful update
    updated_todo = {"id": 1, "title": "New Title", "description": "New Description"}
    response = client.put("/todos/1", json=updated_todo)
    assert response.status_code == 200
    assert response.json()["title"] == "New Title"
    
    # Test ID mismatch
    response = client.put("/todos/1", json={"id": 2, "title": "Test", "description": "Test"})
    assert response.status_code == 400
    
    # Test non-existent todo
    response = client.put("/todos/999", json={"id": 999, "title": "Test", "description": "Test"})
    assert response.status_code == 404

def test_delete_todo():
    # Clear and add test data
    todos_list.clear()
    test_todo = Todo(id=1, title="Test", description="Test")
    todos_list.append(test_todo)
    
    # Test successful deletion
    response = client.delete("/todos/1")
    assert response.status_code == 204
    assert len(todos_list) == 0
    
    # Test delete non-existent todo
    response = client.delete("/todos/999")
    assert response.status_code == 404
