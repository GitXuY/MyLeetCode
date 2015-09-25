class Solution(object):
    def singleNumber(self, nums):
        repository = {};
        for x in nums:
            if repository.has_key(x):
                repository[x] += 1;
            else:
                repository[x] = 1;
        result = [];
        for x in repository.keys():
            if repository[x] == 1:
                result.append(x);
        return x;
