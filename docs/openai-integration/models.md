# OpenAI Models

AIFlow integrates with OpenAI's language models to power its AI capabilities. This page explains which models are supported and how to use them.

## Supported Models

AIFlow currently supports the following OpenAI models:

| Model | Description | Use Cases |
|-------|-------------|-----------|
| `gpt-3.5-turbo` | OpenAI's GPT-3.5 Turbo model | General text processing, summarization, content generation |
| `gpt-4` | OpenAI's GPT-4 model (requires access) | Complex reasoning, advanced content generation, specialized tasks |

## Specifying Models

You can specify which model to use in a step using the `model` property:

```
step ProcessText {
    model: "gpt-3.5-turbo";
    prompt: "Process this text: {{text}}";
    output: processed_text;
}
```

## Model Selection Guidelines

When choosing which model to use, consider the following factors:

### GPT-3.5 Turbo

- **Advantages**:
  - Faster response times
  - Lower cost
  - Good for most general tasks
  - Widely available to all OpenAI API users

- **Best for**:
  - Summarization
  - Basic content generation
  - Simple classification tasks
  - General text processing

### GPT-4

- **Advantages**:
  - More advanced reasoning capabilities
  - Better at complex instructions
  - More accurate responses
  - Better at specialized tasks

- **Best for**:
  - Complex reasoning tasks
  - Advanced content generation
  - Specialized domain tasks
  - Tasks requiring high accuracy

- **Note**: Requires access to GPT-4 API

## API Key Requirements

To use OpenAI models in AIFlow, you need an OpenAI API key. You can set up your API key in two ways:

1. **Environment Variable**:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. **.env File**:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Mock Mode

If you don't have an OpenAI API key or want to test your workflows without making actual API calls, you can use AIFlow's mock mode:

```bash
aiflow your_workflow_file.aiflow --input "Your input text" --mock
```

In mock mode, AIFlow will generate mock responses instead of calling the OpenAI API.

## Rate Limits and Quotas

When using OpenAI models, be aware of the following:

- OpenAI API has rate limits on the number of requests you can make
- Your API key has a quota that limits the total amount of usage
- Different models have different pricing

Check the [OpenAI pricing page](https://openai.com/pricing) for the most up-to-date information on pricing and quotas.

## Best Practices

When using OpenAI models in AIFlow:

1. **Start with GPT-3.5 Turbo** for most tasks
2. **Use GPT-4 only when necessary** for complex tasks
3. **Keep prompts clear and specific** to get the best results
4. **Use mock mode for testing** to avoid unnecessary API calls
5. **Monitor your API usage** to avoid unexpected costs

## Next Steps

- Learn about [model parameters](parameters.md)
- Understand [error handling](error-handling.md)
- Explore [example workflows](../examples/text-processing.md)
