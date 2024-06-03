from pathlib import Path

from asciimatics.exceptions import NextScene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, MultiColumnListBox, Widget, Layout, Divider, Button, Text

from models import LeaderModel

val_path = Path(__file__).parent.parent.joinpath('data/val.txt').absolute()

class LeaderView(Frame):
    def __init__(self, screen: Screen, leader_model: LeaderModel):
        super().__init__(screen,
                         screen.height,
                         screen.width,
                         on_load=self._reload_list,
                         hover_focus=True,
                         can_scroll=False,
                         title="Leader List")

        self._model: LeaderModel = leader_model
        self._only_active: bool = False

        self._list_view = MultiColumnListBox(
            Widget.FILL_FRAME,
            [4, "<18", "<0"],
            self._model.get_summary(None, self._only_active),
            name="leaders",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._edit,
        )

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())

        # Buttons
        layout2 = Layout([1, 1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Ok", self._quit), 0)
        layout2.add_widget(Button("Enable all", self._select_all), 1)
        layout2.add_widget(Button("Disable all", self._unselect_all), 2)
        self._toggle_show_selected_button = Button("Show only enabled", self._toggle_show_selected)
        layout2.add_widget(self._toggle_show_selected_button, 3)
        self._search = Text("Search:", name="search", on_change=self._search)
        layout2.add_widget(self._search, 4)
        self.fix()

    def _on_pick(self):
        pass

    def _edit(self):
        self.save()
        selected_index = self.data["leaders"]
        self._model.toggle_selected(selected_index)
        self._reload_list(selected_index)

    def _reload_list(self, new_value=None):
        data = self._model.get_summary(self._search.value, self._only_active)
        self._list_view.options = data

        if new_value is not None:
            while new_value != 0:
                if any([new_value in t for t in data]):
                    self._list_view.value = new_value
                    break
                new_value -= 1

    def _select_all(self):
        self._model.select_all()
        self._reload_list(self._list_view.value)

    def _unselect_all(self):
        self._model.unselect_all()
        self._reload_list(self._list_view.value)

    def _toggle_show_selected(self):
        self._only_active = not self._only_active
        self._toggle_show_selected_button.text = "Show all" if self._only_active else "Show only enabled"
        self._reload_list(self._list_view.value)

    def _search(self):
        self._reload_list(self._list_view.value)

    def _quit(self):
        self._model.save()
        raise NextScene("Menu")
