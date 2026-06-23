import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect(
            "swarm.db"
        )

        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS experiments(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                algorithm TEXT,
                agents INTEGER,
                obstacles INTEGER,
                avg_speed REAL,
                avg_distance REAL,
                timestamp TEXT
            )
            """
        )

        self.connection.commit()

    def save_experiment(
        self,
        algorithm,
        agents,
        obstacles,
        avg_speed,
        avg_distance
    ):
        self.cursor.execute(
            """
            INSERT INTO experiments(
                algorithm,
                agents,
                obstacles,
                avg_speed,
                avg_distance,
                timestamp
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                algorithm,
                agents,
                obstacles,
                avg_speed,
                avg_distance,
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )
        )

        self.connection.commit()

    def close(self):
        self.connection.close()