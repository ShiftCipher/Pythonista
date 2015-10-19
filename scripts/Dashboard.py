#! usr/bin/env python 
from pyglet import *

#GLOBAL SETUP
#Set Config for OpenGL
config = pyglet.gl.Config(sample_buffers=1, samples=4)

#Create Borderless Window
canvas = pyglet.window.Window(config=config, resizable=False, style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS)

#Set Window Size
canvas.set_size(1080, 720)

#Set Windows Location
canvas.set_location(360,0)

#Record Windows Event
canvas.push_handlers(pyglet.window.event.WindowEventLogger())

#Global Values
scale = 0.25
speed = 9.78

#FUNCTIONS FOR DESKTOP
#Set Fullscreen

@canvas.event
#Press
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print "Mouse Click Left"
    
    if button == mouse.RIGHT:
        print "Mouse Click Right"
    
    if button == mouse.MIDDLE:
        print "Mouse Click Middle"

#Drag 
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    if button == mouse.LEFT:
        print "Mouse Click Drag"

#Motion
def on_mouse_motion(x, y, dx, dy):
    if button == mouse.LEFT:
        icono.x = dx

@canvas.event
def on_draw():
    canvas.clear()
    #Set Background Color 0,0,0,0 isnot Black is Traslucent
    #glClearColor(0,0,0,0)
    glClearColor(1,1,1,1)
    icono.draw()

    #GL Smooth Lines
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    glEnable( GL_POINT_SMOOTH )
    glEnable (GL_BLEND) 
    glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)      

def update(dt):
    icono.x += dt

#Set Update Funtion
pyglet.clock.schedule_interval(update, 0.1) 

pyglet.app.run()