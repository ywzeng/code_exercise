class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result_list = []
        carry = False
        a_index, b_index = len(a)-1, len(b)-1
        while a_index >= 0 or b_index >= 0 or carry:
            if a_index >= 0 and b_index >= 0:
                if a[a_index] == '1' and b[b_index] == '1':
                    if carry:
                        result_list.insert(0, '1')
                    else:
                        result_list.insert(0, '0')
                    carry = True
                elif a[a_index] == '0' and b[b_index] == '0':
                    if carry:
                        result_list.insert(0, '1')
                    else:
                        result_list.insert(0, '0')
                    carry = False
                else:
                    if carry:
                        result_list.insert(0, '0')
                        carry = True
                    else:
                        result_list.insert(0, '1')
                        carry = False
                a_index -= 1
                b_index -= 1
            elif a_index < 0 and b_index < 0 and carry:
                result_list.insert(0, '1')
                carry = False
            else:
                if a_index >= 0:
                    if carry:
                        if a[a_index] == '1':
                            result_list.insert(0, '0')
                            carry = True
                            a_index -= 1
                        else:
                            result_list.insert(0, '1')
                            carry = False
                            a_index -= 1
                    else:
                        result_list.insert(0, a[:a_index+1])
                        a_index = -1
                else:
                    if carry:
                        if b[b_index] == '1':
                            result_list.insert(0, '0')
                            carry = True
                            b_index -= 1
                        else:
                            result_list.insert(0, '1')
                            carry = False
                            b_index -= 1
                    else:
                        result_list.insert(0, b[:b_index+1])
                        b_index = -1
        return ''.join(result_list)
