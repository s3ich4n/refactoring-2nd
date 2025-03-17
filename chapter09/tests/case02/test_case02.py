from chapter09.src.case02.case02 import Organization


def test_organization_initialization():
    org = Organization("Acme Gooseberry", "GB")
    assert org._name == "Acme Gooseberry"
    assert org._country == "GB"
