class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_days(str_date: str) -> int:
            mm, dd = map(int, str_date.split("-"))
            print(months[:mm - 1])
            return sum(months[:mm - 1]) + dd
        
        start = max(date_to_days(arriveAlice), date_to_days(arriveBob))
        end = min(date_to_days(leaveBob), date_to_days(leaveAlice))
        print(start)
        print(end)
        return max(0, end - start + 1)
        