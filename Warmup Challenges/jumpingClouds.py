
"""

	There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

	For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.
	
	Example:
	
		c=[0,1,0,0,0,1,0]
		returns 3
		why? shorter path is 0-2-4-6
"""

def jumpingOnClouds(arr):
    res = 0
    position = 0
    n = len(arr)
    while position != n - 1:
        if position < (n - 2) and arr[position + 2] == 0:
            position += 2
            res += 1
        else:
            position+=1
            res+=1
    return res