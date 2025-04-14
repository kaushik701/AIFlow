# Creating Your First Workflow

This guide will walk you through creating a more complex workflow with multiple steps and conditional logic.

## Multi-Step Workflow

Let's create a workflow that processes text in multiple steps:

1. First, it summarizes the input text
2. Then, it elaborates on the summary with more details

Create a file named `multi_step.aiflow` with the following content:

```
workflow MultiStepProcessor {
    input: text;
    
    step Summarize {
        model: "gpt-3.5-turbo";
        prompt: "Summarize the following text in 1-2 sentences: {{text}}";
        output: summary;
    }
    
    step Elaborate {
        model: "gpt-3.5-turbo";
        prompt: "Elaborate on this summary with more details and examples: {{summary}}";
        output: elaboration;
    }
    
    return: elaboration;
}
```

## Adding Conditional Logic

Now, let's create a workflow that includes conditional logic. This workflow will analyze the sentiment of the input text and respond differently based on the result:

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
            prompt: "The sentiment is {{sentiment}}. Generate a supportive response to this feedback: {{text}}";
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

## Running the Workflows

You can run these workflows using the AIFlow CLI:

```bash
# Run the multi-step workflow
aiflow multi_step.aiflow --input "Your text here"

# Run the sentiment analysis workflow
aiflow sentiment_analyzer.aiflow --input "I really love your product! It has made my life so much easier."
```

Or use mock mode for testing:

```bash
aiflow sentiment_analyzer.aiflow --input "Your feedback text here" --mock
```

## Understanding Template Variables

In these workflows, we use template variables (enclosed in double curly braces `{{}}`) to reference values:

- `{{text}}` refers to the input text provided to the workflow
- `{{summary}}` refers to the output of the Summarize step
- `{{sentiment}}` refers to the output of the AnalyzeSentiment step

This allows you to pass data between steps in your workflow.

## Understanding Conditional Logic

The `if (exists:sentiment)` statement checks if the `sentiment` variable exists and is truthy. If it is, the `PositiveResponse` step is executed; otherwise, the `NegativeResponse` step is executed.

This allows you to create workflows that make decisions based on the output of previous steps.

## Next Steps

Now that you've created more complex workflows, you can:

1. Learn more about [workflow syntax](../language-reference/workflows.md)
2. Explore [step definitions](../language-reference/steps.md) in detail
3. Understand how to use [variables and templates](../language-reference/variables.md)
4. Check out more [examples](../examples/text-processing.md)
