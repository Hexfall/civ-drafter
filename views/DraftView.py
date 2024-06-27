from asciimatics.exceptions import NextScene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Layout, Label, ListBox, VerticalDivider, Divider, Button

from models.LeaderModel import LeaderModel
from models.PlayerModel import PlayerModel
from models.RuleModel import RuleModel


class DraftView(Frame):
    def __init__(self, screen: Screen, leader_model: LeaderModel, player_model: PlayerModel, rule_model: RuleModel):
        super().__init__(screen,
                         screen.height,
                         screen.width,
                         hover_focus=True,
                         can_scroll=False,
                         on_load=self._populate,
                         title="Draft")

        self._leader_model: LeaderModel = leader_model
        self._player_model: PlayerModel = player_model
        self._rule_model: RuleModel = rule_model

        self._selected = [-1] * self._player_model.get_player_count()
        self._list_boxes: list[ListBox] = [None] * self._player_model.get_player_count()
        self._civs_to_draft: int = self._rule_model.get_player_civs()
        self._last_view = False

        # Player boxes
        self.layout = Layout([1])
        self.add_layout(self.layout)
        self._populate()

        # Bottom Buffer
        self.add_layout(Layout([1], fill_frame=True))

        # Button Divider
        button_divider = Layout([1])
        self.add_layout(button_divider)
        button_divider.add_widget(Divider())

        # Buttons
        button_layout = Layout([1])
        self.add_layout(button_layout)
        button_layout.add_widget(Button("Ok", self._ok), 0)

        self.fix()

    def _add_player(self, player_index: int, layout: Layout):
        if player_index != 0:
            layout.add_widget(Divider())
        layout.add_widget(Label(self._player_model.get_player(player_index), align='^'))
        self._list_boxes[player_index] = ListBox(
            self._rule_model.get_player_civs() + 1 if self._rule_model.can_mulligan() else 0,
            [],
        )
        layout.add_widget(self._list_boxes[player_index])

    def _can_mulligan(self):
        return self._rule_model.can_mulligan() and self._civs_to_draft > 1

    def _mulligan(self):
        self._civs_to_draft -= 1
        self._reload()

    def _reload(self):
        civs = self._leader_model.roll()
        for civ in self._selected:
            if civ != -1 and civ in civs:
                civs.pop(civs.index(civ))

        for i, lb in enumerate(self._list_boxes):
            if self._selected[i] == -1:
                lb.options = [self._leader_model.get_civ_summary(civs.pop()) for _ in range(self._civs_to_draft)] + ([("Mulligan", -1)] if self._can_mulligan() else [])
            else:
                lb.options = [self._leader_model.get_civ_summary(self._selected[i])]

    def _ok(self):
        for i, lb in enumerate(self._list_boxes):
            self._selected[i] = lb.value
        if -1 in self._selected:
            self._mulligan()
        elif not self._last_view and self._civs_to_draft > 1:
            self._last_view = not self._last_view
            self._reload()
        else:
            self._quit()

    def _quit(self):
        raise NextScene("Menu")

    def _populate(self):
        self._selected = [-1] * self._player_model.get_player_count()
        self._list_boxes: list[ListBox] = [None] * self._player_model.get_player_count()
        self._civs_to_draft: int = self._rule_model.get_player_civs()

        # Player boxes
        self.layout.clear_widgets()
        for i in range(self._player_model.get_player_count()):
            self._add_player(i, self.layout)
        self.layout.focus(True)

        self.fix()
        self._reload()
