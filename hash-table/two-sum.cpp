#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int> nums, int target) {
    std::unordered_map<int, int> indices;
    std::vector<int> out;
    int len = nums.size();
    for (int i = 0; i < len; ++i) {
        int compliment = target - nums[i];
        if (indices.find(compliment) != indices.end()) {
            out.push_back(indices[compliment]);
            out.push_back(i);
        } else
            indices[nums[i]] = i;
    }
    return out;
}

void print(std::vector<int> v) {
    for (int i: v)
        std::cout << i << " ";
    std::cout << "\n";
}

int main(int argc, char *argv[]) {
    std::vector<int> test = {2,3,5,7,11,15};
    print(twoSum(test, 14)); // answer should be indices [1, 4]
}