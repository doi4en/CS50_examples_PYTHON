# Скачущий бургер
# обработка столкновений с границами экрана

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50) 

class Burger(games.Sprite):
    """ скучающий бургер """
    def update(self):
        """ разворачивает одну или обе компоненты скорости, если достигнута граница экрана"""
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy

def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    burger_image = games.load_image("burger_syrom_fri.png")
    the_burger = Burger(image = burger_image,
                      x = games.screen.width/2,
                      y = games.screen.height/2,
                      dx = 1,
                      dy = 1)
    games.screen.add(the_burger)

    games.screen.mainloop()

# поехали
main()
