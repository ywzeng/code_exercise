# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self) -> int:
        """
        (rand_X - 1) * Y + rand_Y = rand_(X*Y).
        So, (rand7 - 1) * 7 + rand7 = rand49.
        Then, use refuse sampling method to refuse the generated number in [41, 49].
        For the numbers in [1, 40], using mod operation (%10) can get the numbers in [0, 9].
        Add [0, 9] with 1 can get [1, 10].
        :rtype: int
        """
        while True:
            rand_49 = (rand7() - 1) * 7 + rand7()
            # Refuse sampling.
            if rand_49 <= 40:
                return rand_49 % 10 + 1
