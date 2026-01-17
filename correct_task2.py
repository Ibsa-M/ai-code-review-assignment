def count_valid_emails(emails):
    if not isinstance(emails, list):
        return 0

    count = 0

    for email in emails:
        if isinstance(email, str):
            email = email.strip()

            if email.count("@") == 1:
                username, domain = email.split("@")

                if username and "." in domain:
                    count += 1

    return count
