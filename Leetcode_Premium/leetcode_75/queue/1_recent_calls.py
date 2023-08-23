"""

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
"""

from collections import deque


class RecentCounter:
    def __init__(self):
        self.timers = deque()

    def ping(self, t: int) -> int:
        self.timers.append(t)
        while self.timers[0] < t - 3000:
            self.timers.popleft()

        return len(self.timers)