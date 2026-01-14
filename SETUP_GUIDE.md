# Jesse Project Setup and Run Guide

This guide explains how to set up the Jesse trading framework from the source code you have downloaded.

## Prerequisites

1. **Python**: Version 3.10 or higher is required.

## Installation

1. Open a terminal in the project root directory (`c:\Users\Apple Computer\Downloads\jesse-master`).
2. (Optional but recommended) Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Install Jesse in editable mode:
   ```powershell
   pip install -e .
   ```

## Verification

To verify that the installation was successful, you can run the test suite:
```powershell
pytest
```

## Running Jesse

Jesse is a framework that runs specific trading "projects" (bots). To run a bot, you need a project structure.

### 1. Create a Project
Since you are using the source code, you can verify if the CLI command is available:
```powershell
jesse --help
```
If you see a command like `make-project`, use it:
```powershell
mkdir my-bot
cd my-bot
jesse make-project
```

If `make-project` is not available, you can create the minimal required structure manually:
1. Create a new directory for your bot (e.g., `my-bot`).
2. Inside `my-bot`, create two folders:
   - `strategies`
   - `storage`

### 2. Run the Bot
Navigate to your bot directory (e.g., `my-bot`) and run:
```powershell
jesse run
```
This will start the Jesse API server. You can usually access the dashboard or interact with it via `http://localhost:9000` (default port).

> **Note**: For detailed documentation on creating strategies and using the dashboard, refer to the [official documentation](https://docs.jesse.trade).
