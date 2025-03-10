class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = [0] * (len(gain)+1)

        for i in range(1, len(altitude)):
            altitude[i] = altitude[i-1] + gain[i-1]

        return max(altitude)
