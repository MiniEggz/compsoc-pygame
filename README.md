# CompSoc PyGame workshop

NOTE: this workshop is an adaptation of the work by https://www.youtube.com/@ClearCode.

Their git repository can be accessed here: https://github.com/clear-code-projects/2D_Platformer_Logic.

## Contents...
1. [Getting Started](#start)
1.1. [Setting Up Python](#setup)
1.2. [Installing Pygame](#install-pygame)
1.3. [Setting Up Project Folder](#setup-project)
2. [Making Our First Game](#first-game)
2.1. [Basic Setup of PyGame](#basic-setup)
2.2. [Level Design](#level-design)
2.3. [The Player](#the-player)

<a name="start"></a>
## Getting started

<a name="setup"></a>
#### Setting up python
First things first, open up the "Python Command Prompt" (press windows key and search for "python").

<a name="install-pygame">
### Installing pygame
Now we need to install pygame using the command prompt...
```bash
pip install pygame
```

<a name="setup-project"></a>
### Setting up the python project

From here, you want to make sure your terminal is in the right place: the U drive.
```bash
cd U:
```

If you want to download all the files of the quick game concept we made, clone or fork our repository.
```bash
git clone git@github.com:MiniEggz/compsoc-pygame.git
```
Otherwise, you can just create a folder in the U drive and work from there. After setting up the project folder, cd into it with:
```bash
cd compsoc-pygame
```
if you are using our repo or
```bash
cd <your-folder-name>
```
if not.

<a name="first-game"></a>
## Moving onto making our first game!

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

All code involved in level design can be found mainly in level.py and tiles.py - settings.py also contains some level data.

<a name="the-player"></a>
### The Player
Creating the player is obviously a very important part of creating a game. You need to decide how the player will move, how they can interact with their environment, what they will look like, etc...

All player information can be found in code/player.py.
