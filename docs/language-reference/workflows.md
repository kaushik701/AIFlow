# Workflows

In AIFlow, a workflow is the main building block that defines a sequence of processing steps. This page explains how to define and use workflows.

## Workflow Definition

A workflow is defined using the `workflow` keyword, followed by a name and a block of code enclosed in curly braces:

```
workflow WorkflowName {
    // Workflow contents
}
```

## Workflow Components

A workflow consists of the following components:

1. **Input Declaration**: Specifies what input the workflow accepts
2. **Steps**: Define the processing steps in the workflow
3. **Return Statement**: Specifies what the workflow returns

### Input Declaration

The input declaration specifies what input the workflow accepts:

```
input: input_type;
```

Currently, AIFlow supports the following input types:
- `text`: A text string

Example:
```
input: text;
```

### Steps

Steps define the processing operations in the workflow. Each step is defined using the `step` keyword, followed by a name and a block of code:

```
step StepName {
    model: "model_name";
    prompt: "prompt_text";
    output: output_variable;
}
```

See the [Steps](steps.md) page for more details.

### Return Statement

The return statement specifies what the workflow returns:

```
return: variable_name;
```

The variable must be defined by one of the steps in the workflow.

## Workflow Execution

When a workflow is executed, the following happens:

1. The input is provided to the workflow
2. The steps are executed in sequence
3. The value of the variable specified in the return statement is returned

## Example Workflow

Here's an example of a complete workflow:

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

This workflow:
1. Takes text as input
2. Summarizes the text using GPT-3.5 Turbo
3. Analyzes the key points in the summary
4. Returns the analysis

## Workflow with Conditional Logic

AIFlow supports conditional logic in workflows using the `if` and `else` keywords:

```
workflow ConditionalWorkflow {
    input: text;
    
    step AnalyzeSentiment {
        model: "gpt-3.5-turbo";
        prompt: "Analyze the sentiment of the following text and respond with only 'positive', 'negative', or 'neutral': {{text}}";
        output: sentiment;
    }
    
    if (exists:sentiment) {
        step PositiveResponse {
            model: "gpt-3.5-turbo";
            prompt: "Generate a response for this {{sentiment}} feedback: {{text}}";
            output: response;
        }
    } else {
        step DefaultResponse {
            model: "gpt-3.5-turbo";
            prompt: "Generate a neutral response to this feedback: {{text}}";
            output: response;
        }
    }
    
    return: response;
}
```

This workflow:
1. Takes text as input
2. Analyzes the sentiment of the text
3. Executes different steps based on the sentiment
4. Returns the appropriate response

## Best Practices

When creating workflows:

1. **Use descriptive names** for workflows, steps, and variables
2. **Keep workflows focused** on a specific task
3. **Break complex workflows** into smaller, reusable workflows
4. **Use conditional logic** to handle different scenarios
5. **Test workflows** with the `--mock` flag before using them with real API calls

## Next Steps

- Learn about [step definitions](steps.md)
- Understand [variables and templates](variables.md)
- Explore [conditional logic](templates.md#conditional-logic)
