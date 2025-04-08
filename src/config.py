import os

class Config:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.model_name = os.getenv("MODEL_NAME", "default-model")
        self.max_tokens = int(os.getenv("MAX_TOKENS", 150))
        self.temperature = float(os.getenv("TEMPERATURE", 0.7))

    def validate(self):
        if not self.api_key:
            raise ValueError("API_KEY is not set in the environment variables.")
        if self.max_tokens <= 0:
            raise ValueError("MAX_TOKENS must be a positive integer.")
        if not (0 <= self.temperature <= 1):
            raise ValueError("TEMPERATURE must be between 0 and 1.")