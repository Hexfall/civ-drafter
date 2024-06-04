import json
from pathlib import Path

rule_path = Path(__file__).parent.parent.joinpath('data/rules.txt').absolute()


class RuleModel:
    def __init__(self) -> None:
        self.rules = {
            "civs": 3,
            "mulligan": True,
        }
        self._load()

    def _load(self) -> None:
        if rule_path.exists():
            with open(rule_path, 'r') as f:
                self.rules.update(json.load(f))

    def save(self) -> None:
        with open(rule_path, 'w') as f:
            json.dump(self.rules, f, indent=2)
