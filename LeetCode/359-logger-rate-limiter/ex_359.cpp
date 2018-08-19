class Logger {
public:
    /** Initialize your data structure here. */
    Logger() : lastPrint() { }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        if (lastPrint.find(message) == lastPrint.end() || timestamp - lastPrint[message] > 9) {
            lastPrint[message] = timestamp;
            return true;
        }
        return false;
    }
private:
    map<string, int> lastPrint;
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * bool param_1 = obj.shouldPrintMessage(timestamp,message);
 */