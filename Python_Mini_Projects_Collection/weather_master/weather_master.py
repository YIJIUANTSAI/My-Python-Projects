"""
File: weather_master.py
Name: Christine
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -1


def main():
	"""
	This program finds the highest/ lowest/ average temperature,
	and the number of days that will issue the cold weather warning.
	"""
	print("stanCode \"Weather Master 4.0\"!")
	temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))

	if temperature == EXIT:
		print('No temperatures were entered.')
	else:
		highest = temperature
		lowest = temperature
		total_temperature = temperature
		day = 1
		cold_day = 0
		if temperature < 16:  # Solve OBOB
			cold_day += 1
		while True:
			temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if temperature == EXIT:
				break
			if temperature > highest:
				highest = temperature
			if temperature < lowest:
				lowest = temperature
			if temperature < 16:
				cold_day += 1
			total_temperature += temperature
			day += 1

		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = ' + str(lowest))
		print('Average = ' + str(float(total_temperature / day)))
		print(str(cold_day) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
