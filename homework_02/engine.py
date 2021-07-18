"""
create dataclass `Engine`
"""
from dataclasses import dataclass


class Engine(dataclass):
    volume: int
    pistons: int

