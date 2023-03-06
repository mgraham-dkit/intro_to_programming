def validate_email(email):
    if "@" in email and "." in email:
        email_components = email.split("@")
        if len(email_components[0]) > 0 and len(email_components[1]) >= 3:
            if "." in email_components[1]:
                dot_comps = email_components[1].split(".")
                if len(dot_comps[0]) > 0 and len(dot_comps[1]) > 0:
                    return True
    return False

email = "michelle@dkit.ie"
print(validate_email(email))