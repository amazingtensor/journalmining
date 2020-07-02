from django.test import TestCase
from elasticsearch import Elasticsearch


class ElasticSearchTestCase(TestCase):
    def setUp(self):
        self.es = Elasticsearch()

    def test_es_create_delete_index(self):
        index_name = "test-index"
        # ignore 400 cause by IndexAlreadyExistsException when creating an index
        response = self.es.indices.create(index=index_name, ignore=400)
        self.assertTrue(response['acknowledged'])

        response = self.es.indices.delete(index=index_name, ignore=[400, 404])
        self.assertTrue(response['acknowledged'])