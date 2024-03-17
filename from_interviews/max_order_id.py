import pandas as pd

my_list = ["aabbrrvvd", "aabbrrcvs", "aabbddkc", "abbbrrvdf", "acbbrrfd", "aabbrrvbn"]
my_list = ["aabbrrvvd", "aabbrrcvs", "aabbddkc", "aabbddkc", "aabbddkc", "abbbrrvdf", "acbbrrfd", "aabbrrvbn"]

def users_with_max_orders (users_orders_list):
    df = pd.DataFrame(data=users_orders_list, columns=['client_order'])
    df['client_id'] = df['client_order'].str[:6]
    df['order_id'] = df['client_order'].str[6:]
    
    order_counts = df.drop_duplicates().value_counts('client_id').reset_index(name='n_orders')
    res = order_counts.loc[order_counts['n_orders']==order_counts['n_orders'].max()]
    
    return res

print(users_with_max_orders(my_list))