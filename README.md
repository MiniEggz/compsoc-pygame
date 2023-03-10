# CompSoc PyGame workshop

NOTE: this workshop is an adaptation of the work by https://www.youtube.com/@ClearCode.

Their git repository can be accessed here: https://github.com/clear-code-projects/2D_Platformer_Logic.

We have tried to comment the code as verbosely as possible to make it as easy to understand as possible, but give us a shout if things aren't making sense.

## Contents...
1. [Getting Started](#start)
1.1. [Setting Up Python](#setup)
1.2. [Installing Pygame](#install-pygame)
1.3. [Cloning Our Repo](#setup-project)
2. [Making Our First Game](#first-game)
2.1. [Basic Setup of PyGame](#basic-setup)
2.2. [Level Design](#level-design)
2.3. [The Player](#the-player)
3. [Challenges](#challenges)

<a name="start"></a>
## Getting started

<a name="setup"></a>
#### Setting up python
First things first, open up the "Python Command Prompt" (press windows key and search for "python").

<a name="install-pygame"></a>
### Installing pygame
Now we need to install pygame using the python command prompt...
```bash
pip install pygame
```

<a name="setup-project"></a>
### Clone Our Repo

From here, you want to make sure your terminal is in the right place: the U drive.
```bash
cd U:
```

Clone our repo so you can start playing around with things.
```bash
git clone git@github.com:MiniEggz/compsoc-pygame.git
```

cd into the repo
```bash
cd compsoc-pygame
```

<a name="first-game"></a>
## Playing around with our first game!

<a name="basic-setup"></a>
### Basic setup
There is an initial setup we will need to do in pretty much all of the games made in pygame. This basic setup will look something like this:

```python
import pygame

# pygame setup
pygame.init()
screen_size = width, height = (800, 800)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # drawing logic
    screen.fill("green")
    pygame.display.update()
    clock.tick(60)

pygame.quit()
```

<a name="level-design"></a>
### Level design
Level design can be done in a number of different ways, most of which are very complex and completely out of scope for today. The method of level design we've gone for today helps us create different levels extremely quickly.

The player start position is marked by 'P', blocks are marked by 'X' and empty space is just marked by a space (' ').

In Simple, the win block is denoted 'E' and in basic_mario, the win block is denoted 'W'.

All code involved in level design can be found mainly in level.py and tiles.py - settings.py also contains some level data.

<a name="the-player"></a>
### The Player
Creating the player is obviously a very important part of creating a game. You need to decide how the player will move, how they can interact with their environment, what they will look like, etc...

All player information can be found in code/player.py.


<a name="challenges"></a>
# Challenges
* Clone this repository
* Run the code and have a run around!
* Can you create your own level and make sure the player doesn't get stuck anywhere?
* Can you change the background colour?
* Can you change the colour of the tiles used to create the level?
* Can you change the sprite image for the player?
* Can you change the speed of the player? What is too high or too low?
* Can you change the Simple code so you can move with A and D as well as the arrows (maybe add w as jump)?
