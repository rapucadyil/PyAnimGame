import pygame
import sys

def load_image (name):
    image = pygame.image.load(name)
    return image

class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, top, left, width, height):
        """
        constructor
        """
        super(AnimatedSprite, self).__init__()
        self.frames = []
        # append frame imags here
        self.frames.append(pygame.image.load("assets/gfx/bubba_run1.gif"))
        self.frames.append(pygame.image.load("assets/gfx/bubba_run2.gif"))
        self.frames.append(pygame.image.load("assets/gfx/bubba_run3.gif"))
        self.frames.append(pygame.image.load("assets/gfx/bubba_run4.gif"))
        self.frames.append(pygame.image.load("assets/gfx/bubba_run5.gif"))
        self.frames.append(pygame.image.load("assets/gfx/bubba_run6.gif"))

        self.index = 0
        self.current = self.frames[self.index]
        self.src_rect = pygame.Rect(top, left, width, height)



    def animate (self):
        """
        updates this animated sprites animation
        """
        self.index += 1

        if self.index >= len(self.frames):
            self.index = 0

        self.current = self.frames[self.index]

    
if __name__ == "__main__":
    anim = AnimatedSprite(10,10,64,64)
    print(len(anim.frames))