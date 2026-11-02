# Spotlight Series Fall 2026 CMU-Africa 04-801-W2

## Installation

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if it is not already available, then install this project and its dependencies from the repository root:

```powershell
uv sync
```

## Configuration

Set the required environment variables before running the project. For example, in PowerShell:

```powershell
$env:GEMINI_API_KEY="Ak.....Ps3"
```

Replace the example value with your actual Gemini API key.

## Run

The main run for now is:

```powershell
uv run google-gen-ai-sdk/book_delivery.py
```