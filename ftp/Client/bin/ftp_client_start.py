# -*- coding: utf-8 -*-
# Date: 2019/1/29


import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)

if __name__ == '__main__':
    from core import core
    ftp_client_obj = core.Ftp_client()
    ftp_client_obj.initialize()