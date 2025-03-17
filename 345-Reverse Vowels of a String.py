class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v_in_s = [char for char in s if char in vowels]

        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = v_in_s[-1]
                v_in_s.pop()

        return ''.join(s_list)
