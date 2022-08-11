import random
stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    l=[stone,paper,scissors]
    User=int(input('Enter 0 for stone , 1 for paper, 2 for scissors and press -1 for Exit: '))
    print(l[User])
    computer=random.randint(0,2)
    print(l[computer])
    if User == computer:
        print('Match is Tie')
    elif User == 0 and computer ==1:
        print('Computer Win')
    elif User == 0 and computer ==2:
        print('You Win')
    elif User == 1 and computer ==0:
        print('You Win')
    elif User == 1 and computer ==2:
        print('Computer Win')
    elif User == 2 and computer ==0:
        print('Computer Win')
    elif User == 2 and computer ==1:
        print('You Win')
        if User == -1:
            break

    
















