#include <iostream>
#include <vector>

int removeDuplicates(std::vector<int> &nums) {
    int len = nums.size();
    int k = 1;
    for (int i = 1; i < len; ++i) {
        if (nums[i] != nums[i-1])
            nums[k++] = nums[i];
    }
    return k;
}

int main(int argc, char *argv[]) {
    std::vector<int> test = {0,0,0,0,1,1,1,1,2,2,2,3,3,3};
    std::cout << removeDuplicates(test) << "\n";
}