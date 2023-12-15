score=[
  (2000,"player1"),(1600,"player3"),(600,"player2")
]

print("\x1b[43;30m")

score.sort(reverse=True)

for i in score:
  
  print(f"{i[1]:40}{i[0]:10}")
