import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(
            "simulation.db"
        )

        self.cursor = (
            self.connection.cursor()
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS experiments
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                algorithm TEXT,
                avg_speed REAL,
                avg_distance REAL,
                agents_count INTEGER,
                obstacles_count INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        self.connection.commit()

    def save_experiment(
        self,
        algorithm,
        avg_speed,
        avg_distance,
        agents_count,
        obstacles_count
    ):
        self.cursor.execute(
            """
            INSERT INTO experiments
            (
                algorithm,
                avg_speed,
                avg_distance,
                agents_count,
                obstacles_count
            )
            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?
            )
            """,
            (
                algorithm,
                avg_speed,
                avg_distance,
                agents_count,
                obstacles_count
            )
        )

        self.connection.commit()

    def close(self):
        self.connection.close()