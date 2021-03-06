#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 22:50
# @Author  : Shawn
# @File    : 4MedianTwoSortedArrays.py


class Solution:

    def findMedianSortedArrays(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        # if n == 0:
        #     raise ValueError
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = int(half_len) - i
            if i < m and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left
                else:
                    if i == m:
                        min_of_right = B[j]
                    elif j == n:
                        min_of_right = A[i]
                    else:
                        min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2

