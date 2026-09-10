numbers = [1,3,5,7,9,8,6,4]
position = 0
print("Starting value:", numbers[position])
while True:
  current = numbers[position]
  if position < len(numbers)-1 and numbers[position+1] > current:
    position = position + 1
    print("Moved to:", numbers[position])
  elif position > 0 and numbers[position - 1] > current:
    position = position - 1
    print("Moved to:", numbers[position])
  else:
    break
print("Game over!")
print("Highest value reached:", numbers[position])

output:Starting value: 1
Moved to: 3
Moved to: 5
Moved to: 7
Moved to: 9
Game over!
Highest value reached: 9
