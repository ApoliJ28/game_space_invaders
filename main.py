from turtle import Screen
from nave import Nave
from alien import Aliens
from info_bar import InfoBar
import time

# interfaz

screen = Screen()
screen.bgcolor("black")
screen.setup(width=720, height=600)
screen.title("Space Invaders")
screen.tracer(0)

# Se agrega la nave a la interfaz en la pantalla
nave = Nave()
# Se agrega la barra de informacion
info_bar = InfoBar()
# Generar los aliens
aliens = Aliens()



screen.listen()

screen.onkeypress(nave.go_left, "Left")
screen.onkeypress(nave.go_right, "Right")
screen.onkey(nave.shoot_rocket, "space")

run_game = True

while run_game:
    screen.update()
    aliens.move()
    first_alien = aliens.firts_aliens[0]
    ultm_alien = aliens.last_aliens[0]
    time.sleep(0.001)
    
    if aliens.all_alien:
        if len(aliens.shoot_balls) <=3:
            aliens.shoot_alien()
    
        for ball in aliens.shoot_balls:
            ball.move_down()
            if ball.ycor() < - 300:
                ball.remove_ball()
                aliens.shoot_balls.remove(ball)
            if nave.rocket and ball.distance(nave.rocket) < 25:
                info_bar.score += 2
                info_bar.update_info()
                nave.remove_rocket()
                ball.remove_ball()
                aliens.shoot_balls.remove(ball)
            if ball.distance(nave) < 15:
                info_bar.lives -= 1
                info_bar.update_info()
                if info_bar.lives:
                    aliens.remove_all_balls()
                    nave.reset_position()
                else:
                    aliens.remove_all_balls()
                    info_bar.game_over()
                    run_game = False
    
    if nave.rocket: 
        nave.rocket.move_up()
        if nave.rocket.ycor() > 300:
            nave.remove_rocket()
    if first_alien.xcor() < -300:
        aliens.bounce_x_aliens()
    if ultm_alien.xcor() > 300:
        aliens.bounce_x_aliens()
    
    for alien in aliens.all_alien:
        if nave.rocket and alien.distance(nave.rocket) < 25:
            info_bar.score += 10
            info_bar.update_info()
            aliens.all_alien.remove(alien)
            alien.clear()
            alien.hideturtle()
            nave.remove_rocket()
    
    if not aliens.all_alien:
        screen.update()
        info_bar.win()
        break

# Cerrar ventana con un click
screen.exitonclick()