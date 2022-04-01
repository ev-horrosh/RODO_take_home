from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class Table(BaseModel):
    hash: str
    dealership_id: str
    vin: str
    mileage: Optional[int]
    is_new: Optional[bool]
    stock_number: Optional[str]
    dealer_year: Optional[int]
    dealer_make: Optional[str]
    dealer_model: Optional[str]
    dealer_trim: Optional[str]
    dealer_model_number: Optional[str]
    dealer_msrp: Optional[int]
    dealer_invoice: Optional[int]
    dealer_body: Optional[str]
    dealer_inventory_entry_date: Optional[datetime]
    dealer_exterior_color_description: Optional[str]
    dealer_interior_color_description: Optional[str]
    dealer_exterior_color_code: Optional[str]
    dealer_interior_color_code: Optional[str]
    dealer_transmission_name: Optional[str]
    dealer_installed_option_codes: Optional[list[str]]
    dealer_installed_option_descriptions: Optional[list[str]]
    dealer_additional_specs: Optional[str]
    dealer_doors: Optional[str]
    dealer_drive_type: Optional[str]
    updated_at: Optional[datetime] = datetime.now()
    dealer_images: Optional[list[str]]
    dealer_certified: Optional[bool]
