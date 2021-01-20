class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Newton's method.
        Given a positive number N, get the sqrt of N.
        Suppose a random positive integer M， and iteratively calculate the M= (M+N//M)//2 until the integer M not changes.
        """
        init_integer = 1
        while True:
            temp_result = (init_integer + (x/init_integer)) / 2
            if abs(temp_result - init_integer) < 0.1:
                init_integer = int(temp_result)
                break
            init_integer = temp_result
        return init_integer
