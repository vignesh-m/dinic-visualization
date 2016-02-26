""" Display image sequence using matplotlib."""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class ImageSequence(object):

    def __init__(self):
        self.i = 1
        self.pics = [mpimg.imread('bw.png'), mpimg.imread('hello.jpg')]
        plt.subplot(211)
        self.plot = plt.imshow(self.pics[self.i])

    def next(self, event):
        self.i = 1 - self.i
        self.plot.set_data(self.pics[self.i])
        plt.draw()


def start_gui():
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    imageSequence = ImageSequence()
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(imageSequence.next)
    plt.show()
