# Pablo Sanchez
# Python version 2.7.10
# Grade Conversion


score = int(raw_input("Enter assignment score: "))

if score >= 95:
    grade = "A+"
elif score >= 90:
    grade = "A"
# Complete this conditional statement using the rest of the scale
elif score >= 85:
    grade = "B+"
elif score >= 80:
    grade = "B"
elif score >= 75:
    grade = "C"
elif score >= 70:
    grade = "D"
else:
    grade = "F"

print "You earned a " + grade + " for this assignment."