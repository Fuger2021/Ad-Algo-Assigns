#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script was created by xyf1190201325.
"""

import matplotlib.pyplot as plt
import argparse
from pointset import generating

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', type=int, default=1000)
    parser.add_argument('--algo', type=str, default='enum_convexhull')
    parser.add_argument('--perf', type=bool, default=False)

    try:
        args = parser.parse_args()

        if not args.perf:
            points = generating(args.size)
            module = __import__(args.algo)
            time, chull = module.execute(points)

            fig, ax = plt.subplots()
            px = [p[0] for p in points]
            py = [p[1] for p in points]
            ax.scatter(px, py, color='green', s=15)

            chx = [c[0] for c in chull]
            chy = [c[1] for c in chull]
            ax.scatter(chx, chy, color='red', s=15, marker="o")
            ax.text(-3, 107, "time: " + str(time) + "s\nalgo: " + str('dc_convexhull') + "\nsize: " + str(args.size),
                    fontsize=10)

            plt.show()
        else:
            module = __import__(args.algo)
            time_lst = []
            size_lst = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
            for size in size_lst:
                points = generating(size)
                time, chull = module.execute(points)
                time_lst.append(time)

            # print(time_lst)
            fig, ax = plt.subplots()
            ax.set_xlabel('Size')
            ax.set_ylabel('Time(s)')
            ax.plot(size_lst, time_lst, '-o')
            ax.text(0, 0, "algo: " + str(args.algo), fontsize=10)

            plt.show()

    except Exception as e:
        import sys

        e.with_traceback(sys.exc_info()[2])
