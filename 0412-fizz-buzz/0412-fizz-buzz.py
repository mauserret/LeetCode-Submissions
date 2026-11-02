class Solution:

  def fizzBuzz(self, n: int) -> list[str]:
    answer = []
    for i in range(1, n + 1):
      parts = []
      if i % 3 == 0:
        parts.append("Fizz")
      if i % 5 == 0:
        parts.append("Buzz")

      if parts:
        answer.append("".join(parts))
      else:
        answer.append(str(i))
    return answer