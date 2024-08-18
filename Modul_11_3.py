#-*- coding: utf-8 -*-
import inspect
from threading import Thread
from pprint import pprint

import requests


def samp(summa=45):
    nds = summa/100*20
    return nds



class Thread_test(Thread):
    def __init__(self, name):
        super().__init__(name=name)


def introspection_info(obj):
    date = {}
    date["type"] = type(obj)
    if inspect.isfunction(obj):
        signature = inspect.signature(obj)
        date_default = {
            k: v.default
            for k, v in signature.parameters.items()
            if v.default is not inspect.Parameter.empty
        }
        date_arg = {
            k: v
            for k, v in signature.parameters.items()
            if v is not inspect.Parameter.empty
        }
    else:
        date_default = {}
        date_arg = {}
    date["modul"] = inspect.getmodule(obj)
    date_metod = {}
    date_func = {}
    date_class = {}

    # methods = inspect.getmembers(obj, lambda attr: (inspect.isfunction(attr)))
    # date['function'] = methods
    for name, data in inspect.getmembers(obj):
        if name.startswith('__'):
            continue
        if inspect.ismethod(data):
            date_metod[name] = data
        elif inspect.isfunction(data):
            date_func[name] = data
        elif inspect.isclass(data):
            date_class[name] = data
        elif inspect.ismodule(data):
            pass
        else:
            pass
            #pprint(f'Какой то не отобранный {name} : {type(data)}')
        #print('{} : {!r}'.format(name, data))

    if len(date_metod) != 0:
        date["Metod"] = date_metod
    if len(date_func) != 0:
        date["Function"] = date_func
    if len(date_class) != 0:
        date["Class"] = date_class
    if len(date_default) != 0:
        date['Default_arg'] = date_default
        date['Arguments'] = date_arg
    return date


print("Функция :\n")
dict_a = introspection_info(samp)
pprint(dict_a)
print("Библиотека :\n")
dict_b = introspection_info(requests)
pprint(dict_b)
print("Класс :\n")
class_potok = Thread_test('First')
pprint(f'{isinstance(class_potok, Thread)} - Является ли Объект экземпляром Thread')
dict_c = introspection_info(class_potok)
pprint(dict_c)
