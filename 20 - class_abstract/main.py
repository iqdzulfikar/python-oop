"""
20 - Abstract Class
Class biasa -> blue print dari object
Abstract Class --> blue print dari sebuah class untuk subclassnya ngeimplementasi method yg dimilikinya

abc(nama class) -> (Class ABC) Abstract Base Class -> utk membuat sebuah class menjadi abstract
abstractmethod -> utk membuat sebuah method menjadi abstract
"""
from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class PushButton(Button):

    # meng-override click() di class Button, dan ini harus dilakukan (karena Button merupakan class Abstract)
    def click(self):
        print("Push Button Click!")


class RadioButton(Button):

    # meng-override click() di class Button, dan ini harus dilakukan (karena Button merupakan class Abstract)
    def click(self):
        print("Radio Button Click!")


tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()
