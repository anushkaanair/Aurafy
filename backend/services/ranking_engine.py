from backend.data.model_registry import MODELS


class RankingEngine:

    def rank_models(self, tasks):

        results = {}

        for task in tasks:

            models = [m for m in MODELS if m["task"] == task]

            models = sorted(models, key=lambda x: x["cost"])

            results[task] = models

        return results