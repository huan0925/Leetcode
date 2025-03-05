# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s_pivot = 1
        e_pivot = n
        num = (s_pivot + e_pivot) // 2
        result = guess(num)

        if guess(s_pivot) == 0:
            return s_pivot
        elif guess(e_pivot) == 0:
            return e_pivot
        else:
            while(result != 0):
                if result == -1:
                    e_pivot = num
                    num = (s_pivot + e_pivot) // 2
                    result = guess(num)
                elif result == 1:
                    s_pivot = num
                    num = (s_pivot + e_pivot) // 2
                    result = guess(num)

            return num
        
