# Basic Probability Rules and Models
 #Machine Learning #hackerearth 
Problem: 
Mike wants to go fishing this weekend to nearby lake. His neighbour Alice (is the one Mike was hoping to ask out since long time) is also planing to go to the same spot for fishing this weekend. The probability that it will rain this weekend is p1. 
. There are two possible ways to reach the fishing spot (bus or train). The probability that Mike will take the bus is 'pmb' and that Alice will take the bus is 'pab' 
. Travel plans of both are independent of each other and rain.

What is the probability 'prs'
 that Mike and Alice meet each other only (should not meet in bus or train) in a romantic setup (on a lake in rain)?

Input constraints: 
0<= p1<= 1
, 0<= pab <= 1
, 0 <= pmb <= 1

Input format: 

First line: pmb 

Second line: pab 

Third line: p1

Output format: 

prs, rounded up to six decimal places.

Sample Input
0.20
0.20
0.50
Sample Output
0.16
  

Solution in Python(3.8) Code :
pmb = float(input().strip())
pab = float(input().strip())
p1 = float(input().strip())

# Probability of meeting during travel
meet_during_travel = (pmb * pab) + ((1 - pmb) * (1 - pab))

# Probability of meeting only at the lake in the rain
prs = p1 * (1 - meet_during_travel)

# Print result rounded to six decimal places
print(f"{prs:.6f}")
