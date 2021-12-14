input = "D:\\GIT\\AdventOfCode2021\\Python\\Day1"
increases = 0
decreases = 0
debth_a = None


with open(input,"r") as f:
    for debth in f.readlines():
        if debth_a is None:
            debth_a = debth
        else:
            if int(debth_a) < int(debth):
                increases = increases + 1
            else:
                decreases = decreases + 1
        debth_a = debth

print("increases: ", increases)
print("decreases: ", decreases)