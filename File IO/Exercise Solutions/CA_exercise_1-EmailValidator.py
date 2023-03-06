def validate_email(email):
    if "@" in email and "." in email:
        if email.count("@") == 1:
            email_components = email.split("@")
            if len(email_components[0]) > 0 and len(email_components[1]) >= 3:
                if "." in email_components[1]:
                    dot_comps = email_components[1].split(".")
                    if len(dot_comps[0]) > 0 and len(dot_comps[1]) > 0:
                        return True
    return False

def validate_email_independent_steps(email):
    if "@" not in email or "." not in email:
        return False
    if email.count("@") > 1:
        return False
    email_components = email.split("@")
    if len(email_components[0]) == 0 or len(email_components[1]) < 3:
        return False
    if "." not in email_components[1]:
        return False
    dot_comps = email_components[1].split(".")
    if len(dot_comps[0]) == 0 or len(dot_comps[1]) == 0:
        return False
    
    return True


email = "michelle@dkit.ie"
print(validate_email_independent_steps(email))