# contains duplicates:
class Solution:
    def containsDuplicate(self, nums:
        # check if the array contains duplicates
        # if any value appears at least twice in the array
            # return true
        # otherwise return 
        '''
        # first time running at 24 ms
        for n in nums:
            if nums.count(n) > 1:
                return True
            else:
                return False
        
        # second time running at 36 ms
        # A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. 
        setOfElem = set()
        for n in nums:
            if n in setOfElem:
                return True
            else:
                setOfElem.add(n)
        return False
        '''
        # third time: 
        '''
        1. Add the contents of list in a set.
        As set contains only unique elements, so no duplicates will be added to the set.
        Compare the size of set and list.
        If size of list & set is equal then it means no duplicates in list.
        If size of list & set are different then it means yes, there are duplicates in list.
        '''

        if len(nums) == len(set(nums)):
            return False
        else:
            return True


        