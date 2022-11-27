from ursina import *
import orjson as json
# initialize
app = Ursina()

window.fullscreen = False
window.borderless = False
window.fps_counter.visible = False

start = False

def get_cube_pos():
    with open('./path.json', 'rb') as f:
        data = json.loads(f.read())

    path = data['path']
    
    for i in range(0, len(path), 2):
        yield path[i], path[i+1]


t = get_cube_pos()

# loading models
island = Entity(model='island', path='Assets/Models', scale=(0.2, 0.2, 0.2), position=(0, 0, 0))

pos, rot = next(t)
temp = Entity(model='cube', scale=(0.001, 0.001, 0.001), position=pos, rotation=rot)


sf = SmoothFollow(target=temp, offset=(0,0,0), speed=1, rotation_speed=1, rotation_offset=(0,0,0))
sf = camera.add_script(sf)

def dist(a, b):
    return (
        (a.x - b.x)**2 +
        (a.y - b.y)**2 +
        (a.z - b.z)**2
    )**0.5



def update_cube_position():
    global sf, t

    try:
        pos, rot = next(t)
        temp.world_position = pos
        temp.world_rotation = rot
    except StopIteration:
        pass



def input(key):
    global start
    if key == 'space':
        start = True


def update():
    if start:
        if dist(temp.world_position, camera.world_position) < 10 or dist(temp.world_rotation, camera.world_rotation) < 5:
            update_cube_position()

#running app
app.run()