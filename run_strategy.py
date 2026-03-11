from backend.services.strategy_engine import StrategyEngine

engine = StrategyEngine()

query = input("Enter your project idea: ")

result = engine.generate_strategy(query)

print("\nDetected Tasks:")
print(result["tasks"])

print("\nRecommended Models:")
print(result["models"])

print("\nArchitecture Pipeline:")
print(" -> ".join(result["pipeline"]))

print("\nEstimated Cost per Request:")
print("$", result["estimated_cost"])

print("\nComplexity Score:")
print(result["complexity_score"])

print("\nSystem Simulation:")
print("Estimated Latency (ms):", result["simulation"]["estimated_latency_ms"])

print("Throughput (req/sec):", result["simulation"]["estimated_throughput_rps"])
print("Scalability Risk:", result["simulation"]["scalability_risk"])

print("\nConfidence Score:")
print(result["confidence"], "%")