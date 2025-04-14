# Variables

In AIFlow, variables are used to store and pass data between different parts of a workflow. This page explains how variables work in AIFlow.

## Variable Declaration

Variables in AIFlow are implicitly declared in three ways:

1. **Input Declaration**: The input variable is declared in the workflow's input declaration
2. **Output Assignment**: Variables are created by the output assignment in steps
3. **Condition Results**: Variables can be created as the result of condition evaluations

### Input Declaration

The input declaration creates a variable with the specified type:

```
input: text;
```

This creates a variable named after the type (in this case, `text`) that contains the input provided to the workflow.

### Output Assignment

The output assignment in a step creates a variable with the specified name:

```
step ProcessText {
    model: "gpt-3.5-turbo";
    prompt: "Process this text: {{text}}";
    output: processed_text;
}
```

This creates a variable named `processed_text` that contains the model's response.

## Variable Scope

Variables in AIFlow have workflow-level scope, which means:

1. Variables are accessible throughout the entire workflow after they are declared
2. Variables can be referenced in any step after they are declared
3. Variables cannot be accessed outside the workflow they are declared in

## Variable Types

AIFlow currently supports the following variable types:

- **Text**: String values containing text

All variables in AIFlow are treated as text, regardless of their content.

## Using Variables

Variables are primarily used in two ways:

1. **In Template Variables**: To insert variable values into prompts
2. **In Conditions**: To make decisions based on variable values

### In Template Variables

Variables can be referenced in prompts using template variables:

```
prompt: "Process this text: {{variable_name}}";
```

The template variable `{{variable_name}}` will be replaced with the value of the variable when the prompt is processed.

Example:
```
prompt: "Summarize the following text: {{text}}";
```

### In Conditions

Variables can be used in conditions to make decisions:

```
if (exists:sentiment) {
    // Code to execute if sentiment exists and is truthy
}
```

## Variable Lifecycle

The lifecycle of a variable in AIFlow is as follows:

1. **Declaration**: The variable is declared (implicitly through input or output)
2. **Assignment**: The variable is assigned a value
3. **Usage**: The variable is used in template variables or conditions
4. **Scope End**: The variable goes out of scope when the workflow ends

## Example Workflow with Variables

Here's an example of a workflow that uses variables:

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
1. The `text` variable is created by the input declaration
2. The `summary` variable is created by the output assignment in the Summarize step
3. The `analysis` variable is created by the output assignment in the Analyze step
4. The `summary` variable is used in a template variable in the Analyze step
5. The `analysis` variable is returned by the workflow

## Best Practices

When using variables:

1. **Use descriptive names** that indicate what the variable contains
2. **Keep variable names consistent** with their content
3. **Use snake_case** for variable names with multiple words
4. **Avoid reusing variable names** for different purposes
5. **Check if variables exist** before using them in conditions

## Next Steps

- Learn about [template variables](templates.md) in detail
- Understand [conditional logic](templates.md#conditional-logic)
- Explore [workflow examples](../examples/text-processing.md)
