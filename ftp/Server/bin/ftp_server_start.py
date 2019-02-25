# -*- coding: utf-8 -*-
# Date: 2019/1/29

import os
import sys
import socketserver
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)



if __name__ == '__main__':
    from core import core
    from conf import settings
    socketserver_obj = socketserver.ThreadingTCPServer((settings.IP, settings.PORT), core.Ftp_server)
    socketserver_obj.serve_forever()
