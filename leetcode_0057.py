class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if (not intervals and newInterval) or (intervals and not newInterval):
            return intervals if intervals else [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        elif newInterval[0] > intervals[-1][1]:
            intervals += [newInterval]
            return intervals
        else:
            for i in range(len(intervals)):
                if newInterval[0] <= intervals[i][0]:
                    intervals.insert(i, newInterval)
                    break
                elif newInterval[0] <= intervals[i][1]:
                    intervals[i] = [intervals[i][0], max(newInterval[1], intervals[i][1])]
            merged_list = [intervals[0]]
            # Rearrange the list from index 'i' to the end.
            for j in range(1, len(intervals)):
                if intervals[j][0] <= merged_list[-1][1]:
                    merged_list[-1] = [merged_list[-1][0], max(merged_list[-1][1], intervals[j][1])]
                else:
                    merged_list += [intervals[j]]
            return merged_list
