import requests
from bs4 import BeautifulSoup

# url = 'https://www.amazon.in/dp/B08KGC4XW9/ref=sspa_dk_detail_5?psc=1&pd_rd_i=B08KGC4XW9&pd_rd_w=v8SVC&pf_rd_p=1801b34c-8af9-42b5-8961-11f124edc99b&pd_rd_wg=shL4C&pf_rd_r=CJ3D9PESTC556RZ5VR5A&pd_rd_r=c8702c94-fa05-48c4-a0c1-7581459b498f&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVlRHUVBOQjg4WkVCJmVuY3J5cHRlZElkPUEwMTY4NTg5MzMyQUREOTYzWlE2MSZlbmNyeXB0ZWRBZElkPUEwMDg2MTkxNDFMM1AwWjFTNVBTJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='  

url = input('Enter URL : ')
headers = {"User-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
page = requests.get(url, headers=headers)
soup  = BeautifulSoup(page.content, 'html5lib')

with open('amazon.html',"w", encoding='utf-8') as f:
    f.write(str(soup))

import pandas as pd
hdf = pd.read_html('amazon.html')

price = list(hdf[0][1])[1].split()[1]
print('\n', price)
