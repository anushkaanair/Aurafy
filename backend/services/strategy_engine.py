from backend.services.task_analyzer import TaskAnalyzer
from backend.services.ranking_engine import RankingEngine
from backend.services.architecture_pipeline import ArchitecturePipeline
from backend.services.complexity_engine import ComplexityEngine
from backend.services.cost_estimator import CostEstimator
from backend.services.architecture_simulator import ArchitectureSimulator
from backend.services.confidence_engine import ConfidenceEngine

class StrategyEngine:

    def __init__(self):

        self.task_analyzer = TaskAnalyzer()
        self.ranking_engine = RankingEngine()
        self.architecture = ArchitecturePipeline()
        self.complexity = ComplexityEngine()
        self.cost_estimator = CostEstimator()
        self.simulator = ArchitectureSimulator()
        self.confidence_engine = ConfidenceEngine()


    def generate_strategy(self, query):

        tasks = self.task_analyzer.analyze(query)

        models = self.ranking_engine.rank_models(tasks)

        pipeline = self.architecture.generate(tasks)

        complexity_score = self.complexity.calculate(tasks, pipeline)

        estimated_cost = self.cost_estimator.estimate(models)

        simulation = self.simulator.simulate(pipeline)

        confidence  = self.confidence_engine.calculate(tasks, models, complexity_score, simulation)
        
        
        return {
            "tasks": tasks,
            "models": models,
            "pipeline": pipeline,
            "complexity_score": complexity_score,
            "estimated_cost": estimated_cost,
            "simulation": simulation,
             "confidence": confidence

        }