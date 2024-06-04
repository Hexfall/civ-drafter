import sys

from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from models.LeaderModel import LeaderModel
from models.PlayerModel import PlayerModel
from models.RuleModel import RuleModel

from views.DraftView import DraftView
from views.LeaderView import LeaderView
from views.MenuView import MenuView
from views.PlayerView import PlayerView
from views.RuleView import RuleView


def demo(screen, scene, leader_model: LeaderModel, player_model: PlayerModel, rule_model: RuleModel) -> None:
    scenes = [
        Scene([MenuView(
            screen,
            lambda: leader_model.get_selected_count() >= player_model.get_player_count() * rule_model.get_player_civs())],
            -1,
            name="Menu"
        ),
        Scene([LeaderView(screen, leader_model)], -1, name="Leader List"),
        Scene([PlayerView(screen, player_model)], -1, name="Player List"),
        Scene([RuleView(screen, rule_model)], -1, name="Rules"),
        Scene([DraftView(screen, leader_model, player_model, rule_model)], -1, name="Draft"),
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


def main():
    last_scene = None
    while True:
        try:
            Screen.wrapper(
                demo,
                catch_interrupt=True,
                arguments=[last_scene, LeaderModel(), PlayerModel(), RuleModel()],
            )
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene


if __name__ == "__main__":
    main()
