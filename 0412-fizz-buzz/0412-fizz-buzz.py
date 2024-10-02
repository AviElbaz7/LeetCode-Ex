class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        strList = [0] * n
        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                strList[i] = "FizzBuzz"
            elif (i + 1) % 3 == 0:
                strList[i] = "Fizz"
            elif (i + 1) % 5 == 0:
                strList[i] = "Buzz"
            else:
                strList[i] = f"{i + 1}"
        return strList