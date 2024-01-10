# Dictionary

def run01():
    my_dict = {
        'A':'Assumption',
        'B':'University',
        'C':1250
    }
    print(my_dict['A'])

def run01(abac):
    my_dict = {
        'A':'Assumption',
        'B':'University',
        'C':1250
    }
    return my_dict[abac]
print(run01('C'))