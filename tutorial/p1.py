'''
randomness with drawing red card 10,000 times let say
'''
import random 

red_card = set(range(1, 27))
deck = list(range(1, 53))
t =  []

# simulation 
red_count = 0
trials = 100000

for i in range(1, trials + 1):
    draw = random.choice(deck)
    if draw in red_card:
        red_count += 1

    # red count
    c = red_count / i
    print(c)
    t.append(c)

avg = sum(t) / len(t)
print("average:", avg)