'''Write a function to calculate total reward for a given number of steps.
 For every 1000 steps → ₹5
 Every 5000th step → bonus ₹20'''

def total_reward(steps):
    # write your code here
    if steps<5000:
        total=(steps//1000)*5
    else:
        total =(steps//1000)*5+(steps//5000)*20    
    print(total)
total_reward(4000)
total_reward(6000)
total_reward(10000)