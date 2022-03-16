
#DEFINING THE FUNCTION 
def minimumDistances(a):
    # Variable to save a value and it's last occurence position
    valuePositions = dict();
    #Intialize the minDistance to the maximum
    minDistance = len(a);

    for i in range(len(a)):
    # If the value has  already been saved in valuePositions, take it's last occurence position to calculate the distance 
        if (a[i] in valuePositions):
            if(i - valuePositions[a[i]] < minDistance):
                minDistance=i - valuePositions[a[i]];
                if(minDistance==1):
                    # 1 is the minimum distance possible
                    break
        #Update the value last occurence position in Valueposition dictionnary
        valuePositions[a[i]] = i;
    #return the minimum distance found 
    if(minDistance<len(a)):
        return minDistance
    else:
        return -1

#TESTING THE FUNCTION

n=int(input(''));
a=list(map(int,input('').strip().split()));
print(minimumDistances(a));

