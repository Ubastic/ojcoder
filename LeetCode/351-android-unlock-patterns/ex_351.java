public class Solution {
    public int numberOfPatterns(int m, int n) {
        boolean[] visited = new boolean[] {false, false, false, false, false, false, false, false, false};
        int count = 0;
        Map<String, Integer> map = new HashMap<String, Integer>();
        map.put("13", 1);
        map.put("46", 4);
        map.put("79", 7);
        map.put("17", 3);
        map.put("28", 4);
        map.put("39", 5);
        map.put("19", 4);
        map.put("37", 4);
        map.put("31", 1);
        map.put("64", 4);
        map.put("97", 7);
        map.put("71", 3);
        map.put("82", 4);
        map.put("93", 5);
        map.put("91", 4);
        map.put("73", 4);
        for (int i = m; i < n + 1 ; ++i){
            for (int j = 0; j < 9; ++j){
                visited[j] = true;
                count += dfs(visited, i-1, j+1, map);
                visited[j] = false;
            }
        }
        return count;
    }

    private int dfs(boolean[] visited, int n, int curr, Map<String, Integer> map) {
        if (n == 0)     return 1;
        int count = 0;
        for (int i = 0; i < 9; ++i) {
            if (!visited[i] && isValid(curr, i+1, visited, map)) {
                visited[i] = true;
                count += dfs(visited, n-1, i+1, map);
                visited[i] = false;
            }
        }
        return count;
    }

    private static boolean isValid(int curr, int next, boolean[] visited, Map<String, Integer> map) {
        String key = Integer.toString(next *10 + curr);
        return !map.containsKey(key) || visited[map.get(key)];
    }
}