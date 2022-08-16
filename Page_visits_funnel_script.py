import pandas as pd
##Funnel for Cool T-Shirts Inc.

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
#Inspecting the DataFrames using print and head
print(visits.head())
print(cart.head())         
print(checkout.head()) 
print(purchase.head())

#Combining visits and cart using a left merge.
visits_cart_left = pd.merge(visits, cart, how='left')

#How long is the merged DataFrame?
print(len(visits_cart_left))

#How many of the timestamps are null for the column cart_time?
print(visits_cart_left.cart_time.isna().sum())

#What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
perc_visits_cart = ((visits_cart_left.cart_time.isna().sum())/len(visits_cart_left))*100
print(perc_visits_cart)

#What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout_left = cart.merge(checkout, how = 'left')

print(cart_checkout_left.head())
print(cart_checkout_left.shape[0])
print(cart_checkout_left.checkout_time.isna().sum())
perc_cart_checkout = (cart_checkout_left.checkout_time.isna().sum())/(cart_checkout_left.shape[0])*100
print(perc_cart_checkout)

#Merging all four steps of the funnel, in order, using a series of left merges
all_data = visits.merge(cart, how = 'left').merge(checkout, how = 'left').merge(purchase, 'left')

print(all_data.head())

#What percentage of users proceeded to checkout, but did not purchase a t-shirt?
print(len(all_data))
print(all_data.purchase_time.isna().sum())
perc_checkout_purchase = (all_data.purchase_time.isna().sum()/len(all_data))*100
print(perc_checkout_purchase)

#Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?
print(perc_visits_cart) #82.6
print(perc_cart_checkout) #25.311203319502074
print(perc_checkout_purchase) #79.04721753794266

##Average Time to Purchase

#let’s calculate the average time from initial visit to final purchase. Add a column that is the difference between purchase_time and visit_time.

all_data['time_to_purchase'] = all_data['purchase_time'] - all_data['visit_time']

print(all_data.head())
print(all_data.time_to_purchase.mean()) #0 days 00:43:53.360160


#RdEl00
