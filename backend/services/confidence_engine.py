class ConfidenceEngine:

    def calculate(self, tasks, models, complexity_score, simulation):

        score = 100

        # fewer tasks → clearer idea
        if len(tasks) == 0:
            score -= 40
        elif len(tasks) > 3:
            score -= 10

        # model availability
        for task in tasks:
            if task not in models or len(models[task]) == 0:
                score -= 15

        # complexity penalty
        if complexity_score > 8:
            score -= 10

        # scalability risk
        risk = simulation["scalability_risk"]

        if risk == "Medium":
            score -= 10

        if risk == "High":
            score -= 20

        return max(score, 0)