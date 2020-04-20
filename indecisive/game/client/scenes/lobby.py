import arcade
from .base import Base
import string
from .util import arcade_int_to_string


class Lobby(Base):
    def __init__(self, display):
        self.display = display

        self.spritelist = arcade.SpriteList()
        self.spritedict = dict()
        self.sceneTime = 0
        self.name = ""
        self.cursor_index = -1
        self.focus = None

        self.sprite_setup()

    def sprite_setup(self):
        self.spritedict = {
            "back": arcade.Sprite(
                "./assets/simple_button.png",
                scale=0.25,
                center_x=160,
                center_y=687.5
            ),
            "name": arcade.Sprite(
                "./assets/simple_button.png",
                scale=0.25,
                center_x=160,
                center_y=622.5
            )
        }
        self.spritelist.extend(list(self.spritedict.values()))

    def update(self, delta_time: float) -> None:
        self.sceneTime += delta_time

    def draw(self):
        self.spritelist.draw()
        if len(self.name) < 25:
            buffer = " " * (25 - len(self.name))
        else:
            buffer = ""
        arcade.draw_text(buffer + self.name[-25:], 15, 600, color=(255, 255, 255), font_size=35, width=560)

    def mouse_release(self, x: float, y: float, button: int, modifiers: int):
        print((x, y))
        if self.spritedict["back"].collides_with_point((x, y)) is True:
            self.display.change_scenes("loading", startup=False)
        elif self.spritedict["name"].collides_with_point((x, y)) is True:
            self.focus = "name"
        else:
            self.focus = None

    def key_press(self, key, modifiers):
        if self.focus == "name":
            if key == arcade.key.BACKSPACE:
                if self.cursor_index == -1:
                    self.name = self.name[:-1]
                else:
                    self.name = self.name[:self.cursor_index] + self.name[self.cursor_index + 1:]
            elif key == arcade.key.DELETE:
                if self.cursor_index == -1:
                    self.name = self.name[:-1]
                else:
                    self.name = self.name[:self.cursor_index + 1] + self.name[self.cursor_index:]
            elif key == arcade.key.LEFT:
                self.cursor_index -= 1
                if self.cursor_index <= - (len(self.name) + 2):
                    self.cursor_index = -1
            elif key == arcade.key.RIGHT:
                self.cursor_index += 1
                if self.cursor_index >= 0:
                    self.cursor_index = - (len(self.name) + 1)
            else:
                key = arcade_int_to_string(key, modifiers)
                if key != "":
                    if self.cursor_index == -1:
                        self.name = self.name + key
                    else:
                        self.name = self.name[:self.cursor_index + 1] + key + self.name[self.cursor_index + 1:]
