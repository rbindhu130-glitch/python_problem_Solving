def appear_twice(nums):
    if len(nums)==0:
        return "Invalid Input"
    else:
        count={}
        output=[]
        for i in range(0,len(nums),+1):
            if nums[i] not in count:
                count [nums[i]] =1
            else:
                count [nums[i]] = count[nums[i]] +1
        for key in count:
            if count[key] >1:
                output.append(key)
        return output
        
print(appear_twice([1,2,3,1,2,4,5,6,3]))        
