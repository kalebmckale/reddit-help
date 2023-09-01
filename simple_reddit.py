"""
Please help with this simple problem

At the beginning of the condition, which is the starting line (if)

The number entered must be between the number 3 and 5 and the entry (n3) is the number 1 and if 0 does not fulfill the condition complete and goes to achieve another

\------------------------------------------------------------------------------
"""

a = input("name:")
y = input("Age:")
z = input("Sex:")

# with open("c19.txt", "w") as x:
print("**Notice 1 mean yes, 0 mean no.** ")

def sum(Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9):  
    q = (Q1 + Q2 + Q3 + Q4 + Q5 + Q6 + Q7 + Q8 + Q9)  
    if 3 <= q <= 5:
        
x = open("c19.txt", "w")  
x.write("name: " + a + "\\n" + "Age: " + y + "\\n""Sex: " + z + "\\n")  
x.write("Result:\\t"+"he/she must isolate him/her self for 14 days and do covid-19 test.")  
x.close()  
 elif q > 5:  
x = open("c19.txt", "w")  
x.write("name: " + a + "\\n" + "Age: " + y + "\\n""Sex: " + z + "\\n")  
x.write("Result:\\t"+"he/she must do covid-19 test, Maybe he/she infected by covid-19.")  
x.close()  
 elif q < 3:  
x = open("c19.txt", "w")  
x.write("name: " + a + "\\n" + "Age: " + y + "\\n""Sex: " + z + "\\n")  
x.write("Result:\\t"+"he/she must isolate him/her self for 5 days if no more symptoms show,then he/she are not infected.")  
x.close()  


n3 = (int)(input("if was in contact with an infected person:"))  
n4 = (int)(input("Do you have a fever:"))  
n5 = (int)(input("Do you have a cough:"))  
n6 = (int)(input("Do you have shortness of breath or difficulty breathing:"))  
n7 = (int)(input("Do you have Fatigue:"))  
n8 = (int)(input("Do you have muscle or body aches:"))  
n9 = (int)(input("Do you have a headache:"))  
n10 = (int)(input("Do you have a loss of taste or smell:"))  
n11 = (int)(input("Do you have a sore throat:"))  


sum(n3, n4, n5, n6, n7, n8, n9, n10, n11)
