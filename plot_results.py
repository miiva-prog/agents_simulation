import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

connection = sqlite3.connect(
    "simulation.db"
)
query = """
SELECT
    algorithm,
    avg_speed,
    avg_distance
FROM experiments
"""
data = pd.read_sql_query(
    query,
    connection
)
connection.close()

grouped = data.groupby(
    "algorithm"
).mean(
    numeric_only=True
)

plt.figure(
    figsize=(8, 5)
)

plt.bar(
    grouped.index,
    grouped["avg_speed"]
)

plt.title(
    "Average Speed"
)

plt.ylabel(
    "Speed"
)

plt.tight_layout()

plt.savefig(
    "avg_speed.png"
)

plt.close()

plt.figure(
    figsize=(8, 5)
)

plt.bar(
    grouped.index,
    grouped["avg_distance"]
)

plt.title(
    "Average Distance"
)

plt.ylabel(
    "Distance"
)

plt.tight_layout()

plt.savefig(
    "avg_distance.png"
)

plt.close()