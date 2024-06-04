import sys

from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from models.LeaderModel import CivModel
from models.PlayerModel import PlayerModel
from models.RuleModel import RuleModel
from views.LeaderView import LeaderView
from views.MenuView import MenuView
from views.PlayerView import PlayerView
from views.RuleView import RuleView


def demo(screen, scene, civ_model: CivModel, player_model: PlayerModel, rule_model: RuleModel) -> None:
    scenes = [
        Scene([MenuView(screen)], -1, name="Menu"),
        Scene([LeaderView(screen, civ_model)], -1, name="Leader List"),
        Scene([PlayerView(screen, player_model)], -1, name="Player List"),
        Scene([RuleView(screen, rule_model)], -1, name="Rules"),
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


def main():
    civ_model = CivModel()
    player_model = PlayerModel()
    rule_model = RuleModel()
    last_scene = None
    while True:
        try:
            Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene, civ_model, player_model, rule_model])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene


if __name__ == "__main__":
    main()
