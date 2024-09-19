import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initiates one instance of the Pygame module, which will be used throughout this game. 
    # Only this one instance will ever be created for the duration of the game.
    pygame.init()
    
    # Logging to the console
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Display window size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Will be used or frame rate limit and associated timings
    clock = pygame.time.Clock()
    dt = 0

    # Groups of objects in the game
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Initialize the "containers" class/static variable that will keep track of which groups 
    # every new object of the following types, should be assigned to. The Circle parent class 
    # has logic in the constructor to look for the "containers" variable, look for which groups
    # to add the object to and add it to those groups, which are iterable.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Create a player object in the centre of the game window
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # Game loop
    while True:
        # Make the close button functional - clicking on the [x] button closes the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # update all the objects in the updatable group, periodically
        for obj in updatable:
            obj.update(dt)


        for asteroid in asteroids:
            # Ends game if player collides with an asteroid.
            if asteroid.collision(player):
                raise SystemExit("Game over!")
            
            # Handles any of the asteroids colliding with any of the shots (i.e. player shoots an asteroid)
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split() # handle the login of whether or not to split the asteroid and if so, what size?
                    shot.kill() # remove the shot that collided with the asteroid

        # after all updates have been made, draw the object onto the screen
        for obj in drawable:
            obj.draw(screen)
       

        pygame.display.flip()

        # Frame rate is 60 frames / 1000 milliseconds
        dt = clock.tick(60)/1000
        
# Only run the main method if it is called from this file.    
if __name__ == "__main__":
    main()
