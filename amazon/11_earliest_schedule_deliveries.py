from typing import List


def earliestTime(numOfBuildings: int, buildingOpenTime: List[int], offloadTime: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    offloadTime.sort()
    max_building_times = dict()
    for building_number in range(numOfBuildings):
        # Iterate each building with all subsets and try to find the one with the minimum possible
        if building_number not in max_building_times:
            max_building_times[building_number] = []
        idx = 0
        while idx <= len(offloadTime) - 4:

            subset = offloadTime[idx:idx+4]
            max_time = max(subset) + buildingOpenTime[building_number]
            max_building_times[building_number].append(max_time)
            idx += 4

        final_subset = offloadTime[idx:]
        if len(final_subset) > 0:
            max_time = max(subset) + buildingOpenTime[building_number]
            max_building_times[building_number].append(max_time)

    min_time = float('inf')
    for _, times in max_building_times.items():
        if len(times) > 0:
            min_time = min(min_time, max(times))

    return min_time
