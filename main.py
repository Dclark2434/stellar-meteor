import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

   
    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = (updatables)
    asteroid_field = AsteroidField()
    
    Player.containers = (updatables, drawables)


    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0))
        for drawable in drawables:
            drawable.draw(screen)
        updatables.update(dt)
        for asteroid in asteroids:
            if player.collision_with(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision_with(shot):
                    shot.kill()
                    asteroid.kill()

        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()