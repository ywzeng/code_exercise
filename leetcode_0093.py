class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """ Find a partition, making the split IP address valid. """
        def is_valid(s: str, dot_index_list: list) -> bool:
            part_1, part_2, part_3, part_4 = s[:dot_index_list[0]], s[dot_index_list[0]: dot_index_list[1]], s[dot_index_list[1]: dot_index_list[2]], s[dot_index_list[2]:]
            if (len(part_1)>1 and part_1[0] == '0') or (len(part_2)>1 and part_2[0] == '0') or (len(part_3)>1 and part_3[0] == '0') or (len(part_4)>1 and part_4[0] == '0'):
                return False
            if 0<=int(part_1)<=255 and 0<=int(part_2)<=255 and 0<=int(part_3)<=255 and 0<=int(part_4)<=255:
                return True
            return False

        def back_track(s: str, begin: int, track_list: list, result_list: list) -> None:
            """ track_list stores the index of the inserted split-dot. """
            if len(s) > 12:
                return
            if len(track_list) == 3:
                if is_valid(s, track_list):
                    result_list += [track_list[:]]
                return
            
            for i in range(begin, len(s)):
                track_list += [i]
                back_track(s, i+1, track_list, result_list)
                track_list.pop()

        track_list, result_list = [], []
        back_track(s, 1, track_list, result_list)
        for i, dot in enumerate(result_list):
            result_list[i] = '.'.join([s[:dot[0]], s[dot[0]: dot[1]], s[dot[1]: dot[2]], s[dot[2]:]])
        return result_list
