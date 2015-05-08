#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


from data import FRUIT


SHOPLIST = {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}


def get_cost_per_item(shoplist):

    """Function returns total cost per item"""
    newdict = {key: shoplist[key]*FRUIT[key] for key, value
               in shoplist.iteritems() if key in FRUIT}
    return newdict


def get_total_cost(shoplist):

    """This function returns sum of total cost per item"""
    total_cost = sum(get_cost_per_item(shoplist).values())
    return total_cost
