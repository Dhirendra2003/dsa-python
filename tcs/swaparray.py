def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for x in range(0,k):
        temp = nums[-1]
        for (i=0;i<len(nums),i++):
            nums[i]=nums[i-1]
            if(i==0):

            print(nums)
        nums[0]=temp
        print (temp)
        print (nums)

rotate(None,[1,2,3,4,5,6,7],2)