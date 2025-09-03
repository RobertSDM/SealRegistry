from enum import Enum

from attr import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Cordinate:
    start: Point
    end: Point


@dataclass
class ErrorSeal:
    seal: int
    reason: str
