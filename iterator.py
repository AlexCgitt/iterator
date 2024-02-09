import sys
from abc import abstractmethod, ABC, ABCMeta
from typing import Type

from PyQt5.QtWidgets import (QApplication, QMessageBox, QHBoxLayout, QPushButton,
                             QWidget, QVBoxLayout, QLineEdit, QTextEdit, QLabel, QSlider)


class iterator(ABC):
    def __init__(self, position: int = 0):
        self.position = position

    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def get_current(self):
        pass

    def next(self):
        self.position += 1

    def show(self):
        while self.has_next():
            print(self.get_current(), end=", ")
            self.next()
        print()


class MyStringIterator(iterator):
    def __init__(self, value: str):
        iterator.__init__(self)
        self.__value: str = value

    def has_next(self) -> bool:
        return self.position < len(self.__value)

    def get_current(self) -> str:
        return self.__value[self.position]


class MyString(str):

    def __new__(cls, value: str):
        return super().__new__(cls, value)

    def get_iterator(self):
        return MyStringIterator(self)


class MyVectorIterator(iterator):
    def __init__(self, elements: list):
        iterator.__init__(self)
        self.elements = elements

    def has_next(self) -> bool:
        return self.position < len(self.elements)

    def get_current(self) -> str:
        return self.elements[self.position]


class MyVector(list):

    def __new__(cls, elements: str):
        return super().__new__(cls, elements)

    def get_iterator(self):
        return MyVectorIterator(self)


if __name__ == '__main__':
    MyString("Hello, World !").get_iterator().show()
    MyVector("Hello, World !").get_iterator().show()
