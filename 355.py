class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.users:
            self.users[userId] = {}
            self.users[userId]['tweet'] = []
            self.users[userId]['follow'] = set()
        self.users[userId]['tweet'].append([tweetId,self.time])
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId in self.users:
            temp = []
            for t in self.users[userId]['tweet']:
                temp.append(t)
            for user in self.users[userId]['follow']:
                if user in self.users[userId]['follow'] and user in self.users:
                    temp += self.users[user]['tweet']
            temp.sort(key=lambda x:-x[1])
            result = []
            for i in range(min(10,len(temp))):
                result.append(temp[i][0])
            return result
        else:
            return []
        
    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.users:
            self.users[followerId] = {}
            self.users[followerId]['tweet'] = []
            self.users[followerId]['follow'] = set()
        if followeeId != followerId:
            self.users[followerId]['follow'].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId != followerId:
            if followerId in self.users:
                if followeeId in self.users[followerId]['follow']:
                    self.users[followerId]['follow'].remove(followeeId)
