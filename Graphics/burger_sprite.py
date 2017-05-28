# Спрайт-бургер


from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

burger_image = games.load_image("burger_syrom_fri.png")
burger = games.Sprite(image = burger_image, x = 320, y = 240)
games.screen.add(burger)

games.screen.mainloop()
