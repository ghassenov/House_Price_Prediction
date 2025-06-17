import matplotlib.pyplot as plt
import matplotlib


def plot_scatter_chart(df, location):
    bhk2 = df[(df.location == location) & (df.bhk == 2)]
    bhk3 = df[(df.location == location) & (df.bhk == 3)]
    matplotlib.rcParams["figure.figsize"] = (15, 10)
    plt.scatter(bhk2.total_sqft, bhk2.price, color="blue", label="2 BHK", s=50)
    plt.scatter(
        bhk3.total_sqft, bhk3.price, marker="+", color="green", label="3 BHK", s=50
    )
    plt.xlabel("Total Square Feet Area")
    plt.ylabel("Price (Lakh Indian Rupees)")
    plt.title(location)
    plt.legend()


def plot_pp_sqft_count(df):
    matplotlib.rcParams["figure.figsize"] = (20, 10)
    plt.hist(df.price_per_sqft, rwidth=0.8)
    plt.xlabel("Price Per Square Feet")
    plt.ylabel("Count")
