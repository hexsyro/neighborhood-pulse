import pandas as pd


def filter_cities(df,florida_cities):
    df1=df.loc[df['city'].isin(florida_cities), ['name','city','categories','stars','review_count','is_open']].reset_index(drop=True).dropna()
    return df1


def get_primary_category(df,primary_categories):
    def get_prime_cat(categories, primary_categories):
        for cat in categories.split(','):
            cat=cat.strip()
            if cat in primary_categories:
                return cat
        return 'other'
    df['primary_cat']=df['categories'].apply(get_prime_cat, args=(primary_categories,))
        
    df.to_csv('data/processed/business.csv', index=False)
    return df[['name','primary_cat','categories']]

def main():    
    df=pd.read_json('data/raw/yelp_academic_dataset_business.json', lines=True)

    florida_cities = [
        "Jacksonville",
        "Miami",
        "Tampa",
        "Orlando",
        "St. Petersburg",
        "Hialeah",
        "Tallahassee",
        "Port St. Lucie",
        "Cape Coral",
        "Fort Lauderdale",
        "Pembroke Pines",
        "Hollywood",
        "Gainesville",
        "Miramar",
        "Coral Springs",
        "Clearwater",
        "Palm Bay",
        "Lakeland",
        "Pompano Beach",
        "West Palm Beach",
        "Davie",
        "Miami Gardens",
        "Boca Raton",
        "Deltona",
        "Sunrise",
        "Plant City",
        "Sanford",
        "Kissimmee",
        "Daytona Beach",
        "Ocala",
        "Sarasota",
        "Naples",
        "Fort Myers",
        "Bradenton",
        "Melbourne",
        "Pensacola",
        "Destin",
        "Panama City",
        "Key West",
        "Fort Pierce",
        "Vero Beach",
        "Winter Haven",
        "Clermont",
        "Apopka",
        "Titusville",
        "St. Augustine",
        "The Villages"
    ]

    primary_categories = [
        'Restaurants', 'Food', 'Shopping', 'Home Services',
        'Automotive', 'Beauty & Spas', 'Health & Medical',
        'Active Life', 'Nightlife', 'Hotels & Travel',
        'Event Planning & Services', 'Local Services'
        ]
    
    print("======== LOADING DATASET ========")
    df1 = filter_cities(df, florida_cities)
    print("filtered Yelp dataset data to Florida business data.")
    print()
    
    print("======== DEFINING PRIMARY CATEGORY ========")
    get_primary_category(df1, primary_categories)
    print("writed primary categories for Florida business data into 'data/processed/business.csv'")


if __name__ == '__main__':
    main()