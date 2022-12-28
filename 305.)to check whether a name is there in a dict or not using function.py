def STRDICT(d,s):
    for ch in d.values():
        if s == ch:
            print("Hello ",s)
            break
    else:
        a = s[0]
        d[a] = s
    print(d)
a = {"A" : "APOORVA","D" : "DEVANSH","K" : "KEYA"}
s = "VAIBHAVI"
STRDICT(a,s)
        
