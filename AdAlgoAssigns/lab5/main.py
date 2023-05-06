#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script was created by xyf1190201325.
"""
import copy

import matplotlib.pyplot as plt
import argparse
from dataset import gen_data

# N = 100
# # no_repeat = random.sample(range(0, N), N)
# no_repeat = gen_data(N, 1)
# print(no_repeat)
# ad_quick_sort(no_repeat)
# print(no_repeat)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', type=str, default='rand_quick_sort')
    parser.add_argument('--perf', type=bool, default=False)

    N = 20000

    try:
        args = parser.parse_args()

        if not args.perf:
            module = __import__(args.algo)
            dataset = gen_data(N)
            print(dataset)
            time = module.execute(dataset)
            print(dataset)
            print(time)

            # fig, ax = plt.subplots()
            # px = [p[0] for p in points]
            # py = [p[1] for p in points]
            # ax.scatter(px, py, color='green', s=15)
            #
            # chx = [c[0] for c in chull]
            # chy = [c[1] for c in chull]
            # ax.scatter(chx, chy, color='red', s=15, marker="o")
            # ax.text(-3, 107, "time: " + str(time) + "s\nalgo: " + str('dc_convexhull') + "\nsize: " + str(args.size),
            #         fontsize=10)
            #
            # plt.show()
        else:
            import rand_quick_sort
            import ad_quick_sort
            import lib_quick_sort

            r_lst, m_lst, l_lst = [], [], []

            for i in range(10):
                randsort_data = gen_data(N, i)
                # print(randsort_data)
                mediansort_data = copy.deepcopy(randsort_data)
                libsort_data = copy.deepcopy(randsort_data)

                # print('qqq')
                r_time = rand_quick_sort.execute(randsort_data)
                # print(r_time)
                r_lst.append(r_time)
                # print('www')
                m_lst.append(ad_quick_sort.execute(mediansort_data))
                # print('eee')
                l_lst.append(lib_quick_sort.execute(libsort_data))
                # print('rrr')

            # # print(time_lst)
            # fig, ax = plt.subplots()
            # ax.set_xlabel('Size')
            # ax.set_ylabel('Time(s)')
            # ax.plot(size_lst, time_lst, '-o')
            # ax.text(0, 0, "algo: " + str(args.algo), fontsize=10)
            #
            # plt.show()
            size = [i for i in range(10)]
            plt.subplot(131)
            plt.title("rand_Qsort")
            plt.xlim(xmax=max(size) * 1.1, xmin=0)
            plt.ylim(ymax=max(r_lst) * 1.1, ymin=0)
            plt.xlabel("i%")
            plt.ylabel("time(s)")
            plt.plot(size, r_lst, color="blue", marker="o")

            plt.subplot(132)
            plt.title("median_Qsort")
            plt.xlim(xmax=max(size) * 1.1, xmin=0)
            plt.ylim(ymax=max(m_lst) * 1.1, ymin=0)
            plt.xlabel("i%")
            plt.ylabel("time(s)")
            plt.plot(size, m_lst, color="blue", marker="o")

            plt.subplot(133)
            plt.title("lib_Asort")
            plt.xlim(xmax=max(size) * 1.1, xmin=0)
            plt.ylim(ymax=max(l_lst) * 1.1, ymin=0)
            plt.xlabel("i%")
            plt.ylabel("time(s)")
            plt.plot(size, l_lst, color="blue", marker="o")

            plt.legend()
            plt.show()

    except Exception as e:
        import sys

        e.with_traceback(sys.exc_info()[2])
