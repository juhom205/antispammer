import requests
import json
import names
import random
import string
import time

bad_url = "domain.com" # enter your domain of the spammer here
emails = ["gmail.com", "gmx.net", "web.de", "yahoo.com", "hotmail.com", "aol.com", "hotmail.co.uk", "hotmail.fr",
          "msn.com", "yahoo.fr", "wanadoo.fr", "orange.fr", "comcast.net", "yahoo.co.uk", "yahoo.com.br", "yahoo.co.in",
          "live.com", "rediffmail.com", "free.fr", "t-online.de", "protonmail.com", "googlemail.com", "outlook.com", "zoho.com"]
counter = 0


def send_random_request():
    global counter
    email = names.get_full_name().replace(" ", ".") + "@" + random.choice(emails)
    password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(8, 12)))
    payload = {"email": email, "password": password} # usually email and password is choosen the most time. check better the payload before you start
    result = requests.post(bad_url, allow_redirects=False, data=payload)
    counter += 1
    print(f"Sending No.{counter}: {email} and {password}")
    print(result)


if __name__ == "__main__":
    while True:
        send_random_request()
        time.sleep(random.randint(1, 1000) / 10)
