s=[root]
def itr2():
    if len(s)==0:
        return 0
    x=s[0]
    s.pop(0)
            
    if x==None:
        itr2()
                
    s.append(x.left)
    s.append(x.right)
            
                
    itr2()
        
