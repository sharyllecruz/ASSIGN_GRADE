print("Input your grade here, and we'll see what if your rank.")

while True:
		try:
			grade= int(input("input your grade here:"))
			if grade >=90:
				print("Grade A")
				print("You're a outstanding student! Keep it up!")
			elif grade >=80:
				print("Garde B")
				print("Great!")
			elif grade >=70:
				print("Grade C")
				print("Good!")
			elif grade >=60:
				print("Grade D")
				print("Study more! I know you can do better!")
			elif grade >=1:
				print("Gade F")
				print("Buhay ay hindi karera. Kimi, study more!")
			else:
				print("Invalid grade! Please enter a value between 0 and 100.")
		except:
			print("Invalid grade! Please enter a value between 0 and 100.")