
def add_price_per_sqft(df,price,total_sqft):
    df['price_per_sqft'] = df[price]*100000/df[total_sqft]
    return df

def count_by_location_sorted(df):
    return df.groupby('location')['location'].agg('count').sort_values(ascending = False)

    