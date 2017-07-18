class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hash;
        int length = nums.size();
        for (int i=0; i < length; ++i){
            if (hash.find(target-nums[i]) != hash.end()){
                vector<int> a = {hash[target-nums[i]], i};
                return a;
            }
            else
                hash[nums[i]] = i;
        }
    }
};