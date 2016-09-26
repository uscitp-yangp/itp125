print "Hello World"

fib= []

f1 = 1
f2 = 2

fib.append(f1)
fib.append(f2)

answer = 0

# Generate fib seq
for i in range(2, 4000000):
    # Make the new fib number with the previous 2 numbers
    fib.append(f1 + f2)

    # Store f2 into f1
    f1 = f2

    # Store the new fib number into f2
    f2 = fib[len(fib)-1]

    if f2 > 4000000:
        break

for i in range (0, len(fib)):

    if fib[i] % 2 == 0:
        answer = answer + fib[i]

print (answer)
