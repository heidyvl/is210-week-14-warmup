#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


import pet


class Dog(pet.Pet):
    """Class Docstring"""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor"""

        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
