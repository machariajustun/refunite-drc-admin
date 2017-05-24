from refunite_drc_admin.territories import Territories


class DrcReverseGeoCoder(object):
    def __init__(self):
        """ Reverse geo-coder to find a DRC territory for a given coordinate.

        Example usage::

            drc_reverse_geocoder = DrcReverseGeoCoder()
            territories = drc_reverse_geocoder.get_territories(29.1811337, -1.6587838)
            print(territories[0]['admin3_nam'])
            # Goma

        It is recommend to cache the instance of `DrcReverseGeoCoder` so that the
        underlying geo-data is parsed only once.

        """
        self._territories = Territories()

    def get_territories(self, lon, lat):
        """ Returns the DRC territories the given location is in.

        Usually a single territory is returned. But if the location is at the border
        of a territory two or more territories might be returned.

        :param lon: Longitude (x).
        :type: lon: float
        :param lat: Latitude (y).
        :type: lat: float
        :return: A list of territories.
        :rtype: list of Territory
        """
        return self._territories.find(lon, lat)
