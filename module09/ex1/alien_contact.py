from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(le=datetime.today())
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def bussines_rules(self) -> 'AlienContact':
        if not self.contact_id[:2] == "AC":
            raise ValueError("Contact ID must start with 'AC'")
        physical = ContactType.physical
        if self.contact_type is physical and self.is_verified is False:
            raise ValueError("Physical contact reports must be verified")
        telepathic = ContactType.telepathic
        if self.contact_type is telepathic and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if not self.message_received and self.signal_strength > 7:
            raise ValueError("Strong signals should include received messages")
        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")
    alien = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 6, 10),
        location="Area 52, Nevada",
        contact_type="radio",
        signal_strength=9.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli"
    )
    print("Valid contact report:")
    print(f"ID: {alien.contact_id}")
    print(f"Type: {alien.contact_type}")
    print(f"Location: {alien.location}")
    print(f"Signal: {alien.signal_strength}/10")
    print(f"Duration: {alien.duration_minutes} minutes")
    print(f"Witness: {alien.witness_count}")
    print(f"Message: {alien.message_received}")
    print()
    print("======================================")
    print("Expected validation error:")
    try:
        fail_alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 6, 10),
            location="Area 52, Nevada",
            contact_type="telepathic",
            signal_strength=9.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli"
        )
        print(fail_alien.contact_id)
    except ValidationError as e:
        for error in e.errors():
            mensaje = error['msg']
            if mensaje.startswith("Value error, "):
                mensaje = mensaje.replace("Value error, ", "")
            print(mensaje)


if __name__ == "__main__":
    main()
