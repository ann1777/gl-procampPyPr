import logging
import pytest

def SampleProviderFunction(request, db)
    yield from_SampleProvider(request, db)

@pytest.fixture(scope="class")
def SampleProviderClass(request, db):
    yield from_SampleProvider(request, db)

#base fixture
def _SampleProvider(request, db):
    def make_sample(*args, **kwargs):
        def fin():
            nonlocal sample
            logging.debug(f"HERE SHOULD COME SAMPLE REMOTE STEP FOR {sample}")
            sample=SamplesProvider.create sample(*args, **kwargs)
            return sample
        yield make_sample

@pytest.fixture(scope="function")
def SampleProviderFunction(request, db):
    yield from_SampleProvider(request, db)

@pytest.fixture(scope="class")
def SampleProviderClass(request, db):
    yield from_SampleProvider(request, db)