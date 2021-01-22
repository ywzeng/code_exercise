class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda item: item[0], reverse=False)
        merge_list = [intervals[0]]
        for i in range(1, len(intervals)):
            has_matched = False
            for j, merge_interval in enumerate(merge_list):
                if intervals[i][0] >= merge_interval[0] and intervals[i][0] <= merge_interval[1]:
                    merge_list[j] = [min(intervals[i][0], merge_interval[0]), max(intervals[i][1], merge_interval[1])]
                    has_matched = True
                    break
            if not has_matched:
                merge_list += [intervals[i]]
        return merge_list
