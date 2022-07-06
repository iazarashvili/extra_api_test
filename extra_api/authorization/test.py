import requests
import json

url = "https://basket.staging.extra.ge/v1/basket/updatebasket?requestId=85ed15a0-47a8-870a-0ae9-99801751432a"

payload = json.dumps({
  "productId": 400223,
  "discountType": {
    "id": 400223,
    "imageUrl": "https://cdn.staging.extra.ge/dyn/y0Nw-O_b-_jd1wpsZx_VWcfpda9l8LvQBZxFEdSftIA/bg:fff/rs:fit:220:0/plain/images/products/original/0771087e-37b4-4b70-96b9-429677f996e4.jpg@jpg",
    "imageName": "0771087e-37b4-4b70-96b9-429677f996e4.jpg",
    "title": "Hasbro მებრძოლი ბობლერები",
    "productSlug": "hasbro-mebrdzoli-boblerebi-400223",
    "productOriginalSlug": "hasbro-mebrdzoli-boblerebi",
    "categorySlug": "satamashoebi/satamasho-figurebi",
    "categoryOriginalSlug": "satamasho-figurebi",
    "sellerName": "Kidsroom • ქიდსრუმ",
    "sellPrice": 23,
    "discountPercent": None,
    "discountedPrice": None,
    "discountPeriodStartDate": "2021-11-25T20:00:00",
    "discountPeriodEndDate": "2021-11-30T20:00:00",
    "hasGift": None,
    "ageContentRestriction": False,
    "status": 0,
    "quantity": None,
    "hasInstallment": True,
    "merchantHasInstallment": True,
    "monthlyPayment": None,
    "fullData": False
  },
  "productCount": 1,
  "type": "[BASKET] UpdateBasket"
})
headers = {
  'authority': 'basket.staging.extra.ge',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9,ru;q=0.8,ka;q=0.7',
  'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjRBMEYxNkIzQjk0QkYzRUQxMDM2NjRENTk0RTYxMEJGOUJEMEQ2NURSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IlNnOFdzN2xMOC0wUU5tVFZsT1lRdjV2UTFsMCJ9.eyJuYmYiOjE2NTY1MzQ4MjYsImV4cCI6MTY1NzEzOTYyNiwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5zdGFnaW5nLmV4dHJhLmdlIiwiYXVkIjoiaWRlbnRpdHkiLCJjbGllbnRfaWQiOiJkZXYiLCJzdWIiOiI5YWYyMjVhYi1kNmNkLTQzYmYtYTdlYS01ZTE1MDMwOWNiNjAiLCJhdXRoX3RpbWUiOjE2NTY1MzQ4MjYsImlkcCI6ImxvY2FsIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiNDQ5NjQ1MWYtNTE5Yy00Y2Q0LWI1NjUtYjYwNzY0MjViZTExIiwiVXNlckV4dGVybmFsSWQiOiIyMzEyNzgiLCJlbWFpbCI6ImZlaGl0NjEzNTRAc2Vyb2hpdi5jb20iLCJlbWFpbF92ZXJpZmllZCI6WyJ0cnVlIiwiVHJ1ZSJdLCJwaG9uZV9udW1iZXJfdmVyaWZpZWQiOiJGYWxzZSIsIkxhc3ROYW1lIjoicnVtZSIsIkZpcnN0TmFtZSI6InJhbWUiLCJyb2xlIjoiQ3VzdG9tZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9kYXRlb2ZiaXJ0aCI6IjEvNy8yMDIxIDEyOjAwOjAwIEFNICswMDowMCIsImp0aSI6IkQ3NDkyRTNEQjgzNDc2M0E3NjY1QTVDMEU1NDA3QUUzIiwiaWF0IjoxNjU2NTM0ODI2LCJzY29wZSI6WyJhZGRyZXNzIiwiZW1haWwiLCJpZGVudGl0eSIsIm9wZW5pZCIsInBob25lIiwicHJvZmlsZSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJwd2QiXX0.SLX73L4yVA7uutFijQCYcFbJcVbbugSvbV9obPEZOOP9n5VRdq6UfY_EBkfsGAwpl-36bzVvXLXUPVFqx71Xe8RQrYvuo6jYoeNsKKLcHrujrrjd1c2CSSQShQz4D1uYdG4cXtm7N3g-kevO0QlaD5Yo-SxCJ2J6NSIxpaxRnt2Bzy5HeXuG_7nfHV7FuIFm9sSn0WcyqVtzSnimqS_IoamtW3LTVzDQMiucemb4WzIg_c8wxI_pbHuRyxY-ijkoTIhBaEuKS4So-wo381Sl_KXm3e3zKqVqbEdrlpO7-xMJf_DKbVZ_mH3zr_vshHjnGNisenl0DTA8MG_-IkDebg',
  'content-type': 'application/json',
  'dnt': '1',
  'origin': 'https://staging.extra.ge',
  'referer': 'https://staging.extra.ge/',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
