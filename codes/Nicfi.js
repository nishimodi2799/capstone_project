var nicfi = ee.ImageCollection('projects/planet-nicfi/assets/basemaps/africa');
var AOI = ee.Geometry.Polygon(
        [[[30.02974258651884,-1.9843283372681868],
          [30.04399048080595,-1.9843283372681868],
          [30.04399048080595,-1.970260485681338],
          [30.02974258651884,-1.970260485681338]]]);
// Filter basemaps by date and get the first image from filtered results
var basemap= nicfi.filter(ee.Filter.date('2021-06-01','2021-07-01')).first();
var vis = {"bands":["R","G","B"],"min":64,"max":5454,"gamma":1.8};
Map.addLayer(basemap.clip(AOI), vis, '2021-03 mosaic');
Map.centerObject(basemap.clip(AOI),14)
Map.addLayer(
    basemap.normalizedDifference(['N','R']).rename('NDVI'),
    {min:-0.55,max:0.8,palette: [
        '8bc4f9', 'c9995c', 'c7d270','8add60','097210'
    ]}, 'NDVI', false);
Export.image.toDrive({
  image: basemap.clip(AOI),
  description: 'nicfi',
  region: AOI,
  scale: 1,
  'crs':'EPSG:3857',
  folder: 'GEE'
});
