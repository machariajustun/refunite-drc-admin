from unittest.case import TestCase

from shapely.geometry.multipolygon import MultiPolygon

from refunite_drc_admin.territories import Territories


class TestTerritories(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.territories = Territories()

    def test_parse(self):
        self.assertTrue(self.territories._territories)

        territory = self.territories._territories[0]
        self.assertIsInstance(territory._geom, MultiPolygon)
        self.assertIsInstance(territory.bounds, tuple)

        properties = territory.properties
        self.assertEqual(properties['admin1_nam'], 'Tshopo')
        self.assertEqual(properties['admin1_pco'], 'COD51')
        self.assertEqual(properties['admin2_nam'], 'Isangi')
        self.assertEqual(properties['admin2_pco'], 'COD5105')
        self.assertEqual(properties['admin3_nam'], 'Yalihila')
        self.assertEqual(properties['admin3_alt'], 'Yalikila (Yalihilo)')
        self.assertEqual(properties['admin3_pco'], 'COD510513')

    def test_find(self):
        matched_territories = self.territories.find(29.1811337, -1.6587838)
        self.assertEqual(len(matched_territories), 1)
        territory = matched_territories[0]

        self.assertEqual(territory.properties['admin1_nam'], 'Nord-Kivu')
        self.assertEqual(territory.properties['admin2_nam'], 'Goma')
        self.assertEqual(territory.properties['admin3_nam'], 'Goma')
        self.assertEqual(territory.properties['admin3_alt'], None)

    def test_find_three_results(self):
        matched_territories = self.territories.find(24.534625, 0.716924)
        self.assertEqual(len(matched_territories), 3)

    def test_find_empty(self):
        matched_territories = self.territories.find(0, 0)
        self.assertEqual(len(matched_territories), 0)
