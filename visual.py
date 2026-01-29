from graph5 import *
import matplotlib.pyplot as plt

def draw_bar_chart():
     plt.bar(makes, avg_prices)
     plt.xlabel('Makes')
     plt.ylabel('Average Price')
     plt.xticks(rotation=45)
     plt.tight_layout()
     plt.show()

makes, sales, avg_prices = create_lists()

print("Makes",makes)
print("Sales",sales)
print("Average Price",avg_prices)