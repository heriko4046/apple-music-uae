import requests as r
import os
from fake_useragent import UserAgent
import threading

class AppleUAE:
    def __init__(self):
        self.api = r.Session()
        self.ua = UserAgent()

    def claimVOC(self):
        headers = {
            'User-Agent': self.ua.random,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'captcha': '03AFcWeA5yTKdbD6Yjssbb4652cWIdDAGND3oHBImmemGRA-PujQNq-yKiMNrZqqgJsAUaRDNNXxl4FcoTYdyCaoYRq_nssC-t5gWFy3lUgxBTJdj828W8XfRQURB6c3eU3ZqnwZAKSTLkEfY_tbBWoebhXgmULpwkn3klOOZHncTpVe-yrWEW0gWLUeK0frE8mpEudKwi-nK-qNhsrrh8RkuXEk0Oe7anprbrxzIIKtdZXAF7V7vPnXwdoWqwS0xYVOA_z6pAcV_ROcWIMQyDtihrfD-bkJZCTNJqTYiN7jKR3PqrC2e3w3_pSn0O0bldh8YG0kvad2P0Hi6_vjHdOYo1X7bokb2iBcTw-ygLGS9ZOVeNRY7TcFica2hI4DbvlwDWGV3E8vQcGSvCLRGsq6W--EocQZieQNf63wHgKjFAcwJMhwaWVDdEX8-r7xZYmg-iYiFyCDg-GJPPNDKPMGsffoK2sLDUMGfRKPL7q_iyUy-mg91EDuEPX4D8fowMp3hVqJ_ExoEwQynG0jMioUNgrLe0ig95APHHjUHjs6-p_b9RgZQUnZczlKPsN3IVHWoYia9vFaEWvX3dkyXj8AFC9zBHB3uPvw',
            'unique_id': '0b336f57-5dcd-46e5-857b-b3221754ec19',
            'api_endpoint': 'https://codemanager.apple.com/jwt/api/v1/campaigns/0b336f57-5dcd-46e5-857b-b3221754ec19/codes/vend',
            'secret_key': '8de71eedb4225c2db87d42edffc46dfd0fd126f51b8ad740f602998cafd4a01a68f7e9cfcfbb52b63ae1a10558e96ff2acc961f200595698e1a18f2b07bd4aff',
            'referral_token': ''
        }

        response = self.api.post('https://istyle.ae/appleservices/endpoint/ajaxcall/', headers=headers, data=data)
        return response

    def create_thread(self, amount):
        try:
            threads = []
            count = 0

            while count < int(amount):
                thread = threading.Thread(target=self.claim_and_print_response)
                threads.append(thread)
                thread.start()
                count += 1

            for thread in threads:
                thread.join()

        except KeyboardInterrupt:
            pass

    def claim_and_print_response(self):
        response = self.claimVOC()
        if 'code' in response.text:
            data = response.json()
            codee = data['code']
            print(response.text)
        with open('applemusicuae.txt', 'a') as file:
            file.write(response.text + '\n')

if __name__ == "__main__":
    os.system('cls')
    apple_uae = AppleUAE()
    amount = input(">> Amount: ")
    if int(amount) > 50:
        print('[!] May Cause a Crash!')
    apple_uae.create_thread(amount)
