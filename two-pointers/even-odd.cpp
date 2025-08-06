#include <iostream>

// This function rearranges the elements of an integer array so that all even numbers come before all odd numbers.

int * evenOdd(int *arr, int len) {
    int left = 0;
    int right = len - 1;
    while (left < right) {
        while (left < right && arr[left] % 2 == 0) // move left ptr to first odd
            ++left;
        while (left < right && arr[right] % 2 == 1) // move right ptr to first even
            --right;
        if (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
        }
    }
    return arr;
}

int main(int argc, char *argv[]) {
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    int len = 10;
    int * result = evenOdd(arr, len);
    for (int i = 0; i < len; ++i) {
        std::cout << result[i] << "\n";
    }
}