class Solution(object):
    def countOcc(self,int, array):
        count=0
        for i in array:
            if int==i:
                count+=1
        return  count
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copynums=nums
        newarr = []
        count = 0
        for i in range(0,len(nums)):
            if self.countOcc(copynums[i],newarr)<2 :
                print(copynums[i])
                newarr.append(copynums[i])
                count += 1
                nums[count-1] = newarr[count-1]

        # print (count)


        print (newarr)
        print (nums)
        return count
s=Solution()
#s.removeElement([0,1,2,2,3,0,4,2],2)
#s.removeElement([4,5],4)
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
