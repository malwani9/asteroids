import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidsfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill((0,0,0))

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.colliding(player):
               print("Game over!")
               raise SystemExit()

            for shot in shots:
                 if asteroid.colliding(shot):
                     shot.kill()
                     asteroid.split()
                 
                    
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()