m = int(input())
tot = m/600
per = tot*100

print("You have scored {:.2f}% of marks".format(per))

if per<35:
    print("Failed")
elif per>=35 and per<50:
    print("Passed")
elif per>=50 and per<60:
    print("Second class")
elif per>=60 and per<70:
    print("First Class")
else:
    print("First class with dist")