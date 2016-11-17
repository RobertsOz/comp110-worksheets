#A
```
multiplier = 20
multiplicand = 5
result = 0
counter = multiplier

while counter > 0:
  result += multiplicand
  counter -= 1
```
#B
Because the bne statement creates a while loop on a counter that is as long as s0(multiplier). 
So the code will go through the loop s0 times on every loop adding s1(multiplicand) to result. 
If s0 is 5 and s1 is 4 it will go through and write out 4+4+4+4+4 which is the same thing as saying 5x4.
#C
```
factorial = 10
result = 1

while factorial > 0:
    stageresult = 0
    counter = factorial
    while counter > 0:
        stageresult += result
        counter -= 1
    result = stageresult
    factorial -= 1
```
#D
Because it is two nested while loops that multiply s0 with s1 in s2, then s1 changes to the s2 value after that s0 gets subtracted by 1 and repeats the process until s0 is 0.
So these two multiplication loops go through the factorial multiplication on every loop.
If s0 was 5 It would look like this every loop
(s0)x(s1)
5x1=5,
4x5=20,
3x20=60,
2x60=120,
1x120=120.
Which is the same as 5x4x3x2x1
#E
```
addi s0, $zero, 10
addi s1, $zero, 1
loop: mult s1, s0
mflo s3
addi s1,s3,0
addi s0, s0, -1
bne s0 ,$zero, loop
```

