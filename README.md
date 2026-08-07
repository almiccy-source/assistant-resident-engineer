# ACRE - Automated Civil Resident Engineer Assistant

A comprehensive desktop application designed for resident civil engineers to automate project management workflows including BOQ tracking, change requests, payment verification, shop drawings, snagging, QA/QC controls, and compliance with FIDIC, UAE Building Code, and international standards.

## Features

### Core Modules
- **BOQ Management** - Track bill of quantities, rates, and costs
- **Change Request System** - Create, approve, and track scope changes
- **Payment Tracking** - Verify payments against contract conditions
- **Shop Drawings** - Submit, review, and approve drawings
- **Snagging Management** - Log defects and track remediation
- **Quality Control** - QA/QC inspection checklists and reports
- **HSE Monitoring** - Safety observations and incident logging
- **Daily Reports** - Automated progress and activity reports

### User Roles
- **Resident Engineer** - Full project oversight
- **QA/QC Consultant** - Quality inspections and approvals
- **Document Controller** - Document and drawing management
- **Assistant RE** - Support and data entry

### Capabilities
- ✅ Data import/export (Excel, CSV)
- ✅ Automated report generation (PDF, Excel)
- ✅ User authentication with role-based access
- ✅ Cloud and local database support
- ✅ Multi-user collaboration
- ✅ FIDIC compliance templates
- ✅ UAE regulatory compliance checks

## Technology Stack
- **Language:** Python 3.10+
- **Desktop UI:** PyQt6
- **Database:** SQLite (local) / PostgreSQL (production)
- **Reporting:** ReportLab, openpyxl
- **Export:** PDF, Excel, CSV
- **Authentication:** JWT-based role management

## Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/almiccy-source/assistant-resident-engineer.git
cd assistant-resident-engineer
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Initialize the database:**
```bash
python scripts/initialize_db.py
```

5. **Run the application:**
```bash
python src/main.py
```

## Project Structure

```
assistant-resident-engineer/
├── src/
│   ├── main.py                    # Application entry point
│   ├── config.py                  # Configuration settings
│   ├── core/
│   │   ├── database.py            # Database management
│   │   ├── auth.py                # User authentication
│   │   ├── logger.py              # Logging setup
│   │   └── constants.py           # Global constants
│   ├── models/
│   │   ├── boq.py                 # BOQ data models
│   │   ├── change_request.py      # Change request models
│   │   ├── payment.py             # Payment tracking models
│   │   ├── shop_drawing.py        # Drawing management models
│   │   ├── snagging.py            # Defect tracking models
│   │   ├── user.py                # User and roles
│   │   └── inspection.py          # QA/QC inspection models
│   ├── ui/
│   │   ├── main_window.py         # Main application window
│   │   ├── dialogs/               # Dialog windows
│   │   ├── widgets/               # Reusable UI components
│   │   └── styles.qss             # UI stylesheets
│   ├── modules/
│   │   ├── boq_manager.py         # BOQ management logic
│   │   ├── change_request_mgr.py  # Change request management
│   │   ├── payment_mgr.py         # Payment tracking
│   │   ├── shop_drawing_mgr.py    # Drawing management
│   │   ├── snagging_mgr.py        # Snagging management
│   │   ├── inspection_mgr.py      # QA/QC inspections
│   │   └── report_generator.py    # Report generation
│   └── utils/
│       ├── validators.py          # Input validation
│       ├── formatters.py          # Data formatting
│       └── export_utils.py        # Export functionality
├── scripts/
│   ├── initialize_db.py           # Database initialization
│   ├── import_data.py             # Data import script
│   └── generate_reports.py        # Batch report generation
├── tests/
│   ├── unit/                      # Unit tests
│   ├── integration/               # Integration tests
│   └── test_data/                 # Test datasets
├── docs/
│   ├── user_guide.md              # User manual
│   ├── admin_guide.md             # Administrator guide
│   ├── api_reference.md           # API documentation
│   ├── compliance/
│   │   ├── fidic_compliance.md    # FIDIC contract compliance
│   │   ├── uae_building_code.md   # UAE Building Code reference
│   │   └── international_codes.md # International standards
│   └── templates/
│       ├── boq_template.xlsx      # BOQ template
│       ├── change_request.docx    # Change request template
│       └── inspection_checklist.xlsx  # Inspection template
├── config/
│   ├── database.yaml              # Database configuration
│   ├── logging.yaml               # Logging configuration
│   └── app_settings.yaml          # Application settings
├── requirements.txt               # Python dependencies
├── LICENSE                        # MIT License
└── CONTRIBUTING.md                # Contribution guidelines

```

## Usage

### For Resident Engineer
1. Launch the application
2. Log in with your credentials
3. Access the dashboard to view project KPIs
4. Manage BOQ, track progress, and approve changes
5. Generate and review reports

### For QA/QC Consultant
1. Review inspection checklists
2. Conduct quality inspections
3. Log non-conformance reports (NCRs)
4. Approve shop drawings
5. Generate quality reports

### For Document Controller
1. Manage shop drawing submissions
2. Track drawing revisions
3. Maintain document library
4. Archive completed drawings

## Compliance & Standards

This application supports:
- **FIDIC (Fédération Internationale des Ingénieurs-Conseils) Contracts**
- **UAE Building Code**
- **International Construction Standards**
- **Contract Administration Best Practices**
- **HSE (Health, Safety & Environment) Regulations**

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## Support & Documentation

- **User Guide:** See [docs/user_guide.md](docs/user_guide.md)
- **Technical Documentation:** See [docs/api_reference.md](docs/api_reference.md)
- **Compliance Reference:** See [docs/compliance/](docs/compliance/)

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Author

Developed for resident civil engineers managing complex construction and infrastructure projects.

---

**Version:** 1.0.0  
**Last Updated:** August 2026  
**Repository:** https://github.com/almiccy-source/assistant-resident-engineer
