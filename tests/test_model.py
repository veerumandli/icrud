from src.models.Url import Url
import unittest


class TestUrlModel(unittest.TestCase):

    def setUp(self):
        self.url = Url()

    def test_instance_creation(self):
        self.assertIsInstance(self.url, Url)

    def test_create_returns_id(self):
        data = {'url': 'http://example.com'}
        record_id = self.url.create(**data)
        self.assertIsNotNone(record_id)
        self.assertIsInstance(record_id, int)

    def test_all_returns_list(self):
        records = self.url.all()
        self.assertIsInstance(records, list)

    def test_find_returns_record(self):
        data = {'url': 'http://example.com'}
        record_id = self.url.create(**data)
        record = self.url.find(record_id)
        self.assertIsNotNone(record)
        self.assertEqual(record['url'], 'http://example.com')


if __name__ == "__main__":
    unittest.main()
