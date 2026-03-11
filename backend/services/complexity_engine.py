class ComplexityEngine:

    def calculate(self, tasks, pipeline):

        score = 0

        # task count
        score += len(tasks)

        # architecture depth
        score += len(pipeline) * 0.3

        task_weights = {
            "text_generation": 1,
            "image_generation": 3,
            "speech_to_text": 2,
            "text_to_speech": 2,
            "video_generation": 4
        }

        for task in tasks:
            score += task_weights.get(task, 1)

        if len(tasks) > 2:
            score += 2

        return round(score, 2)