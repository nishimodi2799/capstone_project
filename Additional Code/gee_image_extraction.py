import ee
nicfi = ee.ImageCollection('projects/planet-nicfi/assets/basemaps/africa')
a = 0.035
b = 0.035
i = 0
j = 0
Map = {}
for i in range(5):
    for j in range(5):
        AOI = ee.Geometry.Polygon([[[29.82036+(i)*a,-1.629857-(1+j)*b],
          [29.82036+(1+i)*a,-1.629857-(1+j)*b],
          [29.82036+(1+i)*a,-1.629857-j*b],
          [29.82036+(i)*a,-1.629857-j*b]]])
basemap = nicfi.filter(ee.Filter.data('2016-06-01','2016-07-01')).first()
vis = {"bands":["R","G","B"],"min":64,"max":5454,"gamma":1.8}
Map.addLayer(basemap.clip(AOI), vis, '2021-03 mosaic')
Map.centerObject(basemap.clip(AOI),14)
Map.addLayer(
basemap.normalizedDifference(['N','R']).rename('NDVI'),
      {min:-0.55,max:0.8,palette: [
        '8bc4f9', 'c9995c', 'c7d270','8add60','097210'
      ]}, 'NDVI', false)

task_config = {
    'description': 'nicfi_v1_2016',
    'scale': 1,  
    'region': AOI
    }

task = ee.batch.Export.image(GEE_new, 'nicfi_v1_2016', task_config)

task.start()

aoiArea=basemap.clip(AOI).geometry().area().divide(1000000);
print('AOI Area: ',aoiArea,"[km²]")