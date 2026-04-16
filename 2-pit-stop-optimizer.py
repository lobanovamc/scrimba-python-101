# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following: 
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

race_time = float(input('Total race time in seconds: '))
pit_stops = int(input('How many pit stops did you make? '))
pit_stop_duration = float(input('What is the average pit stop duration? '))

total_pit_stop_time = pit_stops * pit_stop_duration
percentage_pits = round((total_pit_stop_time / race_time * 100), 2)

print('Total pit stop time:' , total_pit_stop_time , 'sec')
print('Percentage of race time spent in pits:' , percentage_pits, '%')

if percentage_pits > 5: 
    print('You need a new pit crew. 🛠️')
