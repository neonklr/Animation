from ursina import *
# from Scripts import input_handler
from Scripts.free_hand_camera import FirstPersonController

# initialize
app = Ursina()

# loading models
island = Entity(model='island', path='Assets/Models', scale=(0.2, 0.2, 0.2), position=(0, 0, 0))
cursor = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.008, rotation_z=45)
mouse.locked = True
cursor.enabled = True

player = FirstPersonController()


def input(key):
    if key == 'p':
        print(f"{player.position}, {player.rotation}")

#running app
app.run()