# refunite-drc-admin
A reverse geo-coder that returns the DRC territories at a given location.

Example:

```python
from refunite_drc_admin import DrcReverseGeoCoder
drc_reverse_geocoder = DrcReverseGeoCoder()
territories = drc_reverse_geocoder.get_territories(29.1811337, -1.6587838)
print(territories[0]['admin3_nam'])
# Goma
```

It is recommend to cache the instance of `DrcReverseGeoCoder` so that the underlying geo-data is parsed only once.

## Dataset

The geo-data used for the reverse geo-coding is licensed under the
Open Database License (ODC-ODbL) license.
Source: [Referenciel Géographique Commun/OCHA DR Congo ](https://data.humdata.org/dataset/drc-administrative-boundaries-levels-0-3)

## Set up for development

Create a virtualenv:

    $ virtualenv env
    $ source env/bin/activate
    
Install the dependencies:

    (env) $ pip install -r requirements.txt
    
Run the tests:

    (env) $ bash run-tests.sh

Or use:

    $ tox

## License
MIT License
