import sqlite3
import csv

connection = sqlite3.connect(
    "simulation.db"
)

cursor = connection.cursor()
cursor.execute(
    """
    SELECT
        algorithm,
        avg_speed,
        avg_distance,
        agents_count,
        obstacles_count,
        created_at
    FROM experiments
    """
)
rows = cursor.fetchall()

with open(
    "results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)
    writer.writerow(
        [
            "Algorithm",
            "AvgSpeed",
            "AvgDistance",
            "Agents",
            "Obstacles",
            "CreatedAt"
        ]
    )

    writer.writerows(rows)

connection.close()