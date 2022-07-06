import random

#probability to hit
a = 0.5
b = 0.75
c = 0.5

#number of games
n = 100

def shootout(n, a, b, c):
  totals = [0]*3   #initialize totals to hold a, b, and c wins respectively
  i = 0
  while i < n:     #Play n-number of times
    G_O = False      #Game over boolean. As long as this is not true, the game keeps going
    #a going first, this is how we will check hits
    if random.random() < a:
      #if a hits b...
      if random.random() < c:
        #if c hits a, the game is over
        totals[2] += 1
        print(totals)
      else:
        #if c misses, a hits
        #since the p(a hits) and p(c hits) are the same
        #we only have to check whether c hits, otherwise a hits
        #similar to flipping a coin
        totals[0] += 1
        print(totals)
    #if a misses b, and b hits c...
    elif random.random() < b:
      while G_O == False:
        #if a hits, the game is over and a wins
        if random.random() < a:
          totals[0] += 1
          print(totals)
          G_O = True
        #if a misses, b goes and if b hits, the game is over
        elif random.random() < b:
          totals[1] += 1
          print(totals)
          G_O = True
    #if a and b miss, c gets to go
    #if c hits a...
    elif random.random() < c:
      while G_O == False:
        if random.random() < b:
          totals[1] += 1
          print(totals)
          G_O = True
        elif random.random() < c:
          totals[2] += 1
          print(totals)
          G_O = True
    #if nobody hits, we need to redo the round and decrement i (no negative values)
    else:
      if i > 0:
        i -= 1
        #You can comment this out if you want, was used for personal debugging in first code
        #print("Nobody won, redo\t", i)
      else:
        i = -1
        #print("Nobody won, redo\t", i)
    i += 1
  return totals
