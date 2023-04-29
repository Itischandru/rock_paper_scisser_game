import random
you=0
computer=0
options=['rock','paper','scisser']
while True:
  userinput=input('Type rock/paper/scisser or q to quit :').lower()
  if userinput=='q':
    break

  if userinput not in options:
    continue

  random_number=random.randint(0, 2)
  computer_pic=options[random_number]
  print('computer picked',computer_pic+'.')
  if userinput=='rock' and computer_pic=='scisser':
    print('you own!')
    you+=1
  elif userinput=='paper' and computer_pic=='rock':
    print('you own!')
    you+=1
  elif userinput=='scisser' and computer_pic=='paper':
    print('you own!')
    you+=1
  else:
    print('computer own!')
    computer+=1

print('your own :',you)
print('computer own :',computer)
print('Goodbye')