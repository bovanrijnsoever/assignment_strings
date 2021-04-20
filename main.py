# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# UEFA Euro 1988 Final, part 1.
# In this part the code of the players who scored and when they scored.

# Players who scored:

scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'

print(scorer_1, scorer_2)

# Time of goals:
goal_0 = 32
goal_1 = 54

print(goal_0, goal_1)

# The time wich player scored:
scorers = scorer_1+' '+str(goal_0)+', '+scorer_2+' '+str(goal_1)
print(scorers)

report = str(scorer_1+' '+f"scored in the {goal_0}nd minute\n")+ str(scorer_2 + ' '+f"scored in the {goal_1}th minute")
print(report)

# # UEFA Euro 1988 Final, part 2.
#In the next part the code of the player's

player = 'Jan Wouters'

# first name of the player
print(player.find(' '))
first_name = player[0:3]
print(first_name)

#last name of the player 
print(player.find(' '))
print(len(player))
last_name_len = player[4:11]
print(last_name_len)

#the first letter and last name of the player
name_short = player[0:1]+'. '+ player[4:11]
print(name_short)

#the chant of the player's first name
chant = (first_name +'!'+' ') * 2 + (first_name+'!')
print(chant)

print(chant.find(' '))
print(3 * 4)
good_chant = chant[12] != ''
print(good_chant)
