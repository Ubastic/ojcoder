class Tweet(object):

    def __init__(self, time, tweetId):
        self.timestamp = time
        self.tweetId = tweetId
        self.prev = None

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = 0
        self.users = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self._add_user(userId)
        last_tweet = self.users[userId][0]
        new_tweet = Tweet(-self.timestamp, tweetId)
        new_tweet.prev = last_tweet
        self.users[userId][0] = new_tweet
        self.timestamp += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        self._add_user(userId)
        recents = []
        heap = []
        for user in self.users[userId][1]:
            if self.users[user][0]:
                t = self.users[user][0]
                heapq.heappush(heap, (t.timestamp, t))
        while heap and len(recents) < 10:
            time_stamp, tweet = heapq.heappop(heap)
            if tweet.prev:
                heapq.heappush(heap, (tweet.prev.timestamp, tweet.prev))
            recents.append(tweet.tweetId)
        return recents

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self._add_user(followerId)
        self._add_user(followeeId)
        self.users[followerId][1].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self._add_user(followerId)
        if followerId == followeeId:    return
        if followeeId in self.users[followerId][1]:
            self.users[followerId][1].remove(followeeId)
        
    def _add_user(self, userId):
        if userId not in self.users:
            self.users[userId] = [None, set([userId])]

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)