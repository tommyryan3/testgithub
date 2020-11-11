from numpy import random
# ~2348 combinations
units = [1,2,5,10,20,50,100,200]
sum = 0
combinations = []
# the best way I could come up with was to try a bunch of random combinations and see how many different ones you can generate. This obviously won't get the exact answer but I am pretty confident that it is close. (I'm aware this isn't really what you are looking for, but I couldn't think of a cleaner way)
for i in range(0,500000):
  combination = []
  while sum < 200:
    if sum > 198:
      unit = units[0]
    elif sum > 195:
      unit = units[random.randint(0,2)]
    elif sum > 190:
      unit = units[random.randint(0,3)]
    elif sum > 180:
      unit = units[random.randint(0,4)]
    elif sum > 150:
      unit = units[random.randint(0,5)]
    elif sum > 100:
      unit = units[random.randint(0,6)]
    else:
      unit = units[random.randint(0,8)]
    sum += unit
    combination.append(unit)
  if sum == 200:
    if sorted(combination) not in combinations:
      combinations.append(sorted(combination))
  sum = 0

print(len(combinations))
print(combinations[:10])