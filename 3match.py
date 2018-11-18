
print ("Enter the places")


In = [float(x) for x in input().split()]

var2 = In[0]+In[1]+In[2]

if In[0] >=2.2 and In[1]>=2.2 and In[2]>=2.2:

    if var2 >=9.0:
            
        Out0 = In[1]*In[2]
        Out1 = In[0]*In[2]
        Out2 = In[0]*In[1]

        print ("Stake on A:", (Out0)*1000, "Stakes Ratio:", Out0)
        print ("Stake on X:", (Out1)*1000, "Stakes Ratio:", Out1)
        print ("Stake on B:", (Out2)*1000, "Stakes Ratio:", Out2)

        print ("Profit on A is:", (Out0*(In[0]-1))*1000)
        print ("Profit on X is:", (Out1*(In[1]-1))*1000)
        print ("Profit on B is:", (Out2*(In[2]-1))*1000)

        Out3= (Out0+Out1+Out2)*1000

        print ("Amount at Stake",Out3)

        print ("Return on A:",((Out0*(In[0]-1))-Out1-Out2)*1000)
        print ("Return on X:",((Out1*(In[1]-1))-Out0-Out2)*1000)
        print ("Return on B:",((Out2*(In[2]-1))-Out0-Out1)*1000)

        vartotal = ((((Out0*(In[0]-1))-Out1-Out2)/(Out0+Out1+Out2))*100)

        print ("Percentage of return:",vartotal)
        
    else:
        print ("We won't get Any profit from this match stakes,\n But the Equation is yet to be modified,\n WORK ON IT")
else:
    print ("We won't get Any profit from this match stakes,\n But the Equation is yet to be modified,\n WORK ON IT")
