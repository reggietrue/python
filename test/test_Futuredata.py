import pytest


@pytest.mark.usefixtures("dataload")
class TestExample2:

    def test_editProfile(self,dataload):
        print(dataload)
        print(dataload[1])
        print(dataload[2])