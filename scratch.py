def fun(s):
    """return True if s is a valid email, else return False"""
    try:
        username, url = s.split('@')
        websites, extension = url.split('.')
    except ValueError:
        return False

    return username.replace('_', '').replace('-', '').isalnum() \
           & websites.isalpha() \
           & (0 < len(extension) <= 3)      # the () are very necessary here


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
