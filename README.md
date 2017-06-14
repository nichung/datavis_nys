## data visualization: choropleth
visualizing American Community Survey data by census tract in NYS

JSON and d3 elements based on Mike Bostock's Command Line Cartography

### components:
+ EDA and munging with Python
+ JSON transformation with TopoJSON and ndjson-cli
+ Visualization with d3-geo

### todo:
+ ~~find or make NYC PUMAs with 'ALAND/ALAND10' (land area) & adjust project (geoConicConformal) if necessary~~
+ ~~integrate NYU's modified PUMAs to account for land-based boundaries~~
+ dictionary to JSON to avoid formatting error when turning CSV into JSON with pandas

### generate geojson in prep for d3:
1. generate CSV with relevant data. make sure 'id' strings have leading zeroes to match geoJSON 'id' strings
2. use 'sed' command to format CSV with quotes around strings (not headers)
3. use script to transform CSV to JSON-style object
4. inspect JSON-style object for formatting; use 'sed' command to remove trailing commas and save file as .ndjson
5. join data to geometry using 'ndjson-join' along 'd.id'
6. compute population density using 'ndjson-map' with constant '2589975.2356' to convert land area from m^2 to mi^2
	- convert resulting ndjson object back to geoJSON using 'ndjson-reduce' as FeaturesCollection to test
8. use 'ndjson-map' with d3 parameters to iterate and fine-tune the appropriate color scheme 
9. convert resulting ndjson object back to geoJSON and/or svg
10. move on to choropleth refinement:
	- is population uniformly distributed?
	- is color encoding effective in showing data?
	- title, key, additional geographic cues?
