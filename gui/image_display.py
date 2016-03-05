""" Display image sequence using matplotlib."""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class ImageSequenceRenderer(object):
    """ renders sequence of images provided by ImageSequence """
    def __init__(self, image_sequence):

        fig, ax = plt.subplots()

        self.seq = image_sequence
        self.image = self.seq.init_image()

        plt.subplot(111)
        plt.title('Dinic')
        self.plot = plt.imshow(self.image)

        # plt.subplots_adjust(bottom=0.2)
        plt.subplots_adjust(bottom=0.2)
        axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
        bnext = Button(axnext, 'Next')
        bnext.on_clicked(self.next)

        plt.show()

    def next(self, event):
        if self.seq.complete():
            plt.subplot(111)
            plt.title('Completed!')  # TODO better way to show it has completed
            plt.draw()
            return
        self.image = self.seq.next_image()
        if self.image is not None:
            self.plot.set_data(self.image)
            plt.draw()


class ImageSequence(object):
    """ Class interface to give to ImageSequenceRenderer """
    def __init__(self):
        self.i = 0
        self.count = 0
        self.pics = map(mpimg.imread, ['bw.png', 'hello.jpg'])

    def init_image(self):
        return self.pics[self.i]

    def next_image(self):
        self.i = 1 - self.i
        self.count = self.count + 1
        return self.pics[self.i]

    def complete(self):
        return self.count >= 10


def start_gui(imageSequence):
    imageSequenceRenderer = ImageSequenceRenderer(imageSequence)
