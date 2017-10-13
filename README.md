# djangorestframework-gis bug demonstration on DRF 3.6.4

## Instructions

Install this test application and `pip install -r requirements.txt`. If your env needs extra stuff for GeoDjango to work, add those.

Settings use SQLite3 with Spatialite, change as necessary to suit your environment. (Crucially, you may want to change or remove the `SPATIALITE_LIBRARY_PATH` setting, this is specific to my Mac with Spatialite from Homebrew.)

run `./manage.py runserver` and navigate to http://localhost:8000

POST a single feature, using the Raw data form, e.g.:

    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                25.87681499999997,
                65.45703099999999
            ]
        },
        "properties": {}
    }

The listing at http://localhost:8000/items/ should work.

The retrieval at http://localhost:8000/items/1/ should produce a KeyError for 'type'.