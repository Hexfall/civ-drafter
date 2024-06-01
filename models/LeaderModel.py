from json import loads, dumps
from pathlib import Path
leader_path = Path(__file__).parent.parent.joinpath('data/leaders.txt').absolute()
default_leader_path = Path(__file__).parent.parent.joinpath('data/default_leaders.txt').absolute()


class CivModel:
    def __init__(self):
        self.leaders: dict = {}
        self.__load()
        self.__save()

    def __load(self):
        if leader_path.exists():
            with open(leader_path, 'r', encoding="utf-8") as f:
                self.leaders = loads(f.read())
        else:
            with open(default_leader_path, 'r', encoding="utf-8") as f:
                self.leaders = loads(f.read())

    def __save(self):
        with open(leader_path, 'w', encoding="utf-8") as f:
            f.write(dumps(self.leaders, indent=2))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__save()

    def is_selected(self, id: int) -> bool:
        return self.leaders[id]['selected']

    def get_summary(self):
        items = []
        for id, leader in self.leaders.items():
            items.append((["[*]" if self.is_selected(id) else "[ ]", leader['civ'], leader['leader']], id))
        return items
