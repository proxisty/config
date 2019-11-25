#!/usr/bin/env python

import subprocess
import optparse


def get_local_ip():
    parser = optparse.OptionParser()
    parser.add_option('-ip', '--ipadress', dest='ipadress', help='Show local address ip')
    ()