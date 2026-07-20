class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if self.tweetMap[followee]:
                idx = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][idx]
                heapq.heappush(heap, (time,tweetId, followee,idx-1))

        while heap and len(res) < 10:
            time, tweetId, followee,idx = heapq.heappop(heap)

            res.append(tweetId)

            if idx >= 0:
                time, tweetId = self.tweetMap[followee][idx]
                heapq.heappush(heap, (time,tweetId, followee,idx-1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)
        
