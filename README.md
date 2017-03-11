# AnanthJars

A program that takes three integers - first two the size of two jars and third, the desired quantity, and print out steps to get the desired quantity. For example, if you have two jars which can measure 3 liters and 5 liters, how would you measure exactly 4 liters

Hint: Size of jar 1 and jar 2 are relatively prime and the desired size is less than that of the jar 2 size.

E.g.

Input

Size of Jar1: 3 Size of Jar2: 5 Desired: 4

Output

Jar1: 3 Jar2: 0 Jar1: 0 Jar2: 3 (ie., poured 3 liters from Jar 1 to Jar 2) Jar1: 3 Jar2: 3 (ie., have refilled Jar 1 with 3 liters) Jar1: 1 Jar2: 5 (ie., poured 2 liters from Jar 1 to Jar 2 and Jar 2 got filled) Jar1: 1 Jar2: 0 (ie., emptied out Jar2) Jar1: 0 Jar2: 1 (ie., poured the remaining 1 liter in Jar 1 to Jar 2) Jar1: 3 Jar2: 1 (ie., refill Jar 1 with 3 liters) Jar1: 0 Jar2: 4 (ie., pour 3 liters from Jar 1 to Jar 2) END (as we have measured 4 liters in one of the jars)

Please note that the above is only a sample and the input may vary. Please create a new repository in GitHub (or BitBucket) and check-in the source with an appropriate README file.
