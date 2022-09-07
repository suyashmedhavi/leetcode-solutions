# https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(x+1) for x in range(n)]
        for i in range(n):
            d3 = (i+1)%3 == 0
            d5 = (i+1)%5 == 0
            if d3 and d5:
                answer[i] = "FizzBuzz"
            elif d3:
                answer[i] = "Fizz"
            elif d5:
                answer[i] = "Buzz"
        return answer

