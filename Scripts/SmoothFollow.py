from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange)

def update():
    player.x += held_keys['d'] * .1
    player.x -= held_keys['a'] * .1

e = Entity(model='cube', position=(-4, -4, 0))
sf = e.add_script(SmoothFollow(target=player, offset=(0,-2,0)))

def input(key):
    global sf
    if key == '1' and sf in e.scripts:
        e.scripts.remove(sf)

    if key == '2':
        e.add_script(SmoothFollow(target=player, offset=(0,-1,0)))

EditorCamera()

app.run()