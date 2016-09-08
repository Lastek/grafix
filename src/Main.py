#Author: Cyberstorm
# Created on: 9/7/2016 | 10:52 PM

import ioproc
import ctypes
import time as tms
import numpy as np
import OpenGL as gl
import pyglut as pgl
import sdl2
import transformations

TITLE = "OoooooOOooOooooOOOOoooh!"
class Renderer:
    def __init__(self):
        return

def main():
    global rend

    if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
        print(sdl2.SDL_GetError())
        return 0

    x, y = 0, 0

    # window = sdl2.ext.Window("ekkek", 600,600, sdl2.SDL_WINDOW_OPENGL)
    window = sdl2.SDL_CreateWindow(TITLE, sdl2.SDL_WINDOWPOS_UNDEFINED,
                                   sdl2.SDL_WINDOWPOS_UNDEFINED, 600, 600,
                                   sdl2.SDL_WINDOW_OPENGL)
    context = sdl2.SDL_GL_CreateContext(window)
    rend = Renderer()
    time = sdl2.SDL_GetTicks()
    prev_time = sdl2.SDL_GetTicks()
    frame_time = 0
    e = ioproc(sdl2.SDL_Event())
    dt = 1000. / 60.

    #while sdl2.SDL_WaitEvent(ctypes.byref(sdl2.SDL_QUIT)):
    while e.checkEvents():
        # time = sdl2.SDL_GetTicks()
        # frame_time = time - prev_time
        # prev_time = time
        # while sdl2.SDL_PollEvent(ctypes.byref(e)) !=0:
        #     if(e.type == sdl2.SDL_QUIT):
        #         running = False

        time += dt
        frame_time = time - sdl2.SDL_GetTicks()
        if (frame_time <= 0):
            frame_time = 1
        tms.sleep(frame_time / 1000.)

        # update shit here
        # ...
        rend.doShit()
        rend.draw()
        sdl2.SDL_GL_SwapWindow(window)

    # rend.unload()     #Unload assimp imports
    sdl2.SDL_GL_DeleteContext(context)
    sdl2.SDL_Quit()

