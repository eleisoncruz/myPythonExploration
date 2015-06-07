def mood(theMood):
  theMood = str(theMood).split()
  score = 0
  hits = 0

  # here are the words depending in moods of people
  sadMeter = ["hate", "unfortunate", "reject", "abandon", "no", "no luck", "unlove", "hope", "sad"]
  happyMeter = ["happy", "content", "love", "yehey", "lucky", "joy", "rejoice"]
  normalMeter = ["normal", "fine", "ok", "ordinary"]

  # Test if the mood is sad, happy, or normal
  for a in theMood:
    for x in sadMeter:
      if a == x:
        score = score - 2
        hits = hits + 1
    for y in happyMeter:
      if a == y:
        score = score + 2
        hits = hits + 1
    for z in normalMeter:
      if a == z:
        score = score + 1
        hits = hits + 1

  # Set the average score of all moods
  average = score / hits

  # Test now the mood in average
  if average <= 0 and average < 4:
    moodMeter = "Sad"
  elif average <= 5:
    moodMeter = "Normal"
  elif average <= 10:
    moodMeter = "Happy"
  else:
    moodMeter = "Very Happy"
    
  return str(moodMeter) + " " + str(average) 

print mood(raw_input('Input a string: \n'))
