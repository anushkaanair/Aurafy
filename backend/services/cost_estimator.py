class CostEstimator:

    def estimate(self, models):

        total_cost = 0

        for task in models:

            selected_models = models[task]

            if len(selected_models) > 0:

                cheapest = min(selected_models, key=lambda m: m["cost"])

                total_cost += cheapest["cost"]

        return round(total_cost, 5)