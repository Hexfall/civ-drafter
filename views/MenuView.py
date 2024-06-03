from asciimatics.exceptions import StopApplication, NextScene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Layout, Button, Divider, Widget


class MenuView(Frame):
    def __init__(self, screen: Screen):
        super().__init__(screen,
                         screen.height,
                         screen.width,
                         hover_focus=True,
                         can_scroll=False,
                         title="Menu")

        layout = Layout([1], fill_frame=False)
        self.add_layout(layout)

        layout.add_widget(Divider(draw_line=False, height=2))
        layout.add_widget(Button("Leader List", self._leader_list))
        layout.add_widget(Divider(draw_line=False, height=2))
        layout.add_widget(Button("Player List", self._player_list))
        layout.add_widget(Divider(draw_line=False, height=2))
        layout.add_widget(Button("Rules List", self._rules_list))
        layout.add_widget(Divider(draw_line=False, height=2))
        layout.add_widget(Button("Draft", self._draft))
        layout.add_widget(Divider(draw_line=False, height=2))
        layout.add_widget(Button("Exit", self._quit))

        self.fix()

    def _leader_list(self):
        raise NextScene("Leader List")

    def _player_list(self):
        raise NextScene("Player List")

    def _rules_list(self):
        raise NextScene("Rules List")

    def _draft(self):
        raise NextScene("Draft")

    def _quit(self):
        raise StopApplication("User pressed quit")
