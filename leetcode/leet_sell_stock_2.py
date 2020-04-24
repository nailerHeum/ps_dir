class Solution:
    def checkValidString(self, s: str) -> bool:
        plus_joker = 0
        joker = 0
        balance = 0
        for c in s:
            if balance < joker:
                plus_joker += joker - balance
                joker = balance
            if c is '(':
                balance += 1
            if c is ')':
                if balance > 0:
                    balance -= 1
                    continue
                if plus_joker > 0:
                    plus_joker -= 1
                    continue
                if joker > 0:
                    joker -= 1
                    continue
                return False
            if c is '*':
                if balance == 0:
                    plus_joker += 1
                else:
                    joker += 1
        if balance <= joker:
            return True
        return False

sol = Solution()
print(sol.checkValidString("(())(())(((()*()()()))()((()()(*()())))(((*)()"))
## (**((*