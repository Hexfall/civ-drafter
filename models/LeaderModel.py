import json
from pathlib import Path

leader_path = Path(__file__).parent.parent.joinpath('data/leaders.txt').absolute()
default_leader_path = Path(__file__).parent.parent.joinpath('data/default_leaders.txt').absolute()


class CivModel:
    def __init__(self):
        self.leaders: list = []
        self.__load()
        self.save()

    def __load(self):
        if leader_path.exists():
            with open(leader_path, 'r', encoding="utf-8") as f:
                self.leaders = json.load(f)
        else:
            with open(default_leader_path, 'r', encoding="utf-8") as f:
                self.leaders = json.load(f)
        self.leaders.sort(key=lambda leader: leader['civ'] + leader['leader'])

    def save(self):
        with open(leader_path, 'w', encoding="utf-8") as f:
            json.dump(self.leaders, f, indent=2)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save()

    def is_selected(self, index: int) -> bool:
        return self.leaders[index]['selected']

    def get_summary(self, search: str, only_selected: bool = False) -> list[tuple[list, int]]:
        items = []
        for index, leader in enumerate(self.leaders):
            if not only_selected or self.is_selected(index):
                if search is not None and search != "":
                    if search.lower() in leader['civ'].lower() or search.lower() in leader['leader'].lower():
                        items.append(
                            (["[*]" if self.is_selected(index) else "[ ]", leader['civ'], leader['leader']], index))
                else:
                    items.append(
                        (["[*]" if self.is_selected(index) else "[ ]", leader['civ'], leader['leader']], index))
        return items

    def toggle_selected(self, index: int):
        self.leaders[index]['selected'] = not self.leaders[index]['selected']

    def select_all(self):
        for leader in self.leaders:
            leader['selected'] = True

    def unselect_all(self):
        for leader in self.leaders:
            leader['selected'] = False
