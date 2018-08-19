#include <iostream>
#include <map>

using std::map;

struct Node {
    int key, value;
    Node *prev, *next;
    Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) { }
};


class LRUCache{
public:
    LRUCache(int cap) : capacity(cap) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (node_dict.find(key) != node_dict.end()) {
            Node *n = node_dict[key];
            remove(n);
            add(n);
            return n->value;
        }
        return -1;
    }
    
    void set(int key, int value) {
        if (node_dict.find(key) != node_dict.end())
            remove(node_dict[key]);
        Node *n = new Node(key, value);
        add(n);
        node_dict[key] = n;
        if (node_dict.size() > capacity) {
            Node *old = head->next;
            remove(old);
            node_dict.erase(old->key);
        }
    }

private:
    int capacity;
    map<int, Node*> node_dict;
    Node *head = nullptr, *tail = nullptr;

    void add(Node *node) {
        node->prev = tail->prev;
        tail->prev->next = node;
        node->next = tail;
        tail->prev = node;
    }

    void remove(Node *node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
        // possible memory leak?
    }
};

int main() {
    // 1,[set(2,1),get(2),set(3,2),get(2),get(3)]
    LRUCache cache(1);
    cache.set(2, 1);
    std::cout << cache.get(2) << std::endl;
    cache.set(3, 2);
    std::cout << cache.get(2) << std::endl;
    std::cout << cache.get(3) << std::endl;
    return 0;
}