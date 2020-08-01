# --------------
#Code starts here
def palindrome(num):
    if num<9:
        return num+1
    else:
        while(str(num)!=str(num)[::-1]):
            num=num+1
        return num    


# --------------
#Code starts here
def a_scramble(str_1,str_2):
    str_1=str_1.upper()
    str_1=list(str_1)
    str_1.sort()
    str_2=str_2.upper()
    str_2=list(str_2)
    str_2.sort()
    str_3=str_2.copy()
    if str_1==str_2:
        return True
    else:
        for i in str_2:
            if i in str_1:
                x=str_2.count(i)
                y=str_1.count(i)
                if x<=y:
                    for j in range(x):
                        str_3.remove(i)
                else:
                    return False
                    break
        if len(str_3)==0:
            return True
        else:
            return False
         



    





# --------------
#Code starts here

def check_fib(num):
    x=5*pow(num,2)+4
    y=5*pow(num,2)-4
    #print(x,y)
    #print(pow(round(pow(x,1/2),2),2) ,pow(round(pow(y,1/2),2),2) )
    if x==pow(round(pow(x,1/2),2),2) or y==pow(round(pow(y,1/2),2),2):
        return True
    else:
        return False


# --------------
#Code starts here
def compress(word):
    count=1
    x=[]
    for i in range(1,len(word)):
        if i==(len(word)-1):
            if word[i-1]==word[i] or word[i-1]==word[i].lower() or word[i-1]==word[i].upper():
                count=count+1
                x.append(word[i])
                x.append(str(count))
            elif word[i-1]!=word[i] or word[i-1]!=word[i].lower() or word[i-1]!=word[i].upper():
                x.append(word[i-1])
                x.append(str(count))
                count=1
                x.append(word[i])
                x.append(str(count))
        else:
            if word[i-1]==word[i] or word[i-1]==word[i].lower() or word[i-1]==word[i].upper():
                count=count+1
            elif word[i-1]!=word[i] or word[i-1]!=word[i].lower() or word[i-1]!=word[i].upper():
                x.append(word[i-1])
                x.append(str(count))
                count=1
            

    return "".join(x)


# --------------
#Code starts here
def k_distinct(string,k):
    string=string.upper()
    string=list(string)
    string.sort()
    str2=string.copy()
    for i in range(len(string)-1):
	    if string[i]==string[i+1]:
		    str2.remove(string[i])

    if len(str2)==k:
        return True
    else:
        return False



