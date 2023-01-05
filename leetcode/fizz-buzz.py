class Solution:
    def fizzBuzz(self, t: int) -> List[str]:
        l=[]
        for i in range(1,t+1):
            if i%3==0 and i%5==0:
                l.append("FizzBuzz")
            elif i%3==0:
                l.append("Fizz")
            elif i%5==0:
                l.append("Buzz")
            else:
                l.append(str(i))
        return l
