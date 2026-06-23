from database_manager import DatabaseManager

class ExperimentManager:
    def __init__(self):
        self.db = DatabaseManager()

    def save(
        self,
        algorithm,
        agents_count,
        obstacles_count,
        avg_speed,
        avg_distance,
        simulation_time
    ):
        self.db.save_experiment(
            algorithm,
            agents_count,
            obstacles_count,
            avg_speed,
            avg_distance,
            simulation_time
        )