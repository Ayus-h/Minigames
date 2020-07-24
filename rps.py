def rps():
  import random 
  moves=["rock","paper","scissors"]

  while True:
    c = random.choice(moves)

    p = input("Choose your move: rock, paper, or scissors? ")
    if not(p == "rock" or p == "paper" or p == "scissors"):
      print("Try again - enter the words exactly as they are written")
      pass
    else:
      print("I chose",c)
      if c == p:
         print("Tie, let's play again")
      elif p == "scissors" and c == "paper":
        print("You win")
      elif p == "paper" and c == "rock":
        print("You win")
      elif p == "rock" and c == "scissors":
        print("You win")
      elif p == "paper" and c == "scissors":
        print("I win")
      elif p == "rock" and c == "paper":
        print("I win")
      elif p == "scissors" and c == "rock":
        print("I win")
      while not(c == p):
        quit()
rps()

