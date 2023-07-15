class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list1 = []
        counti = -1
        countl = 0
        # Loop to go through the first set of list 
        for i in nums:
            # print(i)
            counti = counti +1
            # print(len(nums))
            countl = 0
            for l in nums:
                # print("this is l",l)
                if counti == countl :
                    countl = countl + 1
                    # print(countl, "count")
                    continue
                
                # print(i,l)
                
                # print(countl, "count")
                
                # if countl < len(nums):
                #     countl = countl +1
                # else:
                #     countl = -1

                if i + l == target:
                    print("found")
                    # print(i, l)
                    
                    list1.append(counti)
                    list1.append(countl)
                    # print(list1)
                    return list1
                countl = countl + 1
        # embeded list, to go through all the numbers to be multiplied.