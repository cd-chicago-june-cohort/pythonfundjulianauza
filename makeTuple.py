my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


tuplist=[]
for key, value in my_dict.iteritems():
    tupl=()
    a=key
    b=value
    tupl=(a,b)
    tuplist.append(tupl)
print tuplist