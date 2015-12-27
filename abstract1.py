# -*- coding: utf8 -*-
from abc import ABCMeta, abstractmethod


class Flow:
    __metaclass__ = ABCMeta

    @abstractmethod
    def procedure_flow(self):
        pass

    @abstractmethod
    def game_flow(self):
        pass

    @abstractmethod
    def turn_flow(self):
        """
        while is_game_end() is not True:
            do_turn()
            display_score()
        """


class ProcedureFlow(Flow):
    def procedure_flow(self):
        return 1


class GameFlow(Flow):
    def game_flow(self):
        return 2


class TurnFlow(Flow):
    def turn_flow(self):
        while self.is_game_end() is not True:
            self.do_turn()
            self.display_score()

    def is_game_end(self):
        return True

    def do_turn(self):
        pass

    def display_score(self):
        pass


class RealFlow(ProcedureFlow, GameFlow, TurnFlow):
    def __init__(self):
        pass


aaa = RealFlow()
print aaa.turn_flow()

