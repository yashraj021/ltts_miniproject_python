
# Get the use e-mail address
email = input("Enter your E-mail address: ").strip()

#Slicing out username
user_name = email[:email.index("@")]

#Slicing out domain name
domain_name = email[email.index("@")+1:]

#Format message
result = f"Your username is:- '{user_name}' and domain name is:- '{domain_name}'"

#Priniting result
print(result)