import io
import logging
import os

import geojson
from shapely.geometry import shape, Point

from refunite_drc_admin import data
from refunite_drc_admin.territory import Territory

log = logging.getLogger(__name__)


class Territories(object):

    def __init__(self):
        log.info('Loading territories')
        territories_geojson = self._load_as_geojson()
        self._territories = self._parse(territories_geojson)
        log.info('Loading territories has finished')

    def find(self, lon, lat):
        point = Point(lon, lat)

        return [
            territory for territory in self._territories if territory.contains(point)
        ]

    def _load_as_geojson(self):
        file_path = os.path.join(
            os.path.dirname(os.path.realpath(data.__file__)),
            'drc_administrative_boundaries_levels_3.geojson')

        with io.open(file_path, encoding='utf-8') as data_file:
            lines = '\n'.join(data_file.readlines())
            return geojson.loads(lines)

    def _parse(self, territories_geojson):
        features = territories_geojson['features']

        return [
            Territory(shape(f['geometry']), f['properties'])
            for f in features
        ]
