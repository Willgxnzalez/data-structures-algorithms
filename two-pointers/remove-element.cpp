#include <vector>
#include <iostream>

int removeElement(std::vector<int> &nums, int val) {
    int len = nums.size();
    int k = 0;
    for (int i = 0; i < len; ++i) {
        if (nums[i] != val)
            nums[k++] = nums[i];
    }
    return k;
}

int main(int argc, char * argv[]) {
    std::vector<int> test = {0,1,2,4,6,4,3,4,5,4,3,2};
    std::cout << removeElement(test, 4) << "\n";
}