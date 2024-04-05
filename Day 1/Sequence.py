# Sir code
""" input_n=3
input_list=list(map(int,input().split(",")))[:input_n]
print(input_list)

if 7 in input_list:
    index_7=input_list.index(7)
    
    if index_7==input_n-1:
        print(-1)
    else:
        mul=1
        for i in input_list[index_7+1:]:
            mul*=i
        print(mul)
else:
    mul=1
    for i in input_list:
        mul*=i
    print(mul) """
    
# Jayu code

listo = [3,7,2 ]
value = 1
val = 1


if(7 in listo):
    s1 = listo.index(7)
    s2 = len(listo) - 1
    if(s1 == s2):
        print("-1")
    else:
        for i in listo[s1+1:]:
            val *= i;
        print("my Ans is ",  val)

elif(7 not in listo):
    for i in listo:
        val *= i;
    print("my Ans is ",  val)


else:
    print("error")