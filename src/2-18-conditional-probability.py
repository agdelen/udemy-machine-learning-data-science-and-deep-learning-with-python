from numpy import random

random.seed(0)

totals = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
purchases = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
totalPurchases = 0

for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    # lecture
    purchaseProbability = float(ageDecade) / 100.0
    # exercise
    # purchaseProbability = random.random_sample()
    totals[ageDecade] += 1
    if random.random() < purchaseProbability:
        totalPurchases += 1
        purchases[ageDecade] += 1

print('totals= {0}'.format(totals))
print('purchases= {0}'.format(purchases))
print('totalPurchases= {0}'.format(totalPurchases))

# first lets compute P(E|F) where E is purchase and F is you are in your 30's.
# the probability of someone in their 30's buying something is just the percentage of
# how many 30-year-old bought something
PEF = float(purchases[30]) / float(totals[30])
print('P(purchase | 30s)= {0}'.format(PEF))

# P(F) is just the probability of being 30s in this set
PF = float(totals[30]) / 100000.0
print('P(30s)= {0}'.format(PF))

# and P(E) is the overall probability of buying something regardless of your age
PE = float(totalPurchases) / 100000.0
print('P(purchase)= {0}'.format(PE))

# If E and F were independent then we would expect P(E|F) to be about the same as P(E), but they are not.
# P(E) is 0.45 and P(E|F) is 0.3. So that tells us E and F are dependent

print('P(30s)P(purchase)= {0}'.format(PE * PF))

# P(E,F) is different from P(E|F). P(E,F) would be probability of both being 30s and buying something
# out of the total population - not just the population of people in their 30s

print("P(30s, purchase)=", float(purchases[30]) / 100000)

# if E and F are independent the formula holds P(E,F)=P(E)P(F) but in our example E and F
# are dependent which bring us the conditional probability formula
# P(E|F) = P(E,F)/P(F)


print("P(purchase|30s) = P(30s, purchase)/P(30s) =", (float(purchases[30]) / 100000) / PF)
