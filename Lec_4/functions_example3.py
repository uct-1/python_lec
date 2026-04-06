def computepay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    else:
        return hours * rate

h = float(input("Hours: "))
r = float(input("Rate: "))

print(computepay(h, r))