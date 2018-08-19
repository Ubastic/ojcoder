class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: The majority number occurs more than 1/3.
     */
    int majorityNumber(vector<int> nums) {
        // write your code here
        int a = 0, b = 0;
        int cnta = 0, cntb = 0;
        for(auto e : nums){
            if(cnta ==0 && cntb ==0){
                cnta = 1;
                a = e;
                continue;
            }
            
            if(cnta==0 && b!=e){
                cnta = 1;
                a = e;
                continue;
            }
            
            if(cntb==0 && a!=e){
                cntb = 1;
                b = e;
                continue;
            }
            
            if(e == a){
                cnta++;
            }else if(e == b){
                cntb++;
            }else{
                cnta--;
                cntb--;
            }
        }
        
        int sa=0, sb=0;
        for(auto e : nums){
            if(cnta>0 && a ==e){
                sa++;
            }
            if(cntb>0 && b ==e){
                sb++;
            }
        }
        return sa>sb?a:b;
    }
};
