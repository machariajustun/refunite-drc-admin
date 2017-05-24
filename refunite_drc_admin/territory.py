class Territory(object):
    def __init__(self, geom, properties):
        """ A DRC territory.

        The following properties are available:

            - admin1_nam
            - admin1_pco
            - admin2_nam
            - admin2_pco
            - admin3_nam
            - admin3_alt
            - admin3_pco

        :param geom: The territory shape.
        :type: shapely.geometry.Polygon|shapely.geometry.MultiPolygon
        :param properties: Properties of the territory.
        :type: dict
        """
        self._geom = geom
        self._properties = properties

    def contains(self, point):
        """ Returns true if the given point is within the shape of
         the territory.

        :param point:
        :type: shapely.geometry.Point
        :return: True or False
        :rtype: bool
        """
        return self._geom.intersects(point)

    @property
    def bounds(self):
        return self._geom.bounds

    @property
    def properties(self):
        return self._properties.copy()
