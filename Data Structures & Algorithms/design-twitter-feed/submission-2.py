class Twitter:

    def __init__(self):
        self.time = 0
        self.tm = defaultdict(list)
        self.fm = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tm[userId].append([self.time, tweetId])
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        mh = []

        self.fm[userId].add(userId)

        for followeeId in self.fm[userId]:
            if followeeId in self.tm:
                idx = len(self.tm[followeeId])-1
                cnt, twid = self.tm[followeeId][idx]
                mh.append([cnt, twid, followeeId, idx-1])
        
        heapq.heapify_max(mh)

        while mh and len(res)<10:
            cnt, twid, fid, idx = heapq.heappop_max(mh)
            res.append(twid)
            if idx >= 0:
                cnt, twid = self.tm[fid][idx]
                heapq.heappush_max(mh, [cnt, twid, fid, idx-1])

        return res
            

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fm[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.fm[followerId]:
            self.fm[followerId].remove(followeeId)
        
