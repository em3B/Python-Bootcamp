#Assignment: accept list of nums and return True if any three consecutive numbers add up to an odd number. 

def three_odd_numbers(nums): #num is a list of nums 
    for i in range(0, len(nums)-2):
        total= nums[i]+nums[i+1]+nums[i+2]
        if total%2!=0: #test for odd results 
            return True
        
    return False #indent this way to finish testing all possible True results first 