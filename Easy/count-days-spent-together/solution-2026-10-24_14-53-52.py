class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_calc(month, day):
            calc = 0
            for i in range(month - 1):
                calc += days[i] 
            return calc + day 
        
        alice_start = day_calc(int(arriveAlice[:2]), int(arriveAlice[3:])) 
        alice_end = day_calc(int(leaveAlice[:2]), int(leaveAlice[3:])) 
        bob_start = day_calc(int(arriveBob[:2]), int(arriveBob[3:])) 
        bob_end = day_calc(int(leaveBob[:2]), int(leaveBob[3:]))

        overlap = min(alice_end, bob_end) - max(alice_start, bob_start) + 1

        return max(overlap, 0)