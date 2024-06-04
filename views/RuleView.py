from asciimatics.exceptions import NextScene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Layout, Divider, Button, Label

from models import RuleModel


class RuleView(Frame):
    def __init__(self, screen: Screen, rule_model: RuleModel) -> None:
        super().__init__(screen,
                         screen.height,
                         screen.width,
                         hover_focus=True,
                         can_scroll=False,
                         title="Rules")

        self._model: RuleModel = rule_model

        layout = Layout([1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Label("Come back later", align='^'))

        layout2 = Layout([1])
        self.add_layout(layout2)
        layout2.add_widget(Divider())
        layout2.add_widget(Button("Ok", self._quit))

        self.fix()

    def _quit(self):
        self._model.save()
        raise NextScene("Menu")
