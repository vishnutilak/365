
print ("Enter the places")


In = [float(x) for x in input().split()]


var2 = In[0]+In[1]

if In[0]>=1.8 and In[1]>=1.8:   
    if var2 >= 4.2:
                
                Out0 = In[1]*(In[0]-1)
                Out1 = In[0]*(In[1]-1)


                print ("Stake on A:",In[1]*1000)
                print ("Stake on B:",In[0]*1000)


                print  ("Profit on A is", Out0*1000)
                print  ("Profit on B is", Out1*1000)

                Out2 = (Out0-In[0])*1000
                Out3 = (Out1-In[1])*1000

                Out4 = (In[1]+In[0])*1000
                Out5 = (Out2/Out4)*100

                print ("Amount at stake", Out4)
                print ("Return to account if A wins:", Out2)
                print ("Return to account if B wins:", Out3)


                print ("Percentage of return:", Out5)
    else:
        print ("We won't get Any profit from this match stakes,\n But the Equation is yet to be modified,\n WORK ON IT")
else:
    print ("We won't get Any profit from this match stakes,\n But the Equation is yet to be modified,\n WORK ON IT")
