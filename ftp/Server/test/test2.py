# -*- coding: utf-8 -*-
# Date: 2019/1/30

import pickle


class A: pass
a = A()


with open('aaaa', 'wb') as f:
    pickle.dump(a, f, protocol=2)