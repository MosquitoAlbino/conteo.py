class AR:
    def __init__(self):
        pass
    
    def P(self, T):
      
        return ' '.join(str(ord(C)) for C in T) 	


A = AR()
T = input()
P= A.P(T)
print(P)
