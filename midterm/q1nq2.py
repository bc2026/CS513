# 1. 
# No. It violates property 1: distance is always non-negative and commutativity.
# For the example, the distance in the z does not change so we calculate:
# D(0,1) = (0-1)^5  = -1 (violates property 1)
# D(0,1) = D(1,0)… (0-1)^5 =/= (1-0)^5 (violates property 2)
# D(x=0,z=0) <= d(x=0,y=1) + d(y=0, z=0)
# 0	<=  -1 + 0  this is false (violates property 3)




# 2. 
# P(COVID)=P(E)*P(EP)+P(I)*P(IP)+P(S)*P(SP)
# The chance the employee contracts covid is equal to his chance of going to each country and the rate of covid prevalence multiplied. 
# We add the probabilities since he can only go to England OR Italy OR Spain. 
# Since the employee is guaranteed to travel, the probabilities of each country must add up to 100% meaning the probability he goes to Italy is 100% - P(E) – P(S) = 30%. 
# Doing the calculation, we get:

# P(COVID) = ((.5)(1200) + (.2)(1500) + (.3)(1600))/(10^6) = .00138

# A = employee went to England 
# B = employee contracted covid (could be because they went to England therefore A and B are not independent)

# P(A|B) =  P(A) P(B|A)/P(B) = (.5)(1200/10^6)/P(COVID) = (.5)(1200/10^6)/.00138 = 0.434782608696
