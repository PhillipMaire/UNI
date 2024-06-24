

# Standard libraries
import copy
import os
import pickle
import warnings
from datetime import datetime
import shutil

# Data handling
import numpy as np
import pandas as pd


import os



def get_class_info(c, sort_by_type=True, include_underscore_vars=False, return_name_and_type=False, end_prev_len=40):
    def get_len_or_shape(x_in):
        which_one = None
        try:
            len_or_shape_out = str(len(x_in))
            which_one = 'length'
            if type(x_in).__module__ == np.__name__:
                len_or_shape_out = str(x_in.shape)
                which_one = 'shape '
        except:
            if which_one is None:
                len_or_shape_out = 'None'
                which_one = 'None  '
        return len_or_shape_out, which_one

    names = []
    len_or_shape = []
    len_or_shape_which_one = []
    type_to_print = []

    for k in dir(c):
        if include_underscore_vars is False and k[0] != '_':

            tmp1 = str(type(eval('c.' + k)))
            type_to_print.append(tmp1.split("""'""")[-2])
            names.append(k)
            a, b = get_len_or_shape(eval('c.' + names[-1]))
            len_or_shape.append(a)
            len_or_shape_which_one.append(b)
        elif include_underscore_vars:
            tmp1 = str(type(eval('c.' + k)))
            type_to_print.append(tmp1.split("""'""")[-2])
            names.append(k)
            a, b = get_len_or_shape(eval('c.' + names[-1]))
            len_or_shape.append(a)
            len_or_shape_which_one.append(b)
    len_space = ' ' * max(len(k) for k in names)
    len_space_type = ' ' * max(len(k) for k in type_to_print)
    len_space_shape = ' ' * max(len(k) for k in len_or_shape)
    if sort_by_type:
        ind_array = np.argsort(type_to_print)
    else:
        ind_array = np.argsort(names)

    for i in ind_array:
        k1 = names[i]
        k2 = type_to_print[i]
        k5 = len_or_shape[i]
        x = eval('c.' + names[i])
        k3 = str(x)
        k1 = (k1 + len_space)[:len(len_space)]
        k2 = (k2 + len_space_type)[:len(len_space_type)]
        k5 = (k5 + len_space_shape)[:len(len_space_shape)]
        if len(k3) > end_prev_len:
            k3 = '...' + k3[-end_prev_len:]
        else:
            k3 = '> ' + k3[-end_prev_len:]
        print(k1 + ' type->   ' + k2 + '  ' + len_or_shape_which_one[i] + '->   ' + k5 + '  ' + k3)
    if return_name_and_type:
        return names, type_to_print


def get_dict_info(c, sort_by_type=True, include_underscore_vars=False, return_name_and_type=False, end_prev_len=30):
    names = []
    type_to_print = []
    for k in c.keys():
        if include_underscore_vars is False and str(k)[0] != '_':
            tmp1 = str(type(c[k]))
            type_to_print.append(tmp1.split("""'""")[-2])
            names.append(str(k))
        elif include_underscore_vars:
            tmp1 = str(type(c[k]))
            type_to_print.append(tmp1.split("""'""")[-2])
            names.append(str(k))
    len_space = ' ' * max(len(k) for k in names)
    len_space_type = ' ' * max(len(k) for k in type_to_print)
    if sort_by_type:
        ind_array = np.argsort(type_to_print)
    else:
        ind_array = np.argsort(names)

    for i in ind_array:
        k1 = names[i]
        k2 = type_to_print[i]

        if names[i] not in list(c.keys()):
          names[i] = eval(names[i])
        try:
            k3 = str(c[names[i]])
        except:
            k3 = str(c[float(names[i])])


        k1 = (k1 + len_space)[:len(len_space)]
        k2 = (k2 + len_space_type)[:len(len_space_type)]

        if len(k3) > end_prev_len:
            k3 = '...' + k3[-end_prev_len:]
        else:
            k3 = '> ' + k3[-end_prev_len:]

        if 'numpy.ndarray' in k2:
            k4 = str(c[names[i]].shape)
            k4_str = '   shape-> '
        else:
            try:
                k4 = str(len(c[names[i]]))
                k4_str = '   len-> '
            except:
                k4_str = '   None->'
                k4 = 'None'

        print(k1 + ' type->   ' + k2 + k4_str + k4 + '  ' + k3)
    if return_name_and_type:
        return names, type_to_print

def get_class_info2(c, sort_by=None, include_underscore_vars=False, return_name_and_type=False, end_prev_len=30):
    def get_len_or_shape(x_in):
        which_one = None
        try:
            len_or_shape_out = str(len(x_in))
            which_one = 'length'
            if type(x_in).__module__ == np.__name__:
                len_or_shape_out = str(x_in.shape)
                which_one = 'shape '
        except:
            if which_one is None:
                len_or_shape_out = 'None'
                which_one = 'None  '
        return len_or_shape_out, which_one

    names = []
    len_or_shape = []
    len_or_shape_which_one = []
    type_to_print = []

    for k in dir(c):
        if include_underscore_vars is False and k[0] != '_':

            tmp1 = str(type(eval('c.' + k)))
            type_to_print.append(tmp1.split("""'""")[-2])
            names.append(k)
            a, b = get_len_or_shape(eval('c.' + names[-1]))
            len_or_shape.append(a)
            len_or_shape_which_one.append(b)
        elif include_underscore_vars:
            tmp1 = str(type(eval('c.' + k)))
            type_to_print.append(tmp1.split("""'""")[-2])
            names.append(k)
            a, b = get_len_or_shape(eval('c.' + names[-1]))
            len_or_shape.append(a)
            len_or_shape_which_one.append(b)
    len_space = ' ' * max(len(k) for k in names)
    len_space_type = ' ' * max(len(k) for k in type_to_print)
    len_space_shape = ' ' * max(len(k) for k in len_or_shape)
    if sort_by is None:
        ind_array = np.arange(len(names))
    elif 'type' in sort_by.lower():
        ind_array = np.argsort(type_to_print)
    elif 'len' in sort_by.lower() or 'shape' in sort_by.lower():
        np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
        tmp1 = np.asarray([eval(k) for k in len_or_shape])
        tmp1[tmp1 == None] = np.nan
        tmp1 = [np.max(iii) for iii in tmp1]
        ind_array = np.argsort(tmp1)
    elif 'name' in sort_by.lower():
        ind_array = np.argsort(names)
    else:
        ind_array = np.arange(len(names))

    for i in ind_array:
        k1 = names[i]
        k2 = type_to_print[i]
        k5 = len_or_shape[i]
        x = eval('c.' + names[i])
        k3 = str(x)
        k1 = (k1 + len_space)[:len(len_space)]
        k2 = (k2 + len_space_type)[:len(len_space_type)]
        k5 = (k5 + len_space_shape)[:len(len_space_shape)]
        if len(k3) > end_prev_len:
            k3 = '...' + k3[-end_prev_len:]
        else:
            k3 = '> ' + k3[-end_prev_len:]
        print(k1 + ' type->   ' + k2 + '  ' + len_or_shape_which_one[i] + '->   ' + k5 + '  ' + k3)
    if return_name_and_type:
        return names, type_to_print




def info(x):
    if isinstance(x, dict):
        print('type is dict')
        get_dict_info(x)
    elif isinstance(x, list):
        try:
            x = copy.deepcopy(np.asarray(x))
            print('type is list, converting a copy to numpy array to print this info')
            np_stats(x)
        except:
            print(
                "type is a list that can't be converted to a numpy array for printing info or maybe data format is not compatible")

    elif type(x).__module__ == np.__name__:
        print('type is np array')
        np_stats(x)
    else:
        try:
            print('type is ' + str(type(x)) + ' will try printing using "get_class_info2" ')
            get_class_info2(x)
        except:
            print('cant find out what to do with input of type')
            print(type(x))

