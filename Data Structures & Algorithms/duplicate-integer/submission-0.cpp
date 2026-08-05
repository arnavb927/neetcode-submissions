class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        size_t length = nums.size();

        for (int i = 0; i < length; i++) {
            int num1 = nums[i];
            for (int j = i+1; j < length; j++) {
                if (num1 == nums[j]) return true;
            }
        }
        return false;
    }
};