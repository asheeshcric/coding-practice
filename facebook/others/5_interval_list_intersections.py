from typing import List


class Solution:
    def get_intersection(self, int1, int2):
        intersection = [max(int1[0], int2[0]), min(int1[1], int2[1])]
        if intersection[0] > intersection[1]:
            # This means no intersection was found
            return None
        else:
            return intersection

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first, second = 0, 0
        output = []
        while first < len(firstList) and second < len(secondList):
            inter = self.get_intersection(firstList[first], secondList[second])
            if inter:
                output.append(inter)

            # Check which pointer to increase: first or second
            if firstList[first][1] <= secondList[second][1]:
                # Increase the first pointer
                first += 1
            else:
                second += 1

        return output
