public class Solution {
    public boolean validTree(int n, int[][] edges) {
        UF uf = new UF(n);
        for (int i = 0; i < edges.length; i++) {
            if (uf.connected(edges[i][0], edges[i][1]))
                return false;
            uf.union(edges[i][0], edges[i][1]);
        }
        return uf.count() == 1 ? true : false;
    }

    public class UF {
        private int[] id;
        private int[] sz;
        private int count;
        
        public UF(int N) {
            count = N;
            id = new int[N];
            sz = new int[N];
            for (int i = 0; i < N; i++) {
                id[i] = i;
                sz[i] = i;
            }
        }
        
        public int count() { return count; }
        
        public boolean connected(int p, int q) { return find(p) == find(q); }
        
        public int find(int p) {
            while (p != id[p])  p = id[p];
            return p;
        }
        
        public void union(int p, int q) {
            int i = find(p);
            int j = find(q);
            if (i == j) return;
            if (sz[i] < sz[j])  { id[i] = j; sz[j] += sz[i]; }
            else                { id[j] = i; sz[i] += sz[j]; }
            count--;
        }
    }
}