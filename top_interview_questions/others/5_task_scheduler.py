from typing import List

"""
1. First sort the number of tasks in ascending order
2. Find the worst case, i.e. assuming that we only have one tasks and there will be all idle spots after each task
    - idle_times = (max_count - 1) * n (as we do not need to worry about the idle time after the final task)
3. The goal is to minimize this "idle_times" by inserting other tasks if available to us.
4. So, for other tasks, everytime we pop them from the end of the list (max first) and remove the idle times:
    - idle_times -= min(max_count - 1, counts.pop()) # Just makes sure that we don't have more tasks to fill than the idle slots

5. At the end, if our idle_spots are greater than 0, we add that to the total number of tasks and return it.


"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = dict()
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        # Sort the freq of each task in ascending order
        counts = sorted(list(freq.values()))

        # Consider the worst case: i.e. we only have one task repeated k times
        # The number of idle times will be
        max_count = counts.pop()  # pop from the end of the list, i.e. the max_count
        idles = (max_count - 1) * n

        # Now, if we have other tasks, we can fill those tasks in these idle places
        while counts and idles > 0:
            idles -= min(max_count - 1, counts.pop())

        idles = max(0, idles)

        return len(tasks) + idles
