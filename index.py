import pytest

@pytest.fixture
def credentials():
    email = "yash.raj021@gmail.com"
    username = "yash.raj021"
    domain = "gmail.com"

    return (email, username, domain)

def test_method_1(credentials):
    email = get_email(credentials[0])
    
    user_name = get_user_name(email)
    
    domain_name = get_domain_name(email)

    assert credentials[0] == email
    assert credentials[1] == user_name
    assert credentials[2] == domain_name


def get_email(email):

    return email

def get_user_name(email):
    
    user_name = email[:email.index("@")]
    
    return user_name

#Slicing out domain name

def get_domain_name(email):
    
    domain_name = email[email.index("@")+1:]
    
    return domain_name

def formatter(user_name, domain_name):

    result = f"Your username is:- '{user_name}' and domain name is:- '{domain_name}'"

    return result

