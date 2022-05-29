"""
21 - Abstract Class dan Decorator

"""
from abc import ABC, abstractmethod


class Button(ABC):

    def __init__(self, in_link):
        self.link = in_link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass


class PushButton(Button):

    def click(self):
        print("Go to: {}".format(self.link))

    @Button.link.setter
    def link(self, in_link):
        self.link = in_link

    @link.getter
    def link(self):
        return self.link


tombol1 = PushButton("dzul.com")
tombol1.click()
