from chapter10.src.case04.case04_1 import (
    plumage,
    air_speed_velocity,
    BirdData,
    plumages,
    speeds,
)


def test_plumage_european_swallow():
    bird = BirdData(name="European1", type="EuropeanSwallow")
    assert plumage(bird) == "average"


def test_plumage_african_swallow():
    bird = BirdData(name="African1", type="AfricanSwallow", number_of_coconuts=3)
    assert plumage(bird) == "tired"

    bird = BirdData(name="African2", type="AfricanSwallow", number_of_coconuts=2)
    assert plumage(bird) == "average"


def test_plumage_norwegian_blue():
    bird = BirdData(name="Norwegian1", type="NorwegianBlueParrot", voltage=120)
    assert plumage(bird) == "scorched"

    bird = BirdData(name="Norwegian2", type="NorwegianBlueParrot", voltage=90)
    assert plumage(bird) == "beautiful"


def test_plumage_unknown():
    bird = BirdData(name="Unknown1", type="UnknownBird")
    assert plumage(bird) == "unknown"


def test_air_speed_european_swallow():
    bird = BirdData(name="European1", type="EuropeanSwallow")
    assert air_speed_velocity(bird) == 35


def test_air_speed_african_swallow():
    bird = BirdData(name="African1", type="AfricanSwallow", number_of_coconuts=2)
    assert air_speed_velocity(bird) == 36


def test_air_speed_norwegian_blue():
    bird = BirdData(
        name="Norwegian1", type="NorwegianBlueParrot", voltage=100, is_nailed=True
    )
    assert air_speed_velocity(bird) == 0

    bird = BirdData(
        name="Norwegian2", type="NorwegianBlueParrot", voltage=100, is_nailed=False
    )
    assert air_speed_velocity(bird) == 20


def test_air_speed_unknown():
    bird = BirdData(name="Unknown1", type="UnknownBird")
    assert air_speed_velocity(bird) is None


def test_plumages_collection():
    birds = [
        BirdData(name="European1", type="EuropeanSwallow"),
        BirdData(name="African1", type="AfricanSwallow", number_of_coconuts=3),
        BirdData(name="Norwegian1", type="NorwegianBlueParrot", voltage=120),
    ]
    result = plumages(birds)
    assert result == {
        "European1": "average",
        "African1": "tired",
        "Norwegian1": "scorched",
    }


def test_speeds_collection():
    birds = [
        BirdData(name="European1", type="EuropeanSwallow"),
        BirdData(name="African1", type="AfricanSwallow", number_of_coconuts=2),
        BirdData(
            name="Norwegian1", type="NorwegianBlueParrot", voltage=100, is_nailed=False
        ),
    ]
    result = speeds(birds)
    assert result == {"European1": 35, "African1": 36, "Norwegian1": 20}
