def fizzbuzz(x):
    if x%3 == 0 and x%5 == 0:
        return "fizzbuzz"
    elif x%3 == 0:
        return "fizz"
    elif x%5 == 0:
        return "buzz"
    else:
        return str(x)

def starter():
  fizz_list = [fizzbuzz(k) for k in range(1, 31)]
  print('''Welcome to FizzBuzz. Start counting from 1 all the way to 30.
The rules are simple:
if the number is divisible by 3, enter 'fizz',
if it's divisible by 5, enter 'buzz',
if it's divisible by 3 and 5, enter 'fizzbuzz'.''')
  for i in range(len(fizz_list)):
    x = input("Enter your answer: ")
    if not (x  == fizz_list[i]):
      print("You failed, the answer was",fizz_list[i])
      quit()
starter()
