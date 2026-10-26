## Requirements

1.  NodeJS v22.10 or higher (https://nodejs.org/en/download)
2.  Python 3.11 or higher
3.  Git

The Python version needs to be compatible with the dependencies listed in `requirements.txt`.

## Installation

### 1. Clone the Repository

Clone the project and enter its directory:

```bash
git clone https://github.com/phtawde/NexusLocker.git
cd NexusLocker
```

### 2. Set Up Python Virtual Environment

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual env:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

### 3. Install Frontend Dependencies

From the project root (the top level of the project directory), run:

```bash
npm --prefix frontend install
```

Install the root development dependencies:

```bash
npm install
```

## Application Startup

Ensure Python virtual environment is active:

```powershell
.\.venv\Scripts\Activate.ps1
```

From the project root run:

```bash
npm run dev
```

Both the Flask backend and the React frontend will start running. Flask will be for API only calls, while React is the frontend.

## Understanding Project Files

There are several files that you don't have to understand and are only for configs and dependencies.

These files are:

```text
NexusLocker/
├── frontend/
│ ├── eslint.config.js
│ ├── package-lock.json
│ ├── package.json
│ └── vite.config.js
├── package-lock.json
├── package.json
└── requirements.txt
```

You can safely hide these files in your IDE if you'd like.

### Hiding Files in VS Code:

1. Add a folder called ".vscode" at the project root
2. Create a file named "settings.json" inside of .vscode
3. Add exclusions, for example:

```json
{
  "files.exclude": {
    "**/node_modules": true,
    "**/__pycache__": true,
    "**/package-lock.json": true,
    "**/package.json": true,
    "**/eslint.config.js": true,
    "**/vite.config.js": true,
    ".venv": true
  }
}
```

## Diagrams

### Architecture

<img width="2212" height="897" alt="ArchitectureDiagram" src="https://github.com/user-attachments/assets/b94d7cd1-a40f-447c-b66a-6fb095d1e2fa" />

### Classes

<img width="822" height="1057" alt="Class Diagram drawio" src="https://github.com/user-attachments/assets/79137925-ca6e-4dff-a3ec-f3695c59631b" />

### State Chart (Cart)

<img width="767" height="76" alt="Cart State Chart drawio" src="https://github.com/user-attachments/assets/6e8011b6-f893-415a-a2b8-dba3c7860873" />

### Sequence (Checkout)

<img width="727" height="374" alt="Checkout Sequence drawio" src="https://github.com/user-attachments/assets/8f4c996d-b4d7-4219-8bc6-90834552e08c" />

### Use Case

<img width="403" height="912" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/43b9885b-afbe-4c59-ad8d-87c5f4ccf1f2" />
