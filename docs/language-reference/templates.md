# Template Variables

Template variables in AIFlow allow you to dynamically insert values into prompts. This page explains how to use template variables and conditional logic in AIFlow.

## Template Variable Syntax

Template variables are enclosed in double curly braces:

```
{{variable_name}}
```

When the prompt is processed, the template variable is replaced with the value of the variable.

Example:
```
prompt: "Process this text: {{text}}";
```

If the `text` variable contains "Hello, world!", the processed prompt will be:
```
Process this text: Hello, world!
```

## Using Template Variables

Template variables can be used in prompts to reference:

1. **Input Variables**: Variables created by the input declaration
2. **Output Variables**: Variables created by the output assignment in steps

Example workflow with template variables:
```
workflow TextProcessor {
    input: text;
    
    step Summarize {
        model: "gpt-3.5-turbo";
        prompt: "Summarize the following text: {{text}}";
        output: summary;
    }
    
    step Analyze {
        model: "gpt-3.5-turbo";
        prompt: "Analyze the key points in this summary: {{summary}}";
        output: analysis;
    }
    
    return: analysis;
}
```

In this workflow:
- `{{text}}` in the Summarize step references the input variable
- `{{summary}}` in the Analyze step references the output variable from the Summarize step

## Multiple Template Variables

You can use multiple template variables in a single prompt:

```
prompt: "Compare these two texts: First text: {{text1}}. Second text: {{text2}}";
```

## Conditional Logic

AIFlow supports conditional logic using the `if` and `else` keywords. Conditions are specified in parentheses after the `if` keyword.

### Condition Syntax

Currently, AIFlow supports the following condition:

- `exists:variable_name`: Checks if the variable exists and is truthy

Example:
```
if (exists:sentiment) {
    // Code to execute if sentiment exists and is truthy
} else {
    // Code to execute otherwise
}
```

### Conditional Steps

You can use conditional logic to execute different steps based on conditions:

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

In this workflow:
- The `AnalyzeSentiment` step analyzes the sentiment of the input text
- The condition `exists:sentiment` checks if the sentiment variable exists and is truthy
- If the condition is true, the `PositiveResponse` step is executed
- If the condition is false, the `NegativeResponse` step is executed

## Best Practices

When using template variables and conditional logic:

1. **Ensure variables exist** before referencing them in template variables
2. **Use clear conditions** that are easy to understand
3. **Keep conditional blocks focused** on a specific task
4. **Use descriptive step names** in conditional blocks
5. **Test workflows with different inputs** to ensure conditions work as expected

## Next Steps

- Learn about [OpenAI model options](../openai-integration/models.md)
- Explore [workflow examples](../examples/text-processing.md)
- Understand [error handling](../openai-integration/error-handling.md)
