from ursina import held_keys, time, camera, mouse, Vec2, clamp
import constants




def _check_mouse_navigations():
    mouse_sensitivity = Vec2(40, 40)
    camera.rotation_y += mouse.velocity[0] * mouse_sensitivity[1]

    camera.rotation_x -= mouse.velocity[1] * mouse_sensitivity[0]
    camera.rotation_x = clamp(camera.rotation_x, -90, 90)




def check_navigations():
        
    _check_keyboard_navigations()
    _check_mouse_navigations()