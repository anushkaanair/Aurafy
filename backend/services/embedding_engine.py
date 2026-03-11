from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class EmbeddingEngine:

    def __init__(self):

        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def embed(self, text):

        return self.model.encode([text])[0]

    def similarity(self, vec1, vec2):

        return cosine_similarity([vec1], [vec2])[0][0]