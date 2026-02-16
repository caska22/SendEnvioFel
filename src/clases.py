from dataclasses import dataclass
from dataclasses import dataclass
from typing import Optional


@dataclass
class Employee:
    """Data model for an employee from FactorialHR API."""
    id: int
    access_id: int
    first_name: str
    last_name: str
    full_name: str
    company_id: int
    location_id: int
    created_at: str
    updated_at: str
    is_terminating: bool
    active: bool

    # Optional fields
    preferred_name: Optional[str] = None
    birth_name: Optional[str] = None
    gender: Optional[str] = None
    identifier: Optional[str] = None
    identifier_type: Optional[str] = None
    email: Optional[str] = None
    login_email: Optional[str] = None
    birthday_on: Optional[str] = None
    nationality: Optional[str] = None
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    postal_code: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    bank_number: Optional[str] = None
    swift_bic: Optional[str] = None
    bank_number_format: Optional[str] = None
    legal_entity_id: Optional[int] = None
    social_security_number: Optional[str] = None
    terminated_on: Optional[str] = None
    termination_reason_type: Optional[str] = None
    termination_reason: Optional[str] = None
    termination_observations: Optional[str] = None
    manager_id: Optional[int] = None
    timeoff_manager_id: Optional[int] = None
    phone_number: Optional[str] = None
    company_identifier: Optional[str] = None
    age_number: Optional[int] = None
    termination_type_description: Optional[str] = None
    contact_name: Optional[str] = None
    contact_number: Optional[str] = None
    personal_email: Optional[str] = None
    seniority_calculation_date: Optional[str] = None
    pronouns: Optional[str] = None
    disability_percentage_cents: Optional[int] = None
    identifier_expiration_date: Optional[str] = None
    @classmethod
    def from_dict(cls, data: dict) -> 'Employee':
        """Create an Employee instance from a dictionary."""
        # Filter the dictionary to only include fields that are part of the dataclass
        filtered_data = {k: v for k, v in data.items() if k in cls.__annotations__}
        return cls(**filtered_data)