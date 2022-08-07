class Solution {
public:
    int gcd(int a,int b) {
        if (b == 0) return a;
        return gcd(b , a%b);
    }
    int minOperations(vector<int>& nums, vector<int>& numsDivide) {
        int gval = numsDivide[0];
        for(int i = 1 ; i < numsDivide.size() ; i++) {
            gval = gcd(gval,numsDivide[i]);
        }
        sort(nums.begin() , nums.end());
        for(int i = 0 ; i < nums.size(); i++) {
            if(nums[i]>gval) return -1;
            if (gval%nums[i]==0){
                return i;
            }
        }
        return -1 ;
        
    }
};