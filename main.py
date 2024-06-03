import sys

from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from models.LeaderModel import CivModel
from views.LeaderView import LeaderView
from views.MenuView import MenuView


def demo(screen, scene, civ_model: CivModel):
    scenes = [
        Scene([MenuView(screen)], -1, name="Menu"),
        Scene([LeaderView(screen, civ_model)], -1, name="Leader List"),
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


def main():
    civ_model = CivModel()
    last_scene = None
    while True:
        try:
            Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene, civ_model])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene


if __name__ == "__main__":
    main()
