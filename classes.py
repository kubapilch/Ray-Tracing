import pygame
import math

class Wall():
    def __init__(self, A, B):
        self.A = A
        self.B = B

class Ray():
    def __init__(self, start_pos, angle):
        self.start_pos = start_pos
        self.angle = angle
        self.helper_pos = self.getHelperPoint(pygame.display.get_surface().get_width())
        # Set same as helper if there is no walls and ray has to go out of the screen
        self.end_point = self.getHelperPoint(pygame.display.get_surface().get_width())
    
    def getHelperPoint(self, lenght):
        # Is needed for calculating intersections
        # Get a point from starting pos, angle and lenght of vector
        return (lenght * math.cos(math.radians(self.angle)) + self.start_pos[0], lenght * math.sin(math.radians(self.angle)) + self.start_pos[1])


class Button():
    def __init__(self, x, y, width, height, text, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, t):
        # Render new label
        self._text = t
        self.label = pygame.font.SysFont("monospace", 10).render(t, 1, (0, 0, 0))

    def values(self):
        return (self.x, self.y, self.width, self.height)

    def draw(self, surface):
        # Draw button
        pygame.draw.rect(surface, self.color, self.values())
        # Draw label
        surface.blit(self.label, (self.x + (self.width/2 - self.label.get_width()/2), self.y+(self.height/2 - self.label.get_height()/2)))
    
    def clicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False