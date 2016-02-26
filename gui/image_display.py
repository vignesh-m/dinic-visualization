""" Display image sequence using matplotlib."""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class ImageSequenceRenderer(object):
    """ renders sequence of images provided by ImageSequence """
    def __init__(self, image_sequence):
        self.seq = image_sequence
        self.image = self.seq.init_image()
        plt.subplot(211)
        self.plot = plt.imshow(self.image)

    def next(self, event):
        self.image = self.seq.next_image()
        self.plot.set_data(self.image)
        plt.draw()


class ImageSequence(object):
    """ Class interface to give to ImageSequenceRenderer """
    def __init__(self):
        self.i = 0
        self.pics = map(mpimg.imread, ['bw.png', 'hello.jpg'])

    def init_image(self):
        return self.pics[self.i]

    def next_image(self):
        self.i = 1 - self.i
        return self.pics[self.i]


def start_gui(imageSequence):
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    imageSequenceRenderer = ImageSequenceRenderer(imageSequence)
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(imageSequenceRenderer.next)
    plt.show()
