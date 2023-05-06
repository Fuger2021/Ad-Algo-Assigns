#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script was created by xyf1190201325.
"""

import sys
import argparse
from tools import v, gen_map

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', type=str, default='s_astar')
    parser.add_argument('--map', type=str, default='map_1')

    try:
        args = parser.parse_args()
        module = __import__(args.algo)
        map, x_size, y_size, start, end = gen_map(args.map)
        opt_path = module.execute(map, start, end)
        v(opt_path, x_size, y_size, 'pixel_map_' + args.map[-1] + '.png')
        print(start, end, opt_path)

    except Exception as e:
        import sys
