#
#

from random import randint

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums
        self._shuffle_nums = [num for num in nums]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._nums        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self._shuffle_nums)):
            rand_int = randint(0, len(self._shuffle_nums)-1)
            self._shuffle_nums[i], self._shuffle_nums[rand_int] = self._shuffle_nums[rand_int], self._shuffle_nums[i]

        return self._shuffle_nums


from random import shuffle

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums
        self._shuffle_nums = [num for num in nums]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._nums        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffle(self._shuffle_nums)
        return self._shuffle_nums

