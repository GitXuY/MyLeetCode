class Solution(object):
    def singleNumber(self, nums):
        repository = {};
        for x in nums:
            if repository.has_key(x):
                repository.pop(x)
            else:
                repository[x] = 1;
        list_result = repository.keys();
        return list_result[0]
                    
