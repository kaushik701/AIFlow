# OpenAI Parameters

AIFlow allows you to configure various parameters when using OpenAI models. This page explains the available parameters and how to use them.

## Default Parameters

By default, AIFlow uses the following parameters when calling OpenAI models:

| Parameter | Default Value | Description |
|-----------|---------------|-------------|
| `model` | Specified in step | The OpenAI model to use |
| `temperature` | 0.7 | Controls randomness (0.0 to 1.0) |
| `max_tokens` | 1000 | Maximum number of tokens in the response |

## Environment Variable Configuration

You can customize the default parameters using environment variables:

```
TEMPERATURE_DEFAULT=0.5
MAX_TOKENS_DEFAULT=500
```

These environment variables can be set in your system environment or in a `.env` file.

## Parameter Descriptions

### Model

The `model` parameter specifies which OpenAI model to use. See the [Models](models.md) page for details on supported models.

Example:
```
model: "gpt-3.5-turbo";
```

### Temperature

The `temperature` parameter controls the randomness of the model's output. Lower values make the output more deterministic, while higher values make it more random.

- Range: 0.0 to 1.0
- Default: 0.7

Temperature values:
- 0.0: Very deterministic, focused responses
- 0.3: Balanced, slightly creative but mostly focused
- 0.7: Creative, varied responses (default)
- 1.0: Maximum creativity and randomness

### Max Tokens

The `max_tokens` parameter limits the length of the model's response.

- Range: 1 to model's maximum (varies by model)
- Default: 1000

One token is approximately 4 characters for English text.

## Best Practices

When configuring OpenAI parameters:

1. **Use lower temperature** (0.0 - 0.3) for tasks requiring factual, deterministic responses
2. **Use higher temperature** (0.7 - 1.0) for creative tasks
3. **Set appropriate max_tokens** to balance between getting complete responses and controlling costs
4. **Use environment variables** to configure default parameters for all workflows

## Future Enhancements

In future versions of AIFlow, we plan to add support for:

- Per-step parameter configuration
- Additional OpenAI parameters like `top_p`, `presence_penalty`, and `frequency_penalty`
- Model-specific parameter presets

## Next Steps

- Learn about [error handling](error-handling.md)
- Explore [example workflows](../examples/text-processing.md)
- Understand [security best practices](../advanced/security.md)
