# Inputs
cutOffRank = 3
scores = [25, 10, 25, 5, 10, 5]

# Output should be: 3 as ranks will be [1, 2, 2, 4]

rank = 0
total_rank = 0
last_score = 0
scores.sort(reverse=True)
level_up = 0
for score in scores:
    if score == 0:
        break

    total_rank += 1
    if score != last_score:
        rank = total_rank

    last_score = score
    if rank <= cutOffRank:
        level_up += 1
    else:
        break


print(f'Number of people leveling up: {level_up}')
