#tags : array hashtable
#哈希表的作用： 用作一个快速查找表
# 算法思想:
# 遍历给定的数组
# 建立一个哈希表用于 保存 数值 到下标的映射
# 一旦发现 target - nums[i] 的值 为 哈希表中的键，返回。因为求和等式已经满足。
class Solution(object):
    def twoSum(self, nums, target):
        #hash用于建立数值到下标的映射,
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            else:
                hash[nums[i]] = i
        return [-1, -1]
