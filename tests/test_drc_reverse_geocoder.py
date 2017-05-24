from unittest.case import TestCase

from refunite_drc_admin import DrcReverseGeoCoder


class TestDrcReverseGeoCoder(TestCase):

    def test_get_territories(self):
        drc_reverse_geocoder = DrcReverseGeoCoder()
        territories = drc_reverse_geocoder.get_territories(29.1811337, -1.6587838)

        self.assertEqual(len(territories), 1)
        territory = territories[0]
        self.assertEqual(territory.properties['admin1_nam'], 'Nord-Kivu')
        self.assertEqual(territory.properties['admin2_nam'], 'Goma')
        self.assertEqual(territory.properties['admin3_nam'], 'Goma')
        self.assertEqual(territory.properties['admin3_alt'], None)
