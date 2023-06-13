# "Hello, World!"
given=input().upper()

for i in range (0,len(given)):
   words =ord(given[i])
   if 97 <= words <= 122:
       words=words-32
   big =chr(words)

   
keys=""
key_list={1 :".,?!:"
          ,2 :"ABC"
          ,3: "DEF",4 :"GHI", 5 :"JKL" 
          ,6 :"MNO"
          ,7: "PQRS"
          ,8 :"TUV"
          ,9 :"WXYZ"
          ,0 :" "}

for i in given:
  for k,v in key_list.items():
    if i in v:
      button_press=v.index(i)+1
      keys += str(k)*button_press

print(keys)