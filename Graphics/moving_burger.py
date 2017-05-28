# Летающий burger
# движущиеся спрайты

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50) 

wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

burger_image = games.load_image("burger_syrom_fri.png")
the_burger = games.Sprite(image = burger_image,
                         x = games.screen.width/2,
                         y = games.screen.height/2,
                         dx = 1,
                         dy = 1)
games.screen.add(the_burger)

games.screen.mainloop()

