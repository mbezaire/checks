import check50
import random

def getrandinfo(arg):
    nums = []
    for i in range(8):
        nums.append(str(random.randint(0,255)))
    
    if arg % 2 == 0:
        i = 3
        ans = ".".join(nums[4:])
    else:
        i = 5
        ans = ".".join(nums[:4])
    
    nums[i] = str(int(nums[i]) + 256)
    with open("info.txt","w") as f:
        f.write(f'How many are in here? 12.124.32 and also {nums[0]}.{nums[1]}.{nums[2]}.{nums[3]} and lastly {nums[4]}.{nums[5]}.{nums[6]}.{nums[7]} hmm. Oh and 255.0.0.1')

    return ans + "\n255.0.0.1\n"

@check50.check()
def exists():
    """ Check that find.py exists """
    check50.exists("find.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors and finds a valid IP address"""
    ans = getrandinfo(2)
    out = check50.run("python find.py").stdout(timeout=30)
    check50.Mismatch(ans, out)

@check50.check(run)
def run2():
    """ Program finds another valid IP address"""
    ans = getrandinfo(1)
    out = check50.run("python find.py").stdout(timeout=30)
    check50.Mismatch(ans, out)

@check50.check(run2)
def usere():
    """ Program uses re's findall and for each loops without excessive logic"""
    with open('find.py') as f:
        content = f.read()
    ok = False
    if 'import re' in content and 're.findall' in content and 're.compile' in content:
        if content.count(' in ') >= 2 and content.count('for') >= 2:
            check = ''
            count = 0
            with open('find.py') as f:
                lines = f.readlines()
            for line in lines:
                if not line.strip().startswith('#') and len(line.strip()) > 1:
                    check += line
                    count += 1
            if count <= 20 and len(check) < 450:
                ok = True
    if not ok:
        raise check50.Failure("Your code may not be efficiently using the re module, for each loops, and join to achieve its functionality")
