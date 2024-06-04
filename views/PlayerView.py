from asciimatics.exceptions import NextScene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Widget, ListBox, Layout, Divider, Button, Text

from models.PlayerModel import PlayerModel


class PlayerView(Frame):
    def __init__(self, screen: Screen, player_model: PlayerModel):
        super().__init__(screen,
                         screen.height,
                         screen.width,
                         on_load=self._reload_list,
                         hover_focus=True,
                         can_scroll=False,
                         title="Leader List")

        self._model: PlayerModel = player_model

        layout = Layout([1], fill_frame=True)
        self.add_layout(layout)

        # Player List
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            self._model.get_summary(),
            name="leaders",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._edit,
        )
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())

        # Buttons
        layout2 = Layout([1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Ok", self._quit), 0)
        self._add_button = Button("Add", self._add)
        layout2.add_widget(self._add_button, 1)
        self._player_name = Text(label="Name:", on_change=self._name_change)
        layout2.add_widget(self._player_name, 2)

        self.fix()

    def _on_pick(self):
        pass

    def _name_change(self):
        self._add_button.disabled = self._player_name.value is None or self._player_name.value.strip() == ""

    def _add(self):
        self._reload_list(
            self._model.add_player(self._player_name.value)
        )

    def _edit(self):
        self._model.remove_player(self._list_view.value)
        self._reload_list(self._list_view.value)

    def _reload_list(self, new_value=None):
        data = self._model.get_summary()
        self._list_view.options = data

        if new_value is not None:
            while new_value != 0:
                if any([new_value in t for t in data]):
                    self._list_view.value = new_value
                    break
                new_value -= 1

    def _quit(self):
        self._model.save()
        raise NextScene("Menu")
