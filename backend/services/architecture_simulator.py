class ArchitectureSimulator:

    def simulate(self, pipeline):

        base_latency = 50  # base ms
        service_latency = 40  # per service

        services = len(pipeline)

        estimated_latency = base_latency + (services * service_latency)

        throughput = max(1000 - (services * 100), 100)

        risk = "Low"

        if services > 6:
            risk = "Medium"

        if services > 8:
            risk = "High"

        return {
            "estimated_latency_ms": estimated_latency,
            "estimated_throughput_rps": throughput,
            "scalability_risk": risk
        }