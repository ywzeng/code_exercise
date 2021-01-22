class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda item: item[0], reverse=False)
        merge_list = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merge_list[-1][1]:
                merge_list[-1] = [merge_list[-1][0], max(intervals[i][1], merge_list[-1][1])]
            else:
                merge_list += [intervals[i]]
        return merge_list
