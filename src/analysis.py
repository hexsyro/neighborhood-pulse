import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')


def business_rareness(df):
    counts= df.groupby('city')['primary_cat'].value_counts()
    return counts.groupby(level=0).head()

def review_vs_rate(df):
    return df['review_count'].corr(df['stars'])


def rating_distribution(df):
    plt.scatter(df['review_count'], df['stars'], alpha=0.5)
    plt.xlabel('Number of reviews (log scale)')
    plt.ylabel('Star rating')
    plt.xscale('log')
    plt.title('Do Popular Florida Businesses Rate Higher? Not Really', loc='left', fontweight='bold')
    plt.tight_layout(pad=5)
    plt.savefig('outputs/rating_distribution.png', dpi=200, bbox_inches='tight')
    plt.show()
    plt.close()

def city_compare(df):
    top4 = df['city'].value_counts().head(4).index
        
    fig, axes = plt.subplots(2, 2, figsize=(15, 10), sharey=True)
    axes = axes.flatten()
    fig.supxlabel('Share of businesses')
    fig.suptitle('Restaurants Lead the Business Mix in Every Florida City Studied',
                x=0.01, ha='left', fontsize=16, fontweight='bold')

    for name, ax in zip(top4, axes):
        subset = df[df['city'] == name]
        subset['primary_cat'].value_counts(normalize=True).plot(kind='bar', ax=ax)
        ax.tick_params(axis='x', rotation=65)
        ax.set_title(name)
        ax.set_xlabel(None)
        ax.set_ylabel('Normalized business count')

    plt.tight_layout(pad=5)
    plt.savefig('outputs/business_categories.png', dpi=200, bbox_inches='tight')
    plt.show()
    plt.close()

def main():    
    df=pd.read_csv('data/processed/business.csv')
    print("Which business categories dominate the city, and which are rare?: ")
    print(business_rareness(df))
    print()
    print("Do highly-reviewed businesses actually rate better, or is there no relationship?: ")
    print(f" there is a some kind of a relationship with {review_vs_rate(df)} of a correlation")
    print()
    print("How are ratings distributed overall with stars?: ")
    rating_distribution(df)
    print("saved business rating distribution report by reviews into 'outputs/rating_distribution.png'")
    print()
    print("How do two neighborhoods or two cities compare on all of the above?: ")
    city_compare(df)
    print("saved business category report by example 4 cities into 'outputs/business_categories.png'")


if __name__ == '__main__':
    main()