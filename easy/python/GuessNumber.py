'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
'''
import random

rnd = random.randint(1, 10000)


def guess(n):
    return 0 if n == rnd else -1 if n > rnd else 1


class Solution(object):
    def _guess_helper_(self, start, end):
        mid = (start + end) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == 1:
            return self._guess_helper_(mid + 1, end)
        else:
            return self._guess_helper_(start, mid - 1)

    def guessNumber(self, n):
        return self._guess_helper_(1, n)


if __name__ == "__main__":
    assert rnd == Solution().guessNumber(10000)
