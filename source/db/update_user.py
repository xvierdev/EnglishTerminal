import sqlite3


def update_user(db, user):
    """
    Updates the user's record in the database.

    Args:
        db (sqlite3.Connection): The SQLite database connection.
        user (User): The user object containing the new record.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    try:
        with db:
            db.execute(
                "UPDATE Users SET record = ? WHERE nick = ?",
                (user.record, user.nick),
            )
        return True
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return False