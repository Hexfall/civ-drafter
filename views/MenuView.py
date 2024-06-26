from asciimatics.exceptions import StopApplication, NextScene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Layout, Button, Divider, Widget


class MenuView(Frame):
    def __init__(self, screen: Screen, valid_draft):
        super().__init__(screen,
                         screen.height,
                         screen.width,
                         on_load=self._on_load,
                         hover_focus=True,
                         can_scroll=False,
                         title="Menu")

        layout = Layout([1], fill_frame=False)
        self.add_layout(layout)
        self.valid_draft = valid_draft

        layout.add_widget(Divider(draw_line=False, height=2))
        layout.add_widget(Button("Leader List", self._leader_list))
        layout.add_widget(Divider(draw_line=False, height=2))
        layout.add_widget(Button("Player List", self._player_list))
        layout.add_widget(Divider(draw_line=False, height=2))
        layout.add_widget(Button("Rules", self._rules_list))
        layout.add_widget(Divider(draw_line=False, height=2))
        self._draft_button = Button("Draft", self._draft)
        layout.add_widget(self._draft_button)
        layout.add_widget(Divider(draw_line=False, height=2))
        layout.add_widget(Button("Exit", self._quit))

        self.fix()

    def _leader_list(self):
        raise NextScene("Leader List")

    def _player_list(self):
        raise NextScene("Player List")

    def _rules_list(self):
        raise NextScene("Rules")

    def _draft(self):
        raise NextScene("Draft")

    def _quit(self):
        raise StopApplication("User pressed quit")

    def _on_load(self):
        self._draft_button.disabled = not self.valid_draft()
