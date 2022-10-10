
def take_score(elem):
  return elem[1]

def podium(scores):
  scores.sort(key=take_score, reverse=True)
  return scores[0:3] 
  pass

#test
scores = [('Alice',30), ('Bob', 30), ('Phil', 40), ('Michael', 15)]
print(podium(scores))
