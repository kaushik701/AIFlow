# AIFlow: A Language for AI Workflows

AIFlow is a domain-specific language designed to simplify the creation and execution of AI workflows. It provides an intuitive syntax for connecting different AI operations together, making it easy to build complex AI pipelines without writing extensive code.

## Features

- **Simple, Intuitive Syntax**: Define AI workflows with a clear, readable syntax
- **OpenAI Integration**: Seamlessly integrate with OpenAI models
- **Conditional Logic**: Create workflows with decision points based on AI outputs
- **Template Variables**: Easily reference previous outputs in subsequent steps
- **Command-Line Interface**: Run workflows directly from the command line
- **Mock Mode**: Test workflows without making actual API calls

## Example Workflow

```
workflow SentimentAnalyzer {
  input: text;
  
  step AnalyzeSentiment {
    model: "gpt-3.5-turbo";
    prompt: "Analyze the sentiment of the following text and respond with only 'positive', 'negative', or 'neutral': {{text}}";
    output: sentiment;
  }
  
  if (exists:sentiment) {
    step PositiveResponse {
      model: "gpt-3.5-turbo";
      prompt: "The sentiment is {{sentiment}}. Generate a supportive response to this positive feedback: {{text}}";
      output: response;
    }
  } else {
    step NegativeResponse {
      model: "gpt-3.5-turbo";
      prompt: "The sentiment is {{sentiment}}. Generate a helpful response to address this concern: {{text}}";
      output: response;
    }
  }
  
  return: response;
}
```

## Getting Started

Check out the [Installation](getting-started/installation.md) guide to set up AIFlow on your system, then follow the [Quick Start](getting-started/quick-start.md) guide to create your first workflow.

## License

AIFlow is open-source software licensed under the MIT license.