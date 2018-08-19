public class Solution {
    /**
     * @param n an integer
     * @return a list of Map.Entry<sum, probability>
     */
    private TreeMap<Integer, Double> helper(TreeMap<Integer, Double> M){
        TreeMap<Integer, Double> newM = new TreeMap<>();
        double p = 1d/6;
        
        for(int i = 1; i <= 6; i++)
            for(int num : M.keySet()){
                int key = num + i;
                
                if(newM.containsKey(key)) newM.put(key, newM.get(key) + M.get(num)*p);
                
                else newM.put(key, M.get(num)*(1d/6));
            }
        
        return newM;
    }
     
    public List<Map.Entry<Integer, Double>> dicesSum(int n) {
        // Write your code here
        // Ps. new AbstractMap.SimpleEntry<Integer, Double>(sum, pro)
        // to create the pair
        TreeMap<Integer, Double> M = new TreeMap<>();
        double p = 1d/6;
        
        for(int i = 1; i <= 6; i++) M.put(i, p);
        
        for(int i = 2; i <= n; i++) M = helper(M);
        
        List<Map.Entry<Integer, Double>> ans = new ArrayList<>();
        
        for(Map.Entry<Integer, Double> e : M.entrySet()) ans.add(e);
        
        return ans;
    }
}
