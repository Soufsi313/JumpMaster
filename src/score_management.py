import json
import os

class ScoreManager:

    def __init__(self, filepath="data/scores.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump([], f)

    def save_score(self, score):
        try:
            with open(self.filepath, "r") as f:
                scores = json.load(f)
        except:
            scores = []
        scores.append(score)
        with open(self.filepath, "w") as f:
            json.dump(scores, f)

    def get_high_score(self):
        try:
            with open(self.filepath, "r") as f:
                scores = json.load(f)
            if scores:
                return max(scores)
            else:
                return 0
        except:
            return 0