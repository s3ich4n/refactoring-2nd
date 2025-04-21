import pytest

from chapter12.src.case10.case10_2 import (
    BirdData,
    Bird,
)


@pytest.fixture
def default_bird_data():
    return BirdData(
        name="Generic Bird",
        plumage="normal",
    )


@pytest.fixture
def european_swallow_data():
    return BirdData(
        name="European Swallow",
        plumage="sleek",
    )


@pytest.fixture
def african_swallow_data_no_coconuts():
    return BirdData(
        name="African Swallow",
        plumage="colorful",
        number_of_coconuts=0,
    )


@pytest.fixture
def african_swallow_data_with_coconuts():
    return BirdData(
        name="African Swallow",
        plumage="colorful",
        number_of_coconuts=3,
    )


@pytest.fixture
def african_swallow_data_max_coconuts():
    return BirdData(
        name="African Swallow",
        plumage="colorful",
        number_of_coconuts=20,
    )


@pytest.fixture
def norwegian_blue_parrot_data_low_voltage():
    return BirdData(
        name="Norwegian Blue",
        plumage="beautiful",
        voltage=90,
        is_nailed=False,
    )


@pytest.fixture
def norwegian_blue_parrot_data_high_voltage():
    return BirdData(
        name="Norwegian Blue",
        plumage="beautiful",
        voltage=120,
        is_nailed=False,
    )


@pytest.fixture
def norwegian_blue_parrot_data_nailed():
    return BirdData(
        name="Norwegian Blue",
        plumage="beautiful",
        voltage=50,
        is_nailed=True,
    )


# 기본 Bird 클래스 테스트
def test_generic_bird(default_bird_data):
    bird = Bird(default_bird_data)
    assert bird.name == "Generic Bird"
    assert bird.plumage == "normal"


def test_bird_with_no_plumage():
    data = BirdData(name="No Plumage Bird", plumage=None)
    bird = Bird(data)
    assert bird.plumage == "average"  # 깃털이 없으면 "average"를 반환


# European Swallow 테스트
def test_european_swallow(european_swallow_data):
    swallow = Bird(european_swallow_data)
    assert swallow.name == "European Swallow"
    assert swallow.plumage == "sleek"
    assert swallow.air_speed_velocity == 35


# African Swallow 테스트
def test_african_swallow_no_coconuts(african_swallow_data_no_coconuts):
    swallow = Bird(african_swallow_data_no_coconuts)
    assert swallow.name == "African Swallow"
    assert swallow.plumage == "colorful"
    assert swallow.air_speed_velocity == 40  # 40 - 2 * 0


def test_african_swallow_with_coconuts(african_swallow_data_with_coconuts):
    swallow = Bird(african_swallow_data_with_coconuts)
    assert swallow.air_speed_velocity == 34  # 40 - 2 * 3


def test_african_swallow_max_coconuts(african_swallow_data_max_coconuts):
    swallow = Bird(african_swallow_data_max_coconuts)
    assert swallow.air_speed_velocity == 0  # 40 - 2 * 20


# Norwegian Blue Parrot 테스트
def test_norwegian_blue_low_voltage(norwegian_blue_parrot_data_low_voltage):
    parrot = Bird(norwegian_blue_parrot_data_low_voltage)
    assert parrot.name == "Norwegian Blue"
    assert parrot.plumage == "beautiful"  # voltage <= 100
    assert parrot.air_speed_velocity == 19  # 10 + 90/10


def test_norwegian_blue_high_voltage(norwegian_blue_parrot_data_high_voltage):
    parrot = Bird(norwegian_blue_parrot_data_high_voltage)
    assert parrot.name == "Norwegian Blue"
    assert parrot.plumage == "scorched"  # voltage > 100
    assert parrot.air_speed_velocity == 22  # 10 + 120/10


def test_norwegian_blue_nailed(norwegian_blue_parrot_data_nailed):
    parrot = Bird(norwegian_blue_parrot_data_nailed)
    assert parrot.name == "Norwegian Blue"
    assert parrot.plumage == "beautiful"  # voltage <= 100
    assert parrot.air_speed_velocity == 0  # is_nailed = True
