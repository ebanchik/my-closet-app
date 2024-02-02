import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS categories;
        """
    )
    conn.execute(
        """
        DROP TABLE IF EXISTS items;
        """
    )
    conn.execute(
        """
        DROP TABLE IF EXISTS users;
        """
    )
    conn.execute(
        """
        CREATE TABLE categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT UNIQUE NOT NULL
        );
        """
    )
    conn.execute(
        """
        CREATE TABLE items (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          brand TEXT,
          size INT,
          color TEXT,
          fit TEXT,
          category_id INT,
          FOREIGN KEY (category_id) REFERENCES categories (id)
        );
        """
    )
    conn.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        );
        """
    )

    conn.commit()
    print("Tables created successfully")

    categories_seed_data = [
    ("Shirts",),
    ("Pants",),
    ("Sweaters",),
    ("Sweatpants",),
    ("Shoes",),
    ("Accessories",),
    ("Jackets",),
    ("Suits + Blazers",),
    ("Sneakers",)
    ]

    conn.executemany(
        """
        INSERT INTO categories (category_name)
        VALUES (?)
        """,
        categories_seed_data
    )
    conn.commit()
    print("Cateogry seed data created successfully")



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


    users_seed_data = [
    ("admin", "hashed_password_of_admin"),
    # Add more users as needed
    ]
    conn.executemany(
        """
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
        """,
        users_seed_data
    )
    conn.commit()
    print("User seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()

    class DB:
        def users():
            conn = connect_to_db()
            rows = conn.execute(
                """
                SELECT * FROM users
                """
            ).fetchall()
            return [dict(row) for row in rows]

        def items_all():
            conn = connect_to_db()
            rows = conn.execute(
                """
                SELECT * FROM items
                """
            ).fetchall()
            return [dict(row) for row in rows]

        def categories_all():
            conn = connect_to_db()
            rows = conn.execute(
                """
                SELECT * FROM categories
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


        def items_with_categories():
            conn = connect_to_db()
            query = """
            SELECT items.*, categories.category_name
            FROM items
            JOIN categories ON items.category_id = categories.id;
            """
            rows = conn.execute(query).fetchall()

            result_data = []
            for row in rows:
                result_data.append({
                    "id": row["id"],
                    "name": row["name"],
                    "brand": row["brand"],
                    "size": row["size"],
                    "color": row["color"],
                    "fit": row["fit"],
                    "category_id": row["category_id"],
                    "category_name": row["category_name"]
                })


                conn.close()
                return result_data