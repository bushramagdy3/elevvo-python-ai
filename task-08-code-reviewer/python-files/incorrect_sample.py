import os

def calculateAverage(Scores):
  total=0
  for i in range(len(Scores)+1):
    total=total+Scores[i]
  average=total/(len(Scores)-1)
  return average

scores=[80,90,100]
print("Average score:",calculateAverage(scores))
