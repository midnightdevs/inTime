from typing import Union

from fastapi import FastAPI
from typing import Dict, Union
from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items")
def read_items():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()

    # Close the connection
    cursor.close()
    conn.close()

    return {"items": items}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM items WHERE id = ?', (item_id,))
    item = cursor.fetchone()

    # Close the connection
    cursor.close()
    conn.close()

    return {"item": item}


@app.post("/items")
def create_item(item: Dict[str, Union[str, None]]):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    name = item.get('name')
    description = item.get('description')
    cursor.execute('INSERT INTO items (name, description) VALUES (?, ?)', (name, description))
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

    return {"message": "Item created successfully"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Dict[str, Union[str, None]]):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    name = item.get('name')
    description = item.get('description')
    cursor.execute('UPDATE items SET name = ?, description = ? WHERE id = ?', (name, description, item_id))
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

    return {"message": "Item updated successfully"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

    return {"message": "Item deleted successfully"}
