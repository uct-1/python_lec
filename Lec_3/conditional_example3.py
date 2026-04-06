sh = input("Hours: ")
sr = input("Rate: ")

try:
    h = float(sh)
    r = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

if h > 40:
    pay = 40 * r + (h - 40) * (r * 1.5)
else:
    pay = h * r

print(pay)