# PART 1
calories = []
with open('aoc_input.txt') as file:
    for line in file:
        calories.append(line)

total_calories = []       
elf_total=0
for food_item in calories:
    if food_item == '\n':
        total_calories.append(elf_total)
        elf_total=0
    elif int(food_item) >0:
        elf_total += int(food_item)
        
max(total_calories)

# PART 2
total_calories[-1] + total_calories[-2] + total_calories[-3]
