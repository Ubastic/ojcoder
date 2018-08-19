class Queue {
public:
    stack<int> stack1;
    stack<int> stack2;

    Queue() {
        // do intialization if necessary
        //stack1 for enqueue
        //stack2 for dequeue
    }

    void push(int element) {
        // write your code here
        while(!stack2.empty()){
            stack1.push(stack2.top());
            stack2.pop();
        }
        stack1.push(element);
    }
    
    int pop() {
        // write your code here
        int res = top();
        if(!stack2.empty()){
            stack2.pop();
        }
        return res;
    }

    int top() {
        // write your code here
        while(!stack1.empty()){
            stack2.push(stack1.top());
            stack1.pop();
        }
        if(!stack2.empty()){
            return stack2.top();
        }else{
            return -1;
        }
    }
};

