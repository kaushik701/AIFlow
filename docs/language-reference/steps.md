# Steps

In AIFlow, steps are the building blocks of workflows that define individual processing operations. This page explains how to define and use steps.

## Step Definition

A step is defined using the `step` keyword, followed by a name and a block of code enclosed in curly braces:

```
step StepName {
    // Step contents
}
```

## Step Components

A step consists of the following components:

1. **Model Specification**: Specifies which AI model to use
2. **Prompt Definition**: Defines the prompt to send to the model
3. **Output Assignment**: Names the output of the step

### Model Specification

The model specification defines which AI model to use for the step:

```
model: "model_name";
```

AIFlow supports the following models:
- `"gpt-3.5-turbo"`: OpenAI's GPT-3.5 Turbo model
- `"gpt-4"`: OpenAI's GPT-4 model (if you have access)

Example:
```
model: "gpt-3.5-turbo";
```

### Prompt Definition

The prompt definition specifies the text to send to the model:

```
prompt: "prompt_text";
```

The prompt can include template variables to reference values from the workflow:

```
prompt: "Process this text: {{variable_name}}";
```

Example:
```
prompt: "Summarize the following text: {{text}}";
```

### Output Assignment

The output assignment names the output of the step:

```
output: variable_name;
```

This creates a variable that can be used in subsequent steps or returned by the workflow.

Example:
```
output: summary;
```

## Step Execution

When a step is executed, the following happens:

1. The prompt is processed, replacing any template variables with their values
2. The processed prompt is sent to the specified model
3. The model's response is stored in the output variable

## Example Step

Here's an example of a complete step:

```
step Summarize {
    model: "gpt-3.5-turbo";
    prompt: "Summarize the following text in a concise way: {{text}}";
    output: summary;
}
```

This step:
1. Uses the GPT-3.5 Turbo model
2. Sends a prompt asking it to summarize the text (with the `{{text}}` variable replaced by the actual text)
3. Stores the model's response in a variable named `summary`

## Steps in Conditional Blocks

Steps can be used inside conditional blocks:

```
if (exists:sentiment) {
    step PositiveResponse {
        model: "gpt-3.5-turbo";
        prompt: "Generate a response for this positive feedback: {{text}}";
        output: response;
    }
} else {
    step NegativeResponse {
        model: "gpt-3.5-turbo";
        prompt: "Generate a response for this negative feedback: {{text}}";
        output: response;
    }
}
```

In this example, either the `PositiveResponse` step or the `NegativeResponse` step will be executed, depending on the condition.

## Best Practices

When creating steps:

1. **Use descriptive names** that indicate the step's purpose
2. **Keep prompts clear and specific** to get the best results from the model
3. **Use template variables** to reference values from previous steps
4. **Choose the appropriate model** for the task
5. **Use meaningful output variable names** that describe what the output represents

## Next Steps

- Learn about [variables and templates](variables.md)
- Understand how to use [template variables](templates.md)
- Explore [OpenAI model options](../openai-integration/models.md)
