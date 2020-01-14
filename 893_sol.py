#!/usr/bin/env python

class Solution(object):
    def numSpecialEquivGroups(self, A):
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            print tuple(ans)
            return tuple(ans)

        print {count(word) for word in A}

if __name__ == '__main__':
    A = ['abcd', 'cdab', 'cbad', 'xyzz', 'zzxy', 'zzyx']
    sol = Solution()
    print sol.numSpecialEquivGroups(A)
