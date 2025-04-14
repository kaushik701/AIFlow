# Quick Start

This guide will help you get started with AIFlow by creating and running a simple workflow.

## Creating Your First Workflow

Create a new file named `text_processor.aiflow` with the following content:

```
workflow TextProcessor {
    input: text;
    
    step Summarize {
        model: "gpt-3.5-turbo";
        prompt: "Summarize the following text in a concise way: {{text}}";
        output: summary;
    }
    
    return: summary;
}
```

This simple workflow takes text as input, sends it to the GPT-3.5 Turbo model for summarization, and returns the summary.

## Running the Workflow

You can run the workflow using the AIFlow CLI:

```bash
aiflow text_processor.aiflow --input "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to natural intelligence displayed by animals including humans. AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals."
```

If you don't have an OpenAI API key or want to test without making actual API calls, use the `--mock` flag:

```bash
aiflow text_processor.aiflow --input "Your text here" --mock
```

## Understanding the Workflow

Let's break down the components of the workflow:

- `workflow TextProcessor { ... }`: Defines a workflow named "TextProcessor"
- `input: text;`: Specifies that the workflow takes a single input named "text"
- `step Summarize { ... }`: Defines a processing step named "Summarize"
- `model: "gpt-3.5-turbo";`: Specifies which AI model to use
- `prompt: "Summarize the following text: {{text}}";`: The prompt to send to the model, with `{{text}}` as a placeholder for the input
- `output: summary;`: Names the output of this step as "summary"
- `return: summary;`: Specifies that the workflow should return the "summary" variable

## Next Steps

Now that you've created and run a basic workflow, you can:

1. Learn how to create a [multi-step workflow](first-workflow.md)
2. Explore the [language syntax](../language-reference/syntax.md) in more detail
3. Check out the [examples](../examples/text-processing.md) for more complex workflows

For a complete reference of AIFlow's features, see the [Language Reference](../language-reference/syntax.md) section.
