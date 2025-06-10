# Email Agent

The `email_agent` is a Google ADK-powered agent designed to generate professional emails with a structured subject and body. It ensures that the emails are well-formatted, professional, and tailored to the user's request.

## Features

- **Concise and Relevant Subject Line**: Automatically creates a descriptive subject.
- **Well-Structured Email Body**: Generates emails with a professional greeting, clear content, appropriate closing, and a signature.
- **Tone Matching**: Adapts the email tone to match the purpose (e.g., formal for business, friendly for colleagues).

## How it Works

The agent uses the `gemini-2.0-flash` model and a defined `EmailContent` output schema to ensure the generated email always has a `subject` and `body`.

## Getting Started

Follow these steps to set up and run the `email_agent`.

### Prerequisites

- UV (Python package manager)
- Python >= 3.13

### 1. Set up Environment & Install ADK

It's recommended to create and activate a virtual environment:

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment (macOS/Linux)
source .venv/bin/activate
```

### 2. Set up the Model (API Key)

Your agent needs authentication credentials to make calls to the Large Language Model (LLM).

1.  **Get an API key from Google AI Studio.**
2.  Create a `.env` file in the `3-structured-output/email_agent/` directory (if it doesn't exist) and add your API key:

    ```
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    GOOGLE_API_KEY=YOUR_ACTUAL_API_KEY_HERE
    ```

    Replace `YOUR_ACTUAL_API_KEY_HERE` with your actual Google AI Studio API key.

### 3. Run Your Agent

Navigate to the `3-structured-output` directory in your terminal:

```bash
cd 3-structured-output
```

There are two primary ways to run your agent:

#### a) Dev UI (Recommended for Development)

This launches an interactive, browser-based developer UI.

```bash
adk web
```

Open the URL provided (usually `http://localhost:8000` or `http://127.0.0.1:8000`) in your browser. In the top-left corner, select `email_agent` from the dropdown. You can then chat with your agent using the textbox.

#### b) Terminal (CLI)

You can also interact with your agent directly in the terminal.

```bash
adk run email_agent
```

To exit, use `Ctrl+C`.

### Example Prompt

Once the agent is running (either via `adk web` or `adk run`), you can try the following prompt:

```
user>> Draft a professional email to a potential client introducing our new product features.
```
