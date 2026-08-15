class Twitter:
    def __init__(self):
        self.current_time = 0
        self.heap = []
        self.hashmap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # new tweet id by user id
        heapq.heappush(self.heap, (-self.current_time, [userId, tweetId]))
        self.current_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # get Max 10 most recent tweet id's
        ## where is either user or user is following
        curr_feed = []
        tmp_storage = []
        curr_cnt = 0
        is_enough = False
        while self.heap and not is_enough:
            time, user = heapq.heappop(self.heap)
            user_id, tweetId = user
            tmp_storage.append((time, [user_id, tweetId]))
            if user_id == userId or user_id in self.hashmap.get(userId, []):
                curr_feed.append((time, [user_id, tweetId]))
                curr_cnt+=1
            if  curr_cnt >= 10:
                is_enough = True

        for item in tmp_storage: heapq.heappush(self.heap, item)
        return [tweetId for time, (user_id, tweetId) in curr_feed]

    def follow(self, followerId, followeeId):
        if followerId not in self.hashmap:
            self.hashmap[followerId] = set()
        self.hashmap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.hashmap:
            self.hashmap[followerId].discard(followeeId)



  