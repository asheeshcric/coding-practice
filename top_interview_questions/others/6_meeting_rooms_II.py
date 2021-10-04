from typing import List


class Solution:
    # def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    #     times = []
    #     for start, end in intervals:
    #         times.append((start, 1))
    #         times.append((end, 0))

    #     # If we encounter the same times, we want to first end the meetings if possible before starting a new one
    #     times.sort(key=lambda x: (x[0], x[1]))

    #     min_rooms = 0
    #     curr_rooms = 0
    #     for i, (time, start) in enumerate(times):
    #         if start == 1:
    #             curr_rooms += 1
    #         else:
    #             curr_rooms -= 1

    #         min_rooms = max(min_rooms, curr_rooms)

    #     return min_rooms

    # Faster approach
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for s, e in intervals:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()
        min_rooms, curr_rooms = 0, 0
        first, second = 0, 0
        while first < len(start):
            if start[first] < end[second]:
                curr_rooms += 1
                first += 1
            else:
                # Since both are at the same time, we first end the meeting
                curr_rooms -= 1
                second += 1

            min_rooms = max(curr_rooms, min_rooms)

        return min_rooms
