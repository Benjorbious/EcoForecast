import kaggle
import numpy as np 
import pandas as pd 
import datetime as dt
import matplotlib.pyplot as plt, mpld3
import seaborn as sns
import folium
import geopandas as gpd
from IPython.display import HTML as html_print
from termcolor import colored

kaggle.api.authenticate()
kaggle.api.dataset_download_files('belayethossainds/renewable-energy-world-wide-19652022')
kaggle.api.dataset_metadata('belayethossainds/renewable-energy-world-wide-19652022', path = '.')
print('Data source import complete.')


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df_2 = pd.read_csv("renewable-energy-world-wide-19652022/02 modern-renewable-energy-consumption.csv")
df_2['Total Renewable Energy Generation - TWh'] = df_2['Solar Generation - TWh'] + df_2['Wind Generation - TWh'] + df_2['Hydro Generation - TWh'] + df_2['Geo Biomass Other - TWh']

df_2.head()
last_10_years_start = 2021 - 10

top_solar_countries_last_10_years = df_2[df_2['Year'] == 2021].nlargest(5, 'Solar Generation - TWh')

i = 6;
# for country in top_solar_countries_last_10_years['Entity']:
#     country_data_last_10_years = df_2[(df_2['Entity'] == country) & (df_2['Year'] >= last_10_years_start)]
#     plt.figure(figsize=(20, 8))
#     plt.plot(country_data_last_10_years['Year'], country_data_last_10_years['Solar Generation - TWh'], linewidth=3) 
#     plt.title(f'Solar Energy Generation in {country} (Last 10 Years) (TWh)', fontsize=18) 
#     plt.xlabel('Year', fontsize=14) 
#     plt.ylabel('Solar Generation (TWh)', fontsize=14) 
#     plt.grid(True)

#     saveFile = str(i) + '.png'
#     plt.savefig(saveFile)
#     i+=1

total_energy_by_year = df_2.groupby('Year').sum(numeric_only=True)

ax = total_energy_by_year.plot(y='Total Renewable Energy Generation - TWh', figsize=(20, 8), linewidth=3, title='')
# ax.set_title('Total Renewable Energy Generation by Year (TWh)', fontsize=18, fontweight='bold')
ax.set_xlabel('', fontsize=10, fontweight='bold')
ax.set_ylabel('', fontsize=10, fontweight='bold')
saveFile = str(i) + '.png'
plt.savefig(saveFile)
i+=1

solar_wind_hydro_geo_biomass_distribution = df_2.groupby('Year').sum(numeric_only=True)[['Solar Generation - TWh', 'Wind Generation - TWh', 'Hydro Generation - TWh', 'Geo Biomass Other - TWh']]

plt.figure(figsize=(20, 8))
plt.stackplot(solar_wind_hydro_geo_biomass_distribution.index, 
              solar_wind_hydro_geo_biomass_distribution['Solar Generation - TWh'], 
              solar_wind_hydro_geo_biomass_distribution['Wind Generation - TWh'], 
              solar_wind_hydro_geo_biomass_distribution['Hydro Generation - TWh'],
              solar_wind_hydro_geo_biomass_distribution['Geo Biomass Other - TWh'], 
              labels=['Solar', 'Wind', 'Hydro', 'Geo/Biomass/Other'], 
              colors=['yellow', 'blue', 'green', 'brown'], 
              alpha=0.6)
plt.title('', fontsize=15, fontweight='bold')
plt.xlabel('', fontsize=12, fontweight='bold')
plt.ylabel('', fontsize=12, fontweight='bold')
plt.legend(loc='upper left', fontsize=12)
saveFile = str(i) + '.png'
plt.savefig(saveFile)
i+=1