import json
from pathlib import Path

player_path = Path(__file__).parent.parent.joinpath('data/players.txt').absolute()


class PlayerModel:
    def __init__(self) -> None:
        self.players = []
        self._load()

    def _load(self) -> None:
        if player_path.exists():
            with open(player_path, 'r') as f:
                self.players = json.load(f)

    def save(self) -> None:
        with open(player_path, 'w') as f:
            json.dump(self.players, f, indent=2)

    def add_player(self, player: str) -> int:
        self.players.append(player.strip())
        return len(self.players) - 1

    def remove_player(self, index: int) -> None:
        del self.players[index]

    def get_summary(self) -> list[tuple[str, int]]:
        return [(p, i) for i, p in enumerate(self.players)]
