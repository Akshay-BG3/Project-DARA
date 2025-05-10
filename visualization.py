import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# Function to generate a histogram for a selected column
def generate_histogram(df, column):
    fig = plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True)
    return fig

# Function to generate a scatter plot for selected columns
def generate_scatter_plot(df, x_column, y_column):
    fig = plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x_column, y=y_column)
    return fig

# Function to generate a heatmap of correlations for numeric columns
def generate_heatmap(df):
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    corr = df[numeric_columns].corr()
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt='.2f')
    return fig

# Function to generate a box plot for a selected column
def generate_box_plot(df, column):
    fig = plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, y=column)
    return fig

def generate_scatter_plot(df, x_column, y_column):
    fig, ax = plt.subplots()
    ax.scatter(df[x_column], df[y_column], alpha=0.7)
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f"Scatter Plot of {x_column} vs {y_column}")
    return fig