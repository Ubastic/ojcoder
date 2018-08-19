public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers that's previous permuation
     */
    private void swap(ArrayList<Integer> nums, int x, int y){
        int tmp = nums.get(x);
        nums.set(x, nums.get(y));
        nums.set(y, tmp);
    } 
     
    public ArrayList<Integer> previousPermuation(ArrayList<Integer> nums) {
		// write your code
		int index = nums.size() - 1;
		
		while(index > 0 && nums.get(index) >= nums.get(index - 1)) index--;
		
		if(index == 0) for(int i = nums.size()/2 - 1; i >= 0; i--) swap(nums, i, nums.size() - 1 - i);
		
		else{
		    int start = index, end = nums.size() - 1;
		    
		    while(start <= end){
		        int mid = (start + end) / 2;
		        
		        if(nums.get(mid) >= nums.get(index - 1)) end = mid - 1;
		        
		        else start = mid + 1;
		    }
		    
		    swap(nums, end, index - 1);
		    
		    for(int i = (nums.size() - 1 + index) / 2; i >= index; i--) swap(nums, i, nums.size() - 1 + index - i);
		}
		
		return nums;
    }
}
