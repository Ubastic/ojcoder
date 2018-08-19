class Node {
    int key, value;
    Node prev, next;
    public Node(int k, int v) {
        key = k;
        value = v;
    }
}

public class LRUCache {
    
    int capacity;
    Node head = null;
    Node tail = null;
    HashMap<Integer, Node> map = null;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
        head.prev = null;
        tail.next = null;
        map = new HashMap<>();
        
    }
    
    public int get(int key) {
        if (map.containsKey(key)) {
            Node n = map.get(key);
            remove(n);
            add(n);
            return n.value;
        }
        return -1;
    }
    
    public void set(int key, int value) {
        if (map.containsKey(key))
            remove(map.get(key));
        Node n = new Node(key, value);
        add(n);
        map.put(key, n);
        if (map.size() > capacity) {
            Node old = head.next;
            remove(old);
            map.remove(old.key);
        }
    }
    
    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    private void add(Node node) {
        node.prev = tail.prev;
        node.prev.next = node;
        node.next = tail;
        tail.prev = node;
    }
}