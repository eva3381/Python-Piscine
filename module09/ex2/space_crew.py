from pydantic import BaseModel, model_validator, Field
from enum import Enum
from datetime import datetime
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(le=datetime.today())
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(ge=1, le=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def mission_validation_rules(self):
        if self.mission_id[:1] != "M":
            raise ValueError('Mission ID must start with "M"')
        leader = any(
            m.rank in [Rank.captain, Rank.commander] for m in self.crew)
        if not leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        len_crew = len(self.crew)
        most_experience = [
            member.years_experience for member in self.crew
            if member.years_experience >= 5]
        percent_experience_member = len(most_experience) / len_crew
        if self.duration_days > 365 and percent_experience_member < 0.5:
            raise ValueError(
                "Long missions (>365 days)"
                "need 50% experienced crew (5+ years)"
                )
        for members in self.crew:
            if members.is_active is False:
                raise ValueError("All crew members must be active")
        return self
