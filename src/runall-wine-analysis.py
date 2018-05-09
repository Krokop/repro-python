import importlib


subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

FILENAME = 'data/raw/winemag-data-130k-v2.csv'
country = 'Chile'


if __name__ == '__main__':
    new_data_filename = subset.process_data_GBP(FILENAME)
    print(new_data_filename)
    plot_filename = plotwines.create_plots(new_data_filename)
    country_file = country_sub.get_country(new_data_filename, country)
    print(country_file)