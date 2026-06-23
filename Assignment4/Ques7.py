"""
Question 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
"""

run,over=map(float,input("Enter total run and total over").split())
rmg_ball=over-int(over)
balls = int(over)*6+rmg_ball*10
run_rate=run/over
print("Run rate :",run_rate)
print("Balls :",balls)
