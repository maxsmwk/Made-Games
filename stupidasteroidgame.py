"""
Question 3: Orbital Defense Game (30 pts)

You are developing a game called Orbital Defense, in which the player
controls a laser turret to protect a space station from incoming
asteroids. The battlefield is divided into five lanes, numbered 1
through 5. In each round, the player chooses a lane to aim at, while
an asteroid appears in a randomly selected lane. The player earns
points based on how closely the turret's aim matches the asteroid's
location.

Scoring Rules
  - Direct hit: The turret and asteroid are in the same lane.
    Base score: 3 points.
  - Near hit: The turret and asteroid are in adjacent lanes.
    Base score: 1 point.
  - Miss: The lanes are separated by 2 or more positions.
    Base score: 0 points.

Consecutive Direct Hit Bonus
  - If two or more consecutive completed rounds are direct hits, award
    an extra 2 points for each direct hit starting with the second one.
    For example, three direct hits in a row earn 3, 5, and 5 points.
  - A near hit or a miss ends the consecutive-direct-hit streak.
    A direct hit after that starts a new streak and earns 3 points.
  - Invalid input is not a completed round. It must not affect the
    score, the round count, or an existing streak.

Implement the following four functions using the exact function names
and parameters specified below:

1. validate_lane(choice)
   Given the user's input as a string, return an integer from 1 through 5
   for a valid lane. Return the empty string ("") if the input is empty.
   Raise ValueError if the lane number is outside the valid range.

2. random_asteroid_lane()
   Randomly generate and return an integer from 1 through 5,
   inclusive, representing the asteroid's lane.

3. score_shot(turret_lane, asteroid_lane)
   Given turret_lane and asteroid_lane as integers, return the base score
   for the round (3, 1, or 0) using the scoring rules above. Do not
   include the consecutive-hit bonus in this value.

4. main()
   Run the interactive game in an infinite loop, following these steps
   in order:
   - Prompt the player to choose a turret lane.
   - Pass the input to validate_lane. If the function returns an empty
     string, end the game. If it raises a ValueError, display an error
     message and prompt again without generating an asteroid or changing
     the score, round count, or consecutive-hit streak.
   - If validate_lane returns a valid lane, call random_asteroid_lane
     to determine the asteroid's lane.
   - Call score_shot to calculate the base score, then determine any
     consecutive direct hit bonus using the scoring rules above. Calculate
     the points earned for the round by adding the base score and bonus.
   - Count the completed round and add the points earned to the
     running total score.
   - Display the player's lane, the asteroid's lane, the base points,
     the bonus points, the points earned in that round, and the running
     total score.
   When the game ends, display the number of completed rounds and the
   final total score.

Make sure to call your main() function.

Expected Output Example

The following is one possible run. Player inputs, random outcomes,
and wording may differ, but your program must display all the
information shown.

Orbital Defense
Choose a turret lane from 1 to 5 (Enter to quit).
Select lane: 3
Turret lane: 3
Asteroid lane: 3
Base points: 3
Streak bonus: 0
Points earned: 3
Total score: 3

Select lane: x
Invalid lane. Please enter a whole number from 1 to 5.
Select lane: 3
Turret lane: 3
Asteroid lane: 3
Base points: 3
Streak bonus: 2
Points earned: 5
Total score: 8

Select lane: 5
Turret lane: 5
Asteroid lane: 4
Base points: 1
Streak bonus: 0
Points earned: 1
Total score: 9

Select lane: 4
Turret lane: 4
Asteroid lane: 4
Base points: 3
Streak bonus: 0
Points earned: 3
Total score: 12

Select lane:
Rounds played: 4
Final score: 12
"""

import random

def validate_lane(choice):
  #IF BLANK
  if choice == "":
    choice = ""
  
  else:
    choice = int(choice)

    #RAISE ERRORE
    try:
      if choice > 5:
        raise ValueError("Your choice should be between 1 and 5!")
    except ValueError:
      return -1

  return choice

def random_asteroid_lane():
  return random.randint(1,5)

def score_shot(turret_lane, asteroid_lane):
  score = 0
  #DIRECT HIT
  if turret_lane == asteroid_lane:
    score = 3
  #ADJACENT
  elif (asteroid_lane + 1) >= turret_lane >= (asteroid_lane - 1):
    score = 1
  else:
    score = 0

  return score


def main():
  loop = True
  base_score = 0
  if_consecutive = False
  bonus_points = 0
  rounds = 0
  while loop:
    #USER INPUT

    user_choice = input("Which lane do you choose(1 - 5): ")

    #VALIDATION
    user_lane = validate_lane(user_choice)

    #ENDGAME
    if user_lane == "":
      loop = False

    #ERR
    elif user_lane == -1:
      print("You must select a value between 1 and 5!")
      continue


    else:
    #SCORE DETERMINATION
      asteroid_lane = random_asteroid_lane()
      score = score_shot(user_lane, asteroid_lane)
      if score == 3 and if_consecutive == True:
        base_score += score + 2
        bonus_points += 2
        rounds += 1
      elif score == 3:
        if_consecutive = True
        base_score += score
        rounds += 1
      elif score == 1:
        if_consecutive = False
        base_score += score
        rounds += 1
      else:
        if_consecutive = False
        base_score += score
        rounds += 1

      #DISPLAY
      print("Player Lane: ", user_lane)
      print("Asteroid Lane: ", asteroid_lane)
      print("Your score this round: ", score)
      print("Bonus points: ", bonus_points)
      print("Total points: ", base_score)

  #END OF GAME
  print("Rounds played: ", rounds)
  print("Final score: ", base_score)



        
if __name__ == "__main__":
  main()
