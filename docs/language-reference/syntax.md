# AIFlow Syntax

This page provides an overview of the AIFlow language syntax.

## Basic Structure

An AIFlow program consists of one or more workflow definitions. Each workflow defines a sequence of steps that process input data and produce output.

The basic structure of an AIFlow workflow is:

```
workflow WorkflowName {
    input: input_type;
    
    step StepName {
        model: "model_name";
        prompt: "prompt_text";
        output: output_variable;
    }
    
    return: output_variable;
}
```

## Comments

AIFlow supports single-line comments using the `//` syntax:

```
// This is a comment
workflow Example {
    // This is another comment
    input: text;
}
```

## Identifiers

Identifiers in AIFlow (names for workflows, steps, and variables) must:

- Begin with a letter or underscore
- Contain only letters, numbers, and underscores
- Be case-sensitive

Examples of valid identifiers:
- `MyWorkflow`
- `process_text`
- `step1`
- `_internal_variable`

## Keywords

AIFlow has the following reserved keywords:

- `workflow`: Defines a new workflow
- `input`: Specifies the input for a workflow
- `step`: Defines a processing step
- `model`: Specifies which AI model to use
- `prompt`: Defines the prompt to send to the model
- `output`: Names the output of a step
- `return`: Specifies what the workflow should return
- `if`: Starts a conditional block
- `else`: Defines the alternative in a conditional block

## Literals

AIFlow supports the following types of literals:

- **String literals**: Enclosed in double quotes, e.g., `"This is a string"`
- **Identifiers**: Names for workflows, steps, and variables

## Template Variables

Template variables allow you to reference values within strings. They are enclosed in double curly braces:

```
prompt: "Process this text: {{variable_name}}";
```

## Statements

AIFlow has the following types of statements:

- **Workflow definition**: `workflow Name { ... }`
- **Input declaration**: `input: type;`
- **Step definition**: `step Name { ... }`
- **Model specification**: `model: "model_name";`
- **Prompt definition**: `prompt: "prompt_text";`
- **Output assignment**: `output: variable_name;`
- **Return statement**: `return: variable_name;`
- **Conditional statement**: `if (condition) { ... } else { ... }`

## Complete Example

Here's a complete example of an AIFlow workflow with multiple steps and conditional logic:

```
workflow TextAnalyzer {
    input: text;
    
    step Summarize {
        model: "gpt-3.5-turbo";
        prompt: "Summarize the following text: {{text}}";
        output: summary;
    }
    
    step AnalyzeSentiment {
        model: "gpt-3.5-turbo";
        prompt: "Analyze the sentiment of this summary. Respond with only 'positive', 'negative', or 'neutral': {{summary}}";
        output: sentiment;
    }
    
    if (exists:sentiment) {
        step GenerateResponse {
            model: "gpt-3.5-turbo";
            prompt: "Generate a response based on this {{sentiment}} sentiment summary: {{summary}}";
            output: response;
        }
    } else {
        step DefaultResponse {
            model: "gpt-3.5-turbo";
            prompt: "Generate a neutral response to this summary: {{summary}}";
            output: response;
        }
    }
    
    return: response;
}
```

## Next Steps

- Learn more about [workflow definitions](workflows.md)
- Explore [step definitions](steps.md) in detail
- Understand [variables and templates](variables.md)
- See how to use [template variables](templates.md)
