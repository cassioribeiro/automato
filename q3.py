#!/usr/bin/env python
# -*- coding: utf-8 -*-


from q4 import Q4
from q6 import Q6
import re

class Q3:

    def __init__(self, transition):
        self._final_state = True
        self._letter_list = []
        self._current_letter = 'Ɛ'
        self._word = None
        self._transition = transition
        self._current_state = 'Q3'

    @property
    def final_state(self):
        return self._final_state

    def start(self):

        if self._transition.list_letters.__len__() != 0:
            self._transition.list_letters.pop(0)

        if self._transition.list_letters.__len__() != 0:
            self._current_letter = self._transition.current_letter

        return self.next_transition()

    def next_transition(self):

        self._transition.current_transition(self._current_letter,
                                            self._current_state)

        self._transition.final_state = self._final_state

        if self._current_letter == '.':
            return Q4(self._transition).start()
        elif re.findall(r'[0-9]', self._current_letter) != []:
            return Q3(self._transition).start()
        elif self._current_letter is 'E':
            return Q6(self._transition).start()
        elif self._transition.list_letters.__len__().__eq__(0):
            self._transition.consumed_word = True
            return True
        elif self._current_letter is None:
            self._transition.consumed_word = True
            return True
        else:
            self._transition.consumed_word = True

            if self._transition.list_letters.__len__() != 0:
                self._transition.consumed_word = False
            return True

