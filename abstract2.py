# -*- coding: utf8 -*-
from abc import ABCMeta, abstractmethod


class Flow:
    def procedure_flow(self):
        pass

    def game_flow(self):
        pass

    def turn_flow(self):
        while ~TurnFlow.is_game_end():
            TurnFlow.do_turn()
            TurnFlow.display_score()

class ProcedureFlow(Flow):
    def procedure_flow(self):
        return 1


class GameFlow(Flow):
    def game_flow(self):
        return 2


class TurnFlow(Flow):
    @classmethod
    def is_game_end(cls):
        pass

    @classmethod
    def do_turn(cls):
        pass

    @classmethod
    def display_score(cls):
        pass


aaa = Flow()
print aaa.turn_flow()
