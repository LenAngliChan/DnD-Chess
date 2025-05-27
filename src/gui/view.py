import arcade
from typing import Any

from src.models.board import Board, Cell
from src.utils.constants import (
    CELL_SIZE,
)


class Chess(arcade.View):
    """Модель игры"""

    def __init__(self):
        """Инициализация игры"""

        super().__init__()
        self.background_color = arcade.color.GRAY

        self.camera = arcade.Camera2D()
        # self.map_section = arcade.Section(
        #     name="BattleMap",
        #     left=0,
        #     bottom=0,
        #     width=6 * CELL_SIZE,
        #     height=self.window.height
        # )
        # self.side_section = arcade.Section(
        #     name="UnderGround",
        #     left=6 * CELL_SIZE,
        #     bottom=0,
        #     width=2 * CELL_SIZE,
        #     height=self.window.height
        # )
        #
        # self.sm = arcade.SectionManager(view=self)
        # self.sm.add_section(self.map_section)
        # self.sm.add_section(self.side_section)

        self.board = Board()
        self.cell_list = arcade.SpriteList()
        self.figure_list = arcade.SpriteList()
        self.building_list = arcade.SpriteList()

    def setup(self):
        """Начало игры"""

        self.board.initialize_cells()
        self.board.initialize_buildings()
        self.board.initialize_figures()
        self.board.fill_domains()

        for cell in self.board.cells.values():
            self.cell_list.append(cell)

        for figure in self.board.figures.values():
            self.figure_list.append(figure)

        for building in self.board.buildings.values():
            self.building_list.append(building)

        self.board.start_circle()

    def on_resize(self, width, height):
        """Resize window"""
        super().on_resize(width, height)
        self.camera.match_window()

    # def on_show_view(self) -> None:
    #     self.sm.enable()
    #
    # def on_hide_view(self) -> None:
    #     self.sm.disable()

    def on_draw(self):
        """Нарисовать элементы игры"""
        self.clear()

        self.cell_list.draw()
        self.building_list.draw()
        self.figure_list.draw()

    def update(self):
        pass

    def on_mouse_press(
        self,
        x: int,
        y: int,
        button: int,
        key_modifiers: Any,
    ):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            sprites = arcade.get_sprites_at_point(
                point=(x, y),
                sprite_list=self.cell_list,
            )
            if sprites:
                cell = sprites[0]
                if isinstance(cell, Cell):
                    self.board.select_cell(cell=cell)
                    print(self.board.current_cell.name)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            if self.board.current_cell:
                current_action, target_cell = None, None
                sprites = arcade.get_sprites_at_point(
                    point=(x, y),
                    sprite_list=self.cell_list,
                )
                if sprites:
                    cell = sprites[0]
                    if isinstance(cell, Cell):
                        target_cell = cell
                if target_cell and target_cell in self.board.get_cell_neighbors():
                    value = "use" if target_cell.figure else "move"
                    actions = self.board.current_cell.figure.get_action_list()
                    for action in actions:
                        if action.attribute == value:
                            current_action = action
                            break
                    self.board.select_action(action=current_action)
                    print(self.board.current_action.name)
                    self.board.select_target(target=target_cell)
                else:
                    print("Необходимо выбрать клетку в пределах доступа (по горизонтали или вертикали)")

    # def draw_selected_cell(self):
    #     self.cell.color = arcade.color.GREEN
    #     around_indexes = self.cell.select()
    #     for index in around_indexes:
    #         around_cell = self.board.cells.get(index)
    #         if around_cell:
    #             around_cell.color = arcade.color.YELLOW
    #             self.around_cells.append(around_cell)
    #
    # def clear_cell_selection(self):
    #     self.cell.color = self.cell.domain.color
    #     for cell in self.around_cells:
    #         cell.color = self.cell.domain.color
