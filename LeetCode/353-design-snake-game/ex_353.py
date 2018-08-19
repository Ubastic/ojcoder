from Queue import Queue
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.offset = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        self.width = width
        self.height = height
        
        self.queue = Queue()
        self.body = set()
        self.head = (0, 0)
        self.queue.put(self.head)
        self.body.add(self.head)
        
        self.food = food
        self.food_at = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        next_move = tuple([self.head[0] + self.offset[direction][0], self.head[1] + self.offset[direction][1]])
        if next_move[0] < 0 or next_move[0] >= self.height or next_move[1] < 0 or next_move[1] >= self.width:
            return -1
        if self.food_at == len(self.food) or next_move != tuple(self.food[self.food_at]):
            tail = self.queue.get()
            self.body.remove(tail)
        else:
            self.food_at += 1
            
        if next_move in self.body:      return -1
        self.body.add(next_move)
        self.head = next_move
        self.queue.put(next_move)   
        return self.food_at

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)