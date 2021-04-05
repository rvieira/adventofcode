input_file_name = "clean-input.txt"
valid_count = 0

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
        print ("Valid: " + line)
        return True
    else:
        print("Not valid: " + line)
        return False

for line in open(input_file_name):
    if all_req_fields(line):
        valid_count += 1
print("Valid count: "+str(valid_count))