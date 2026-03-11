class ArchitecturePipeline:

    def generate(self, tasks):

        pipeline = ["User", "API Gateway"]

        if "text_generation" in tasks:
            pipeline.append("LLM Service")

        if "image_generation" in tasks:
            pipeline.append("Image Model")

        if "speech_to_text" in tasks:
            pipeline.append("Speech Recognition Service")

        if "text_to_speech" in tasks:
            pipeline.append("Voice Synthesis Service")

        pipeline.append("Storage")
        pipeline.append("Frontend")

        return pipeline