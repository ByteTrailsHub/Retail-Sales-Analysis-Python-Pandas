import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUT_DIR = BASE_DIR / "output"
OUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_DIR / "data_sales.csv")
df=df.drop(index=0)
df['revenue'] = df['units_sold'] * df['price']
df['gross_profit'] = (df['price'] - df['cost']) * df['units_sold']
df['gp_percent'] = (df['gross_profit'] / df['revenue']) *100

daily_summary = (
    df
    .groupby('date', as_index=False)
    .agg(total_revenue=('revenue', 'sum'))
)

category_check = (
    df
    .groupby('category', as_index=False)
    .agg(total_revenue=('revenue', 'sum'), total_gross_profit=('gross_profit', 'sum'))

)

category_check["total_gp_percent"] = (category_check["total_gross_profit"]/category_check["total_revenue"]) *100

daily_summary.plot(kind='line', x='date', y='total_revenue')
plt.savefig(OUT_DIR / "daily_revenue_trend.png", bbox_inches="tight")
plt.close()


sorted_check = category_check.sort_values(by='total_revenue', ascending=False)
sorted_check.plot(kind='bar', x='category', y='total_revenue')
plt.savefig(OUT_DIR / "category_revenue.png", bbox_inches="tight")
plt.close()

sorted_check2 = category_check.sort_values(by='total_gp_percent', ascending=False)
sorted_check2.plot(kind='bar', x='category', y='total_gp_percent')
plt.savefig(OUT_DIR / "category_gp_percent.png", bbox_inches="tight")
plt.close()


plt.close()
#print(df.head())
# print(daily_summary.head())
#print(category_check.head())
#print(sorted_check2.head())

daily_summary.to_csv(OUT_DIR /'daily_revenue_summary.csv', index=False)
sorted_check.to_csv(OUT_DIR /'category_performance_summary.csv', index=False)