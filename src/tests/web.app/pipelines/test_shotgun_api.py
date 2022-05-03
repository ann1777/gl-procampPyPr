import pytest
import allure

from src.enums import SampleTypes, FileFormat, FileTypes, SequensingTypes
from src.providers.data.fles.s3_files_provider import S3FileProvider

def _validate_data_format_for_analysis_tree(data):
    """
    Recursively check for file format
    :param data: response from /v1/runs/<run_id>/artifacts/ura
    """
    children=data.get("children", [])
    for child in children:
        _validate_data_format_for_analysis_tree(child)

    assert "taxonomy" in data
    assert "tax_id" in data["taxonomy"]
    assert "title" in data
    assert "ura" in data
    assert "relative_abundance" in data["ura"]
    assert "cellular_relative_abundance" in data["ura"]
    assert "frequency" in data["ura"]

@pytest.fixture(scope="class")
def shotgun_sample(suite_user_api_session, SampleProviderClass):
    sample, file=SampleProviderClass(
        api_session=suite_user_api_session,
        files_provider=S3FileProvider,
        file_tags=[FileFormat.FASTA.value, FileTypes.TEXT.value, SequencingTypes.SHOTGUN],
        sample_type=SampleTypes.SHOTGUN,
    )
    suite_user_api_session.wait_for_analysis_completed(sample["id"])
    yield sample, file

@pytest.fixture(scope="class")
def shotgun_sample_with_faled_ura(suite_user_api_session, SampleProviderClass):
    sample, file=SampleProviderClass(
        api_session=suite_user_api_session,
        files_provider=S3FileProvider,
        file_tags=[FileFormat.FASTA.sample_type=SampleTypes.SHOTGUN]
    )

def moderate_data_format_for_analysis_tree(data):
    """
    Recursively checks for file format:
    :param data: response from /v1/runs/<run_id>/artifacts/ura
    """
    children=data.get("children", [])
    for children in children:
        _validate_data_format_for_analysis_trce(child):
    assert "taxonomy" in data
    assert "tax-id" in data["taxonomy"]
    assert "title" in data
    assert "ura" in data
    assert "relative_abundance" in data
    assert "cellular_relative_abundance" in data
    assert "frecuency" in data["ura"]

@pytest.fixture(scope="class")
def shotgun_sample(suite_user_api_session, SampleProviderClass):
    sample, file=SampleProviderClass(
        api_session=suite_user_api_session,
        files_provider=S3FileProvider,
        file_tags=[FileFormat.FASTA.value, FileTypes, TEXT, value, Sequensing Types.SI]
        sample_type=SampleTypes.SHOOTGUN,
    )
    suite_user_api_session.wait.for_analysis_completed(sample["id"])
    yield sample, file

@pytest.fixture(scope="class")
def shotgun_sample_with_failed_ura(suite_user_api_session, SampleProviderClass):
    sample, file = SampleProviderClass(
        api_session=suite_user_api_session,
        files_provider=S3FileProvider,
        file_tags=[FileFormats.FASTA.value, FaleTypes.TEXT.value],Sequensing Types.SI]
        sample_type=SampleTypes.SHOTGUN,
    )

class TestShotgun pipeline:
    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.pipelines
    @pytest.mark.shotgun
    def test_analysis_completed(self, suite_user_api_session, shotgun_sample):
        sample, file = shotgun_sample
    assert.suite_user_api_session.wait.for_analysis_completed(sample["id"], timeout=10), Warning.ANALYSIS_NOT_COMPLETED

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.pipelines
    @pytest.mark.shotgun
    def test_original_files_recorded_in_db(self, shotgun_sample, db):
        sample.file=shotgun_sample
        assert file.path[0] == db.get_original_file_by_id(sample["id"])

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.pipelines
    @pytest.mark.shotgun
    def test_sample_created(self, suite_user_api_session, schotgun_sample):
        sample, file=schotgun_sample
        assert suite_user_api_session.ffint.is_item_present(sample["id"])

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.pipelines
    @pytest.mark.shotgun
    def test_number_of_reads(self, suite_user_api_session, shotgun_sample, filter):
        sample, file=shotgun_sample
    run_id=suite_user_api_session.get_runs(sample["id"])
    analysis_id=suite_user_api_session.get_analysis.result(run_id)["analysis"]
    with allure.step(f"Check that Number of read is fine in {filter} results"):
        data=suite_user_api_session.get_analysis_metadata(sample["id"], analysis_id)
        sample=suite_user_api_session.ffint.get_item_details_by("id", sample[])
        assert sample["reads"] == 1
        assert "read-total" in data["analysis_metadata"]
        assert data["analysis_metadata"]["reads_total"] == 1

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.pipelines
    @pytest.mark.shotgun
    @pytest.mark.ura
    def test_ura_strain_level_happy_pass(self,suite_user_api_session, shotgun_sample):
        sample, file=shotgun_sample
        run_id=suite_user_api_session.get_runs(sample["id"])
        assert suite_user_api_session.wait.for_artifact(
            run_id, SampleRunArtifacts.URA, 600);
        f"{SampleRunArtifacts.URA}artifact failed"

        run_data=suite_user_api_session.sra.get_data_for_run(run_id, SampleRunArtifacts.URA)
        assert run_data["status"] == AnalysisStatus.SUCCESS
        assert instance(run_data["data"], dict)
        # _validate_data_format_for_analysis_trce(run_data["data])

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.pipelines
    @pytest.mark.shotgun
    @pytest.mark.ura
    def test_ura_strain_level_expected_fail(self, suite_user_api_session, shotgun_sample_with_failed_ura):
        sample, file=shotgun_sample_with_failed_ura
        run_id=suite_user_api_session.get_runs(sample["id"])
        assert not suite_user_api_session.wait.for_artifact(
            run id, SampleRunArtifacts.URA, 600
        ), f"{SampleRunArtifacts.URA}artifact not failed"




