# Turn Micro Types - Architecture & Development Guide

## Project Overview

**turn_micro_types** is a Python client library providing type definitions and schemas for Turn's microservices ecosystem. It serves as a shared types package for:
- Worker microservice (background check candidate data)
- Checks service (background check dispositions and classifications)
- Cohort service (cohort invitation management)
- Communications protocol (internal messaging)
- State machine abstractions (workflow management)

The library is published as an installable Python package via pip/git and used across Turn's backend services to maintain consistent data models and type safety.

**Current Branch:** `story/SCREEN-5190/parse-worker-documents-with-ai-image-recognition`

## Tech Stack

- **Language:** Python 3.8+
- **Core Dependencies:**
  - `pydantic >= 1.10.5` - Data validation and serialization
  - `typing-extensions >= 4.4.0` - Extended type hints
  - `mypy >= 1.0.1` - Static type checking
- **Code Quality Tools:**
  - `black == 23.1.0` - Code formatter (line length: 85 chars)
  - `flake8 == 6.0.0` - Linter (max complexity: 10)
  - `mypy == 1.1.1` - Type checker with pydantic plugin
- **Package Management:** setuptools (editable installs from git)

## Directory Structure

```
turn_micro_types/
├── src/turn_micro_types/          # Main package root
│   ├── __init__.py
│   │
│   ├── checks_service/            # Background checks domain
│   │   ├── constants.py           # CheckType enum (MVR, etc.)
│   │   ├── requests/
│   │   │   └── request_check/
│   │   │       └── __init__.py    # RequestCheckSchema
│   │   ├── responses/
│   │   │   └── __init__.py        # RunChecksEndpointResponse
│   │   └── dispositions/          # AI disposition classification
│   │       ├── constants.py       # DispositionClassification enum
│   │       ├── requests/
│   │       │   └── classify.py    # ClassificationDictRequest
│   │       └── responses/
│   │           └── classify.py    # Classification response schemas
│   │
│   ├── worker_micro/              # Partner worker data models
│   │   └── responses/
│   │       └── PartnerWorker/
│   │           ├── constants.py   # PARTNER_WORKER_STATES (state machine)
│   │           └── responses/
│   │               ├── __init__.py         # Address & Details schemas
│   │               └── partner_worker_document.py  # Document types
│   │
│   ├── cohort_service/            # Cohort/invitation management
│   │   └── invitation/
│   │       ├── constants.py       # InvitationState enum (21 states)
│   │       └── __init__.py
│   │
│   ├── communications_protocol/   # Internal messaging
│   │   ├── constants.py           # SupportEmailCommunicationCategory enum
│   │   └── requests/
│   │       └── support_email.py   # InternalCommsReferencesPWPayload
│   │
│   ├── turn_state_machine/        # Generic state machine framework
│   │   ├── __init__.py            # TurnStateMachine abstract base
│   │   └── exception.py           # State machine exceptions
│   │
│   └── misc/                      # Utility enums
│       ├── us_states.py           # USStateAbbreviation enum
│       └── py.typed               # PEP 561 marker file
│
├── .github/
│   ├── workflows/
│   │   ├── typings.yml            # mypy type checking (on PR)
│   │   ├── black.yml              # Code formatting check (line-length: 85)
│   │   ├── flake8.yml             # Linting (max-line-length: 88)
│   │   └── pip-audit.yml          # Security audit (ignores: PYSEC-2022-42969, GHSA-r9hx-vwmv-q579)
│   └── pull_request_template.md
│
├── .vscode/
│   └── settings.json              # VSCode Python config
│
├── pyproject.toml                 # Package metadata & build config
├── requirements.txt               # Dev/test dependencies
├── tox.ini                        # Flake8 config
├── mypy.ini                       # Type checker config
├── example.py                     # Usage example
├── MANIFEST.in                    # Includes py.typed marker
├── README.md                      # Installation instructions
└── .gitignore

```

## Common Development Commands

### Setup & Installation

```bash
# Install in development mode
pip install -e .

# Install dependencies
pip install -r requirements.txt

# Upgrade pip
python -m pip install --upgrade pip
```

### Code Quality & Testing

```bash
# Type checking with mypy (enforces `disallow_untyped_defs`)
mypy src/turn_micro_types

# Format code with black (line length: 85)
black src/turn_micro_types --line-length 85

# Lint with flake8 (max line length: 88, max complexity: 10)
flake8 src/turn_micro_types

# Security audit
pip-audit
```

### CI/CD Workflows (GitHub Actions)

The project runs 4 automated checks on every pull request:

1. **typings.yml** - mypy type checking
   - Python 3.10
   - Enforces `disallow_untyped_defs = True`
   - Uses pydantic mypy plugin

2. **black.yml** - Code formatting
   - Checks with `--check --verbose --line-length 85`

3. **flake8.yml** - Linting
   - Python 3.8
   - Max line length: 88, max complexity: 10

4. **pip-audit.yml** - Security vulnerability scanning
   - Ignores known safe vulnerabilities

### Local Development Workflow

```bash
# 1. Make changes
# 2. Format code
black src/turn_micro_types --line-length 85

# 3. Lint
flake8 src/turn_micro_types

# 4. Type check
mypy src/turn_micro_types

# 5. Commit and push (triggers CI checks)
```

## Architecture & Patterns

### 1. Domain-Driven Structure

The package is organized by business domains rather than technical layers:
- Each domain (checks_service, worker_micro, etc.) owns its requests, responses, and constants
- Clear separation between input schemas (requests) and output schemas (responses)
- Constants files define domain-specific enums and configurations

### 2. Pydantic-Based Type Safety

**Pattern:** All data structures inherit from `pydantic.BaseModel`
- Automatic validation and serialization
- IDE type hints support
- JSON schema generation capability
- Optional and default fields for API flexibility

Example:
```python
class RequestCheckSchema(BaseModel):
    partner_worker_id: int

class RunChecksEndpointResponse(BaseModel):
    checks_run: List[CheckType] = []
    errors: List[str] = []
```

### 3. State Machine Framework

**TurnStateMachine** - Generic, reusable state machine for workflow management:
- Abstract base class with generics for type-safe state definitions
- Supports on-enter and on-exit callbacks (`_on_enter_*` and `_on_exit_*` methods)
- Validates state transitions from specific previous states
- Supports wildcard transitions (`from_state="*"`)
- Integrates with database models via transition callbacks

Implementations:
- `PARTNER_WORKER_STATES` - 17 states for background check workflow
- `InvitationState` - 21 states for cohort invitations

### 4. Strict Type Annotations

**Policy:** All definitions are fully typed
- `mypy` enforces `disallow_untyped_defs = True`
- Pydantic's `mypy` plugin validates BaseModel field types
- Every function and method must have return type hints

### 5. Enum-Based Constants

Heavy use of `Enum` classes for domain constants:
- `CheckType` - MVR checks
- `DispositionClassification` - Conviction classifications
- `SupportEmailCommunicationCategory` - Support ticket categories
- `USStateAbbreviation` - 60 US states/territories
- `PartnerWorkerDocumentType` - 10 document types (DL, passport, consent, etc.)

### 6. PEP 561 Type Hints Support

Includes `py.typed` marker file in package for external type checking:
- Signals to mypy that this package is fully typed
- Enables accurate type checking in consuming projects

## Key Schemas & Models

### Worker Microservice
- **PartnerWorkerDetailsSchema** - Comprehensive worker profile (id, name, SSN validation, document URLs, etc.)
- **PartnerWorkerAddressSchema** - Nested address with location data
- **PartnerWorkerDocumentEntry** - Document metadata (id, type, URL, created_at)
- **PARTNER_WORKER_STATES** - Workflow state machine (initiated → resolved/rejected)

### Checks Service
- **RequestCheckSchema** - Trigger background check by worker ID
- **RunChecksEndpointResponse** - List of checks run and errors
- **ClassificationDictRequest** - Batch classification data submission
- **AiResponse** - AI model output (disposition, plea, status, prompt tracking)
- **ClassificationResponse/DictResponse** - Classification results with metadata

### Communications Protocol
- **InternalCommsReferencesPWPayload** - Route support communications
  - Validates turn_id format: `^C\d{10}$`
  - Supports predefined or custom communication categories
  - Optional agent notes

### Cohort Service
- **InvitationState** - 21-state invitation workflow (created → closed)

## Testing & Type Checking

### Test Configuration (.vscode/settings.json)
- Test framework: pytest (Python: `python.testing.pytestEnabled = true`)
- Test discovery: `src/test` directory
- Type checking: basic mode in IDE

### Mypy Configuration (mypy.ini)
```ini
[mypy]
plugins = pydantic.mypy          # Validate pydantic models
disallow_untyped_defs = True     # ALL defs must have types
```

### Flake8 Configuration (tox.ini)
```ini
[flake8]
max-complexity = 10
max-line-length = 88
exclude = .git, __pycache__, .venv, .pytest_cache, etc.
```

## Package Distribution

### Installation Methods

```bash
# Stable releases (if published to PyPI)
pip install turn_micro_types

# Development from GitHub
pip install git+https://github.com/turnhq/turn-alerts-client

# Specific commit
pip install git+https://github.com/turnhq/turn-alerts-client@<commit_hash>
```

### Build System
- **Backend:** setuptools (setuptools >= 61.0)
- **Configuration:** pyproject.toml with metadata
- **Distribution:** Configured for editable installs from git

## Recent Work (Branch: SCREEN-5190)

**Parse Worker Documents with AI Image Recognition**
- Recent commits indicate work on document parsing
- AI-powered image recognition for document classification
- Relates to PartnerWorkerDocumentEntry and new document handling

## Important Notes

### Code Style Requirements
- **Black:** 85 character line length (stricter than flake8's 88)
- **Type hints:** Required on all definitions
- **Pydantic models:** Use `Field()` for documentation and validation rules
- **Enums:** String enums for API compatibility (e.g., `class X(str, Enum)`)

### Common Patterns to Follow
1. Create request/response pairs in separate files
2. Define domain constants in `constants.py`
3. Use Optional fields for potentially missing data
4. Include `py.typed` in package directories for type safety
5. Use State Machine for complex workflows
6. Validate sensitive data with Pydantic Field constraints

### Known Vulnerabilities (Ignored in pip-audit)
- `PYSEC-2022-42969` - Acknowledged as safe for this context
- `GHSA-r9hx-vwmv-q579` - Acknowledged as safe for this context

## Development Workflow

1. **Create feature branch** from `master` (main branch)
2. **Make changes** following code patterns
3. **Run local checks:**
   ```bash
   black src/turn_micro_types --line-length 85
   flake8 src/turn_micro_types
   mypy src/turn_micro_types
   ```
4. **Commit** with semantic commit messages (fix:, feat:, etc.)
5. **Push** to trigger GitHub Actions CI
6. **All 4 CI checks must pass** (type checking, formatting, linting, security)
7. **Create pull request** following PR template
8. **Merge** once approved and CI passes

## VSCode Configuration

The project includes VSCode settings (.vscode/settings.json):
- **Formatter:** Black with type checking
- **Linting:** mypy (flake8 disabled in IDE but runs in CI)
- **Testing:** pytest in `src/test` directory
- **Type checking:** Basic mode

## Useful Resources

- **README.md** - Installation and basic usage
- **example.py** - Example of creating and sending alerts
- **.github/pull_request_template.md** - PR guidelines
- **pyproject.toml** - Package metadata and dependencies
