import random
def primary():
  #print("Keep it logically awesome.")
  print("Hey! Here is a motivational quote for you:")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 25
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__ == "__main__":
    primary()
