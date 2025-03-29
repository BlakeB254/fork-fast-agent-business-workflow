from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Union, Any
from enum import Enum

class FieldStatus(str, Enum):
    EMPTY = "empty"
    IN_PROGRESS = "in_progress"
    FINALIZED = "finalized"

class FieldMetadata(BaseModel):
    status: FieldStatus = FieldStatus.EMPTY
    suggestions: Optional[List[str]] = None
    editable: bool = True
    required: bool = False
    helper_text: Optional[str] = None
    context_notes: Optional[str] = None

class EnhancedField(BaseModel):
    value: Any
    metadata: FieldMetadata

# Example of how the business profile would be structured
class EnhancedBusinessProfile(BaseModel):
    business_name: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                required=True,
                helper_text="Legal name of the business as registered",
                context_notes="This will appear on all legal documents"
            )
        )
    )
    
    trade_name: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                helper_text="Trade name or DBA (Doing Business As) if different from legal name",
                context_notes="Use this if your business operates under a different name than its legal entity name"
            )
        )
    )
    
    business_type: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                required=True,
                helper_text="Legal structure of your business (LLC, Corporation, Sole Proprietorship, etc.)",
                context_notes="Different business types have different legal and tax implications"
            )
        )
    )
    
    industry: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                required=True,
                helper_text="Primary industry of your business operations",
                context_notes="This will help determine relevant regulations and business requirements"
            )
        )
    )
    
    formation_date: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                helper_text="Date when your business was legally formed (MM/DD/YYYY)",
                context_notes="Important for compliance filings and anniversary requirements"
            )
        )
    )
    
    state_of_incorporation: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                helper_text="State where your business is legally registered",
                context_notes="Different states have different requirements and tax implications"
            )
        )
    )
    
    ein: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                helper_text="Employer Identification Number (XX-XXXXXXX)",
                context_notes="If you don't have an EIN, you can apply at IRS.gov. Using your personal SSN for business can create liability risks."
            )
        )
    )
    
    duns_number: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                helper_text="Data Universal Numbering System identifier (if applicable)",
                context_notes="Useful for government contracts and establishing business credit"
            )
        )
    )
    
    business_description: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                required=True,
                helper_text="Brief description of your business purpose and activities",
                context_notes="This will be used in marketing materials and business documents"
            )
        )
    )
    
    business_address: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                required=True,
                helper_text="Primary business address",
                context_notes="Using a virtual address or PO box can provide privacy and help establish business credibility separate from your home."
            )
        )
    )
    
    mailing_address: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                helper_text="Mailing address if different from physical address",
                context_notes="This is where you'll receive business mail and correspondence"
            )
        )
    )
    
    phone_number: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                required=True,
                helper_text="Primary business phone number",
                context_notes="Consider a dedicated business phone line to maintain professionalism"
            )
        )
    )
    
    email_address: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                required=True,
                helper_text="Primary business email address",
                context_notes="Use a professional email with your business domain for credibility"
            )
        )
    )
    
    website: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value="",
            metadata=FieldMetadata(
                helper_text="Business website URL",
                context_notes="A professional website enhances credibility and online presence"
            )
        )
    )
    
    social_media_profiles: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value={},
            metadata=FieldMetadata(
                helper_text="Social media profile URLs (LinkedIn, Facebook, Twitter, etc.)",
                context_notes="Active social media presence can boost your business visibility"
            )
        )
    )
    
    business_licenses: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value=[],
            metadata=FieldMetadata(
                helper_text="Business licenses and permits with expiration dates",
                context_notes="Different industries require specific licenses to operate legally"
            )
        )
    )
    
    revenue_model: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value=[],
            metadata=FieldMetadata(
                required=True,
                helper_text="How your business generates revenue",
                context_notes="Understanding your revenue streams helps with business planning and forecasting"
            )
        )
    )
    
    color_scheme: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value={
                "primary": "#3498db",
                "secondary": "#2c3e50",
                "accent": "#e74c3c"
            },
            metadata=FieldMetadata(
                helper_text="Brand color scheme (primary, secondary, accent)",
                context_notes="Consistent colors help establish brand recognition"
            )
        )
    )
    
    logo_uploaded: EnhancedField = Field(
        default_factory=lambda: EnhancedField(
            value=False,
            metadata=FieldMetadata(
                helper_text="Whether a logo has been uploaded",
                context_notes="A professional logo enhances brand identity"
            )
        )
    )