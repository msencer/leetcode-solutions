/*
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
*/

class Solution {
public:
    int trailingZeroes(int n) {
        int zeroes = 0;
        int power = 1;
        while(pow(5,power) <= n){
            zeroes += n / pow(5,power);
            power++;
        }
        return zeroes;
    }
};