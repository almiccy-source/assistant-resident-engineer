"""
Application constants and enumerations
Centralized definitions for the ACRE application
"""

from enum import Enum

# ============================================================================
# CONTRACT AND COMPLIANCE CONSTANTS
# ============================================================================

class ContractType(str, Enum):
    """Types of construction contracts"""
    FIDIC_DB = "fidic_db"  # Design-Build
    FIDIC_DBE = "fidic_dbe"  # Design-Build-Operate
    FIDIC_DBC = "fidic_dbc"  # Design-Build-Construct
    FIDIC_IC = "fidic_ic"  # Integrated-Contract
    FIDIC_SP = "fidic_sp"  # Short-Form
    FIXED_PRICE = "fixed_price"
    TIME_MATERIALS = "time_materials"
    LUMP_SUM = "lump_sum"

class PaymentStatus(str, Enum):
    """Payment status codes"""
    PENDING = "pending"
    APPROVED = "approved"
    SUBMITTED = "submitted"
    PAID = "paid"
    REJECTED = "rejected"
    DISPUTED = "disputed"

class ChangeRequestStatus(str, Enum):
    """Change request status codes"""
    DRAFT = "draft"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    IMPLEMENTED = "implemented"
    CLOSED = "closed"

class InspectionStatus(str, Enum):
    """Quality inspection status"""
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    PASSED = "passed"
    FAILED = "failed"
    CONDITIONAL_PASS = "conditional_pass"

class SnagStatus(str, Enum):
    """Snagging/defect status"""
    OPEN = "open"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    PENDING_APPROVAL = "pending_approval"
    CLOSED = "closed"
    DEFERRED = "deferred"

class DrawingStatus(str, Enum):
    """Shop drawing status"""
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    COMMENTS = "comments"
    APPROVED = "approved"
    APPROVED_AS_NOTED = "approved_as_noted"
    REJECTED = "rejected"
    RESUBMIT = "resubmit"

class DocumentType(str, Enum):
    """Types of documents in the project"""
    DRAWING = "drawing"
    SPECIFICATION = "specification"
    METHOD_STATEMENT = "method_statement"
    SHOP_DRAWING = "shop_drawing"
    TEST_REPORT = "test_report"
    CERTIFICATE = "certificate"
    INSPECTION_REPORT = "inspection_report"
    DAILY_REPORT = "daily_report"
    MEETING_MINUTES = "meeting_minutes"
    CONTRACT = "contract"

# ============================================================================
# MEASUREMENT AND UNITS
# ============================================================================

class UnitType(str, Enum):
    """Measurement units"""
    # Length
    METER = "m"
    KILOMETER = "km"
    CENTIMETER = "cm"
    
    # Area
    SQUARE_METER = "m²"
    SQUARE_KILOMETER = "km²"
    HECTARE = "ha"
    
    # Volume
    CUBIC_METER = "m³"
    LITER = "L"
    
    # Weight
    KILOGRAM = "kg"
    TONNE = "t"
    GRAM = "g"
    
    # Count
    PIECE = "pc"
    EACH = "ea"
    NUMBER = "no"
    
    # Others
    RUNNING_METER = "rm"
    SQUARE_FOOT = "ft²"
    CUBIC_FOOT = "ft³"

# ============================================================================
# COMPLIANCE STANDARDS
# ============================================================================

class ComplianceStandard(str, Enum):
    """Applicable compliance standards"""
    UAE_BUILDING_CODE = "uae_building_code"
    FIDIC_CONDITIONS = "fidic_conditions"
    ISO_9001 = "iso_9001"
    ISO_14001 = "iso_14001"
    OSHA = "osha"
    LOCAL_REGULATIONS = "local_regulations"

class SafetyPriority(str, Enum):
    """HSE/Safety observation priority"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    OBSERVATION = "observation"

# ============================================================================
# FINANCIAL CONSTANTS
# ============================================================================

class CurrencyCode(str, Enum):
    """Currency codes"""
    AED = "AED"  # UAE Dirham
    USD = "USD"  # US Dollar
    EUR = "EUR"  # Euro
    GBP = "GBP"  # British Pound
    INR = "INR"  # Indian Rupee

class BudgetType(str, Enum):
    """Types of budget items"""
    FIXED = "fixed"
    CONTINGENCY = "contingency"
    PROVISIONAL_SUM = "provisional_sum"
    PRIME_COST = "prime_cost"

# ============================================================================
# REPORT TYPES
# ============================================================================

class ReportType(str, Enum):
    """Types of reports that can be generated"""
    DAILY_PROGRESS = "daily_progress"
    WEEKLY_SUMMARY = "weekly_summary"
    MONTHLY_REPORT = "monthly_report"
    FINANCIAL_STATUS = "financial_status"
    QUALITY_REPORT = "quality_report"
    SAFETY_REPORT = "safety_report"
    CHANGE_REQUEST_LOG = "change_request_log"
    SNAGGING_LIST = "snagging_list"
    MATERIAL_RECEIPT = "material_receipt"
    HANDOVER_REPORT = "handover_report"

# ============================================================================
# ERROR CODES
# ============================================================================

class ErrorCode(str, Enum):
    """Application error codes"""
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    NOT_FOUND = "NOT_FOUND"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    DATABASE_ERROR = "DATABASE_ERROR"
    FILE_ERROR = "FILE_ERROR"
    EXPORT_ERROR = "EXPORT_ERROR"
    PERMISSION_DENIED = "PERMISSION_DENIED"

# ============================================================================
# DEFAULT VALUES
# ============================================================================

DEFAULT_CURRENCY = CurrencyCode.AED
DEFAULT_CONTRACT_TYPE = ContractType.FIDIC_DB
DEFAULT_INSPECTION_PRIORITY = SafetyPriority.MEDIUM

# Application Configuration Constants
APP_TITLE = "ACRE - Automated Civil Resident Engineer Assistant"
APP_VERSION = "1.0.0"
ORGANIZATION = "Civil Engineering Solutions"
SUPPORT_EMAIL = "support@acre-app.com"

# UI Constants
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
DEFAULT_FONT_SIZE = 10
DEFAULT_FONT_FAMILY = "Segoe UI"

# File Upload Constants
MAX_FILE_SIZE_MB = 50
ALLOWED_FILE_EXTENSIONS = ['.pdf', '.xlsx', '.xls', '.csv', '.dwg', '.pdf', '.jpg', '.png', '.doc', '.docx']

# Database Constants
DB_CONNECTION_TIMEOUT = 30
DB_MAX_POOL_SIZE = 10
