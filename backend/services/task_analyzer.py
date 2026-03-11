from backend.data.tasks import TASK_LIBRARY


class TaskAnalyzer:

    def analyze(self, query):

        query = query.lower()
        detected_tasks = []

        for task, data in TASK_LIBRARY.items():

            for keyword in data["keywords"]:

                if keyword in query:
                    detected_tasks.append(task)
                    break

        return detected_tasks