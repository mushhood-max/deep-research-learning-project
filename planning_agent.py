class PlanningAgent:
    def __init__(self):
        self.name = "PlanningAgent"

    def plan(self, query):
        # This will be a simple implementation for now
        # It will split the query by spaces and return a list of tasks
        tasks = query.split()
        return tasks


