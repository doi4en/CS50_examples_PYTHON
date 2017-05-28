# Ускользающий бургер
# проверка на соприкосновение спрайтов

from livewires import games
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)


class Pan(games.Sprite):
    """" Сковорода, которую можно мышью перемещать по экрану. """
    def update(self):
        """ Перемещает спрайт в позицию, в которой находится указатель """
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()
 
    def check_collide(self):
        """ Проверяет, не соприкоснулись ли сковорода и бургер """
        for burger in self.overlapping_sprites:
            burger.handle_collide()


class Burger(games.Sprite):
    """" Ускользающий бургер """
    def handle_collide(self):
        """ Перемещает спрайт в случайную позицию на графическом экране. """
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)


def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    burger_image = games.load_image("burger_syrom_fri.png")
    burger_x = random.randrange(games.screen.width)
    burger_y = random.randrange(games.screen.height)
    the_burger = Burger(image = burger_image, x = burger_x, y = burger_y)
    games.screen.add(the_burger)

    pan_image = games.load_image("pan.bmp")
    the_pan = Pan(image = pan_image,
                  x = games.mouse.x,
                  y = games.mouse.y)
    games.screen.add(the_pan)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()

# поехали
main()
