import re

input_file_name = "clean-input.txt"
valid_count = 0

def validate_byr(line):
    print("BYR "+line)
    if int(line[4:]) >= 1920 and int(line[4:]) <= 2002:
        print("good")
        return True
    else:
        print("bad")
        return False

def validate_iyr(line):
    print("IYR "+line)
    if int(line[4:]) >= 2010 and int(line[4:]) <= 2020:
        print("good")
        return True
    else:
        print("bad")
        return False

def validate_eyr(line):
    print("EYR "+line)
    if int(line[4:]) >= 2020 and int(line[4:]) <= 2030:
        print("good")
        return True
    else:
        print("bad")
        return False

def validate_hgt(line):
    print("HGT "+line)
    if line[-2:] == "cm" and int(line[4:-2]) >= 150 and int(line[4:-2]) <= 193:
        print("good")
        return True
    elif line[-2:] == "in" and int(line[4:-2]) >= 59 and int(line[4:-2]) <= 76:
        print("good")
        return True
    else:
        print("bad")
        return False

def validate_hcl(line):
    print("HCL "+line)
    charRe = re.compile(r'[^a-zA-Z0-9]')
    if line[4:5] == "#" and len(line) == 11 and not charRe.search(line,5):
        print("good")
        return True
    else:
        print("bad")
        return False

def validate_ecl(line):
    print("ECL "+line)
    if line[4:] in ("amb","blu","brn","gry","grn","hzl","oth"):
        print("good")
        return True
    else:
        print("bad")
        return False

def validate_pid(line):
    print("PID "+line)
    charRe = re.compile(r'[^0-9]')
    if len(line[4:]) == 9 and not charRe.search(line,4):
        print("good")
        return True
    else:
        print("bad")
        return False

def validate_cid(line):
    return True


def validate_fields(line):
    success = True
    switcher = {
        "byr:": validate_byr,
        "iyr:": validate_iyr,
        "eyr:": validate_eyr,
        "hgt:": validate_hgt,
        "hcl:": validate_hcl,
        "ecl:": validate_ecl,
        "pid:": validate_pid,
        "cid:": validate_cid
    }
    for str_field in line.split():
        func = switcher.get(str_field[:4])
        if not func(str_field):
            success = False
    return success      
        
def all_req_fields(line):
    # must contain 
    # byr (Birth Year)
    #iyr (Issue Year)
    #eyr (Expiration Year)
    #hgt (Height)
    #hcl (Hair Color)
    #ecl (Eye Color)
    #pid (Passport ID)
    #cid (Country ID)
    if line.find("iyr:") != -1 and line.find("eyr:") != -1 and line.find("hgt:") != -1 and line.find("hcl:") != -1 and line.find("ecl:") != -1 and line.find("pid:") != -1 and line.find("byr:") != -1:
        if validate_fields(line):
            print ("Valid: " + line)
            return True
    else:
        print("Not valid: " + line)
        return False

for line in open(input_file_name):
    if all_req_fields(line):
        valid_count += 1
print("Valid count: "+str(valid_count))