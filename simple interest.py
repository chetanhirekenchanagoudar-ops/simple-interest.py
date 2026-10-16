def simple_interest(principle,rate,time);
    return(principle*rate*time)/100
if__name__=="__main__"
p = int(sys.argv[1])
i = int(sys.argv[2])
t = int(sys.argv[3])
print("simple interest:",simple_interest(p,i,t))
