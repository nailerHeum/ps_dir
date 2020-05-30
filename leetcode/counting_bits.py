class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        answer = [1]
        counter = 1
        exp = 1
        while 2**(exp - 1) < num:
            tmp = []
            for v in answer[:2**(exp - 1)]:
                counter += 1
                if counter > num:
                    break
                if counter == 2 ** exp:
                    tmp.append(1)
                    continue
                tmp.append(v + 1)
            answer += tmp
            exp += 1
        return [0] + answer
