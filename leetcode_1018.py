class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        """
        From the left to the right is that from high bit to low bit.
        For example, the binary number of a decimal number '2' is '10', in which '1' is the high bit and '0' is the low bit.
        Note that, directly calculate the decimal number of the given 'binary number' is very stupid, which would undoubtedly lead to timeout.
        Given a binary sequence A, A[:i] = (A[:i-1]<<1) + A[i] = A[:i-1] * 2 + A[i].
        Besides, four important equation: 
        1. (a + b) % p = (a % p + b % p) % p;
        2. (a - b) % p = (a % p - b % p) % p;
        3. (a * b) % p = (a % p * b % p) % p;
        4. (a^b) % p = ((a % p)^b) % p.
        Therefore, we only need to calculate remainder of A[:i-1].
        """
        prior_remainder = A[0]
        result_list = [True] if prior_remainder == 0 else [False]
        for i in range(1, len(A)):
            current_remainder = (prior_remainder * 2 + A[i]) % 5
            result_list += [True] if current_remainder == 0 else [False]
            prior_remainder = current_remainder
        return result_list
