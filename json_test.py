# Reading data back / when working with STRINGS | method 1
nyc_json__file = open('/home/nchung/Workbench/datavis-A/PUMAs_nyc__2010/nyc.json')
nyc_json__str = nyc_json__file.read()
main_nyc_data = json.loads(nyc_json__str)

# Reading data back / when working with FILES | method 2
with open('/home/nchung/Workbench/datavis-A/data/cb_2013/ny_key.json', 'r') as f:
     misc_nyc_data = json.load(f)