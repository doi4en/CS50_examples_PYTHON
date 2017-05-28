# Паника в маке
# Игрок должен ловить падающий бургер, пока он не достиг земли

from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)


class Pan(games.Sprite):
    """
    Сковорода, в которую игрок может ловить падающий бургер.
    """
    image = games.load_image("pan.bmp")

    def __init__(self):
        """ Инициализирует объект Рап и создает объект Text для отображения счета """
        super(Pan, self).__init__(image = Pan.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)
        
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """ Передвигает объект по горизонтали """
        self.x = games.mouse.x
        
        if self.left < 0:
            self.left = 0
            
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_catch()

    def check_catch(self):
        """ Проверяет, поймал ли игрок падающий бургер """
        for burger in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            burger.handle_caught()


class Burger(games.Sprite):
    """
    бургеры, падающие на землю.
    """ 
    image = games.load_image("burger_syrom_fri.png")
    speed = 1   

    def __init__(self, x, y = 90):
        """ Инициализирует объект Burger """
        super(Burger, self).__init__(image = Burger.image,
                                    x = x, y = y,
                                    dy = Burger.speed)

    def update(self):
        """ Проверяет, не коснулась ли нижняя кромка спрайта нижней границы экрана """
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """ Разрушает объект, пойманный игроком. """
        self.destroy()

    def end_game(self):
        """ Завершает игру. """
        end_message = games.Message(value = "Вільна каса",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)


class Ronald(games.Sprite):
    """
    Рональд, который, двигаясь влево-вправо, разбрасывает бургеры
    """
    image = games.load_image("ron.png")

    def __init__(self, y = 55, speed = 2, odds_change = 200):
        """ Инициализирует объект Ronald """
        super(Ronald, self).__init__(image = Ronald.image,
                                   x = games.screen.width / 2,
                                   y = y,
                                   dx = speed)
        
        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        """ Определяет, надо ли сменить направление."""
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx
                
        self.check_drop()


    def check_drop(self):
        """ Уменьшает интервал ожидания на единицу или сбрасывает очередной бургер
        и восстанавливает исходный интервал """
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_burger = Burger(x = self.x)
            games.screen.add(new_burger)

            # вне зависимости от скорости падения бургера "зазор" между падающими бургерами принимается равным 30 % каждого из них по высоте
            self.time_til_drop = int(new_burger.height * 1.3 / Burger.speed) + 1


def main():
    """ собственно игра """
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    the_ronald = Ronald()
    games.screen.add(the_ronald)

    the_pan = Pan()
    games.screen.add(the_pan)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()

# начнем!
main()

