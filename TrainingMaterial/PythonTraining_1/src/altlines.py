'''
@author: cquiroz
'''

if __name__ == '__main__':
    pass

with open (r"C:\eclipse_workspace\pyberry3\DATA\alt.txt") as F:
    with open(r"C:\eclipse_workspace\pyberry3\DATA\a.txt", "w") as a:
        with open(r"C:\eclipse_workspace\pyberry3\DATA\b.txt", "w") as b:
            for line in F:
                if line.startswith("a"):
                    a.write(line)
                    print(a)
                elif line.startswith("b"):
                    b.write(line)
                    print(b)
        
        
