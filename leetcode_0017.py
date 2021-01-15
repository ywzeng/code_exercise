class Solution:
    def __init__(self):
        self.keyboard_dict = {'2': 'abc', '3': 'def', '4': 'ghi',
                                '5': 'jkl', '6': 'mno', '7': 'pqrs', 
                                '8': 'tuv', '9': 'wxyz'}
        self.result_list = []

    def letterCombinations(self, digits: str) -> List[str]:
        track_list = []
        self.back_track(digits, 0, track_list)
        return self.result_list
    
    def back_track(self, digits: str, digit_index: int, track_list: list) -> None:
        if not digits:
            return
        if len(track_list) == len(digits):
            self.result_list += [''.join(track_list)]
            return
        
        for i in range(digit_index, len(digits)):
            for c in self.keyboard_dict[digits[i]]:
                track_list += [c]
                self.back_track(digits, i+1, track_list)
                track_list.pop()
