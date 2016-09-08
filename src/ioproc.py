#Author: Cyberstorm
# Created on: 9/8/2016 | 12:15 AM
import numpy as np
import sdl2
import ctypes

class IOProc():
    """ Handles input and output to other classes """
    def __init__(self, e=0 ):
        """
        @param e: Takes SDL_Event() class
        @type e: sdl2.SDL_Event()
        @type t: Transform()
        :return: None
        """
        self.event = 0
        if self.initEvent(e) is 0:
            pass    #proceed with initialization
        self.mouseDown = False
        self.mousePos = np.array([0, 0], dtype="int32")
        self.running = True
    def initEvent(self, e):
        try:    #need to somehow check if correct class as well
            if(e != 0):
                self.event = e
                return 0
            else:
                raise Exception('e Needs to be SDL_Event() class')
        except Exception as exc:
            print(exc)
            a = exc.args
            print('e = ', a)
            return 1

    def checkEvents(self):
        """
        This just acts as a var switch and calls the process function
        @type self.event: sdl2.SDL_Event()
        @return: None
        """
        while sdl2.SDL_PollEvent(ctypes.byref(self.event)) !=0:
            if(self.event.type == sdl2.SDL_QUIT):
                self.running = False
            if(self.event.type == sdl2.SDL_MOUSEBUTTONDOWN):
                self.mouseDown = True
            if(self.event.type == sdl2.SDL_MOUSEBUTTONUP):
                self.mouseDown = False
            if(self.event.type == sdl2.SDL_MOUSEMOTION):
                    # print ("x: %i, y: %i" % (event.motion.x, event.motion.y))
                    self.mousePos[0] = self.event.motion.x
                    self.mousePos[1] = self.event.motion.y
                    # rend.mouseMove(self.event.motion.x, self.event.motion.y)
                    sdl2.SDL_FlushEvent(sdl2.SDL_MOUSEMOTION)
            self.process()
        return self.running
