

EXIT = -1


def main():
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


if __name__ == "__main__":
	main()
