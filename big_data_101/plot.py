import matplotlib.pyplot as plt

def plot_top_selling_products(df):
    """Plot the top 10 highest selling products."""
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df['product_id'], df['sales'], color='skyblue')
    plt.xlabel('Product ID')
    plt.ylabel('Sales')
    plt.title('Top 10 Highest Selling Products')
    plt.xticks(rotation=45)
    plt.tight_layout()
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', 
                ha='center', va='bottom', fontsize=10)
    
    plt.savefig('big_data_101/plot/top_ten_highest_selling_products.png', bbox_inches='tight')
    # plt.show()
