import requests
import json
import pandas as pd

site = "https://shop.doverstreetmarket.com/" # Enter your desired Shopify site
for i in range (1,2) :
  url = f'{site}products.json?limit=250&page={i}'
  
  r = requests.get(url)
  
  data = r.json()
  
  product_list =[]
  
  for item in data['products'] : 
      title = item['title']
      handle = item['handle']
      created = item['created_at']
      product = item['product_type']
      for variant in item['variants'] : 
          price = variant['price']
          sku = variant['sku']
          id = variant['id']
          product_id = variant['product_id']
          available = variant['available']
  
  
      product =  {'title' : title,
                  'handle' : handle,
                  'created' : created,
                  'price': price,
                  'id' : id,
                  'product_id' : product_id,
                  'sku': sku,
                  'available': available,
      }
      product_list.append(product)
  
  df = pd.DataFrame(product_list)
  df.to_csv(f'{site}.csv')
  
