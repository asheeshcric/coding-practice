"""
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. 
The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, 
he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. 
The character 'R' and 'D' represent the Radiant party and the Dire party. 
Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. 
This procedure will last until the end of voting. 
All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. 
Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

"""

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R_queue = deque()
        D_queue = deque()
        for i, person in enumerate(senate):
            # Separating all indices of Rs and Ds into two separate queues to see which comes first
            if person == "R":
                R_queue.append(i)
            else:
                D_queue.append(i)

        while R_queue and D_queue:
            R_idx, D_idx = R_queue.popleft(), D_queue.popleft()
            if R_idx < D_idx:
                # This means R is going to destroy D as it comes first
                # So, we need to put back R into the queue as we will revisit it again next round
                R_queue.append(R_idx + len(senate))
            else:
                # D wins over R
                D_queue.append(D_idx + len(senate))

        return "Radiant" if R_queue else "Dire"
