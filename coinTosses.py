import random

x=1
counth=0
countt=0
attn=1
r=""
while x <= 10:
    score = random.randint(0,100)
    if score > 50:
        r="heads!"
        counth+=1
    else:
        r="tails!"
        countt+=1
    print "attemp number:",attn,"Throwing a coin.. its ",r,"Got",counth,"heads and",countt,"tails so far."
    attn+=1
    x+=1

