rounds = []
with open('aoc_input.txt') as file:
    for line in file:
        rounds.append(line)

#PART 1  
shape_score=0
outcome = 0
for game in rounds:
    
    if game [2] == 'X':
        shape_score += 1
        if game[0] == 'A':
            outcome += 3
        elif game[0] == 'B':
            continue
        elif game[0] == 'C':
            outcome += 6
            
    elif game[2] == 'Y':
        shape_score += 2
        if game[0] == 'A':
            outcome += 6
        elif game[0] == 'B':
            outcome +=3
        elif game[0] == 'C':
            continue
            
    elif game[2] == 'Z':
        shape_score += 3
        if game[0] == 'A':
            continue
        elif game[0] == 'B':
            outcome +=6
        elif game[0] == 'C':
            outcome += 3
            
shape_score+outcome

# PART 2
shape_score = 0
outcome = 0
for game in rounds:
    
    if game [2] == 'X':
        if game[0] == 'A':
            shape_score += 3
        elif game[0] == 'B':
            shape_score += 1
        elif game[0] == 'C':
            shape_score +=2
            
    elif game[2] == 'Y':
        outcome += 3
        if game[0] == 'A':
            shape_score += 1
        elif game[0] == 'B':
            shape_score += 2
        elif game[0] == 'C':
            shape_score += 3
            
    elif game[2] == 'Z':
        outcome +=6
        if game[0] == 'A':
            shape_score += 2
        elif game[0] == 'B':
            shape_score += 3
        elif game[0] == 'C':
            shape_score += 1

shape_score+outcome
