hand = open('regex_sum_42.txt')
for line in hand :
	line = line.rstrip()
	if line.find('[0-9.]+') !=0 :
		print(line)
