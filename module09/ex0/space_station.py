from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxigen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field(le=datetime.today())
    is_operational: bool = Field(default=True)
    notes: str | None = None


def main():
    print("Space Station Data Validation")
    print("========================================")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxigen_level=92.3,
        last_maintenance=datetime(2024, 5, 20),
        is_operational=True,
        notes="All correct")
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxigen_level}%")
    status = "Operational" if station.is_operational else "Maintenance"
    print(f"Status: {status}")
    print()
    print("========================================")
    print("Expected validation error:")
    try:
        fail_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=60,
            power_level=85.5,
            oxigen_level=92.3,
            last_maintenance=datetime(2024, 5, 20),
            is_operational=True,
            notes="All correct")
        print(fail_station.station_id)
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
