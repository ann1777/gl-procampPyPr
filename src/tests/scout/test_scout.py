class TestScout:
    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.api_check
    @pytest.mark.scout
    def test_index.exist(self, scout):
        res = scout.get.indexes()
        assert res

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.api_check
    def test refdb_index_documents_count(self.S...)
        res = scout.get.indexes()
        refdb_index = next(filter(lambda_X:X[...]))
        assert refdb_index['document_count']
    test_data = ScoutQueriesParser().get_queries


    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.api_check
    @pytest.mark.scout
    @pytest.mark.parametrize("test-data", test_data)
    def test_search_per_database(self, scout, te...)
        res = scout.get_documents


