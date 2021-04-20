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
goal_1 = 32
goal_2 = 54

print(goal_1, goal_2)

# The time wich player scored:
scorers = scorer_1+' '+str(goal_1)+', '+scorer_2+' '+str(goal_2)
print(scorers)

report = f'{scorer_1} scored in the {goal_1}nd minute\n{scorer_2} scored in the {goal_2}th minute'
print(report)

# # UEFA Euro 1988 Final, part 2.
#In the next part the code of the player's

player = 'Jan Wouters'

# first name of the player
print(player.find(' '))
first_name = player[:player.find(' ')]
print(first_name)

#last name of the player 
print(player.find(' '))
print(len(player))

last_name_len = player[(player.find(' ')):(len(player))]
print(last_name_len)

#the first letter and last name of the player
name_short = player[0]+'.'+ player[(player.find(' ')):(len(player))]
print(name_short)

#the chant of the player's first name
chant = (first_name +'!'+' ') * len(first_name)
print(chant)

#the good chant
chant_len = (len(chant))
print(chant_len)
good_chant = chant_len != ' '
print(good_chant)
