#include <iostream>
#include <string>
#include <unordered_map>

int romanToInt(std::string s) {
    std::unordered_map<char, int> roman = { {'I', 1},
                                            {'V', 5},
                                            {'X', 10},
                                            {'L', 50},
                                            {'C', 100},
                                            {'D', 500},
                                            {'M', 1000} };
    int len = s.length();
    if (len == 1) return roman[s[0]];

    int ans = 0;
    for (int i = 0; i < len; ++i) {
        int curr = roman[s[i]];
        int next = roman[s[i+1]];
        if (curr >= next)
            ans += curr;
        else {
            ans += next - curr;
            ++i;
        }
    }
    return ans;
}

int main(int argc, char *argv[]) {
    std::cout << romanToInt("MCMXCIV") << std::endl;
    std::cout << romanToInt("LVIII") << std::endl;
    std::cout << romanToInt("III") << std::endl;
}