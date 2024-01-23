import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS items;
        """
    )
    conn.execute(
        """
        CREATE TABLE items (
          id INTEGER PRIMARY KEY NOT NULL,
          name TEXT,
          brand TEXT,
          size INT,
          color TEXT,
          fit TEXT,
          category_id INT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    items_seed_data = [
        ("Loose-fit Jeans", "HOPE", 34, "Mid Grey Stone", "very baggy", 2),
    ]
    conn.executemany(
        """
        INSERT INTO items (name, brand, size, color, fit, category_id)
        VALUES (?,?,?,?,?,?)
        """,
        items_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()


def items_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM items
        """
    ).fetchall()
    return [dict(row) for row in rows]

def items_create(name, brand, size, color, fit, category_id):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO items (name, brand, size, color, fit, category_id)
        VALUES (?, ?, ?, ?, ?, ?)
        RETURNING *
        """,
        (name, brand, size, color, fit, category_id),
    ).fetchone()
    conn.commit()
    return dict(row)

def items_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM items
        WHERE id = ?
        """,
        id,
    ).fetchone()
    return dict(row)

def items_update_by_id(id, name, brand, size, color, fit, category_id):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE items SET name = ?, brand = ?, size = ?, color = ?, fit = ?, category_id = ?
        WHERE id = ?
        RETURNING *
        """,
        (name, brand, size, color, fit, category_id, id),
    ).fetchone()
    conn.commit()
    return dict(row)