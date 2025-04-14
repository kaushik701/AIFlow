# Installation

This guide will walk you through the process of installing AIFlow on your system.

## Prerequisites

Before installing AIFlow, make sure you have the following:

- Python 3.8 or higher
- pip (Python package installer)
- An OpenAI API key (for using OpenAI models)

## Installation Steps

### 1. Install from PyPI

The simplest way to install AIFlow is using pip:

```bash
pip install aiflow
```

### 2. Install from Source

Alternatively, you can install AIFlow from source:

```bash
git clone https://github.com/kaushik701/AIFlow.git
cd AIFlow
pip install -e .
```

## Setting Up Your API Keys

AIFlow requires an OpenAI API key to function properly. You can set up your API key in two ways:

### Option 1: Environment Variables

Set your API key as an environment variable:

```bash
# On Windows
set OPENAI_API_KEY=your_api_key_here

# On macOS/Linux
export OPENAI_API_KEY=your_api_key_here
```

### Option 2: .env File

Create a `.env` file in your project directory with the following content:

```
OPENAI_API_KEY=your_api_key_here
```

## Verifying Installation

To verify that AIFlow is installed correctly, run the following command:

```bash
aiflow --version
```

You should see the version number of AIFlow printed to the console.

## Using Mock Mode

If you don't have an OpenAI API key or want to test your workflows without making actual API calls, you can use AIFlow's mock mode:

```bash
aiflow your_workflow_file.aiflow --input "Your input text" --mock
```

In mock mode, AIFlow will generate mock responses instead of calling the OpenAI API.

## Next Steps

Now that you have AIFlow installed, check out the [Quick Start](quick-start.md) guide to create your first workflow.