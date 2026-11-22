
# TestGenius AI

### Autonomous Selenium Testing & Intelligent Debugging Platform

TestGenius AI is an AI-powered software testing platform designed to transform requirements into automated test cases, execute browser tests, analyze failures, and assist developers with intelligent debugging.

## Project Vision

Build an integrated QA engineering platform combining browser automation, agentic AI, machine learning, distributed execution, and cloud infrastructure.

## Core Features

- Requirement-to-test-case generation
- Automated browser testing with Selenium
- AI-powered failure classification
- Root-cause analysis and debugging suggestions
- Evidence-based self-healing locator recommendations
- Regression test selection
- Flaky-test detection
- Automated QA reports and analytics
- Human approval for AI-proposed changes

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, JavaScript |
| API Backend | Python, FastAPI |
| AI Agents | LangGraph |
| Browser Automation | Selenium 4, Java 17 |
| Distributed Coordinator | Rust, Axum, Tokio |
| Machine Learning | scikit-learn |
| Database | PostgreSQL |
| Cloud | AWS, Azure |
| Containers | Docker |
| Version Control | Git, GitHub |

## Architecture

The platform is organized into independent modules:

1. Frontend Dashboard
2. API Gateway
3. AI Agent Engine
4. Rust Job Coordinator
5. Selenium Browser Runner
6. ML Failure Analysis
7. PostgreSQL Database
8. Cloud Infrastructure

## Repository Structure

```text
testgenius-ai/
├── frontend/
├── services/
│   ├── api-gateway/
│   ├── ai-engine/
│   ├── coordinator/
│   ├── selenium-runner/
│   └── api-test-runner/
├── database/
├── ml/
├── infrastructure/
├── tests/
├── docs/
└── .github/
```

## Development Environment

Developed locally on Apple Silicon macOS.

- Python 3.12
- Java 17
- Node.js 24
- Rust stable
- Docker
- Visual Studio Code
- IntelliJ IDEA

## Development Status

**Current Phase:** Environment Setup and Project Foundation

The repository structure and local development environment have been prepared. Application modules will be implemented incrementally.

## Security Principles

- Authorized target applications only
- Secure handling of credentials and secrets
- Human approval for locator healing
- Structured validation of AI outputs
- Audit trails for execution and debugging
- Tenant-aware access control

## Future Scope

- Distributed browser execution
- AWS deployment
- Azure deployment
- Advanced QA analytics
- Agent evaluation and observability

## Author

Aritrika Biswas

GitHub: https://github.com/aritrikabiswas

---

*TestGenius AI — Building intelligent, autonomous software testing workflows.*

# macOS
.DS_Store

# Environment variables and secrets
.env
.env.*
!.env.example
*.pem
*.key

# Python
__pycache__/
*.py[cod]
.venv/
venv/
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
htmlcov/

# JavaScript / React / Node
node_modules/
dist/
build/
.vite/
coverage/

# Java / Maven / Gradle
target/
.gradle/
*.class

# Rust
**/target/

# IDE
.idea/
.vscode/

# Logs and temporary files
*.log
*.tmp

# Generated test artifacts
artifacts/
test-results/
