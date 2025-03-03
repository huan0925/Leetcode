class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len_word1 = len(word1)
        len_word2 = len(word2)
        merge_str = ''

        if len_word1 >= len_word2:
            max_len = len_word1
        else:
            max_len = len_word2

        for i in range(0, max_len):
            if len_word1 != 0 and len_word2 != 0:
                merge_str += word1[i] + word2[i]
                len_word1 -= 1
                len_word2 -= 1
            elif len_word1 == 0 and len_word2 != 0:
                merge_str += word2[i:]
                break
            elif len_word2 == 0 and len_word1 != 0:
                merge_str += word1[i:]
                break

        return merge_str
