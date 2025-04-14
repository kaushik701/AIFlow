# Text Processing Examples

This page provides examples of AIFlow workflows for text processing tasks.

## Basic Text Summarization

This workflow takes a text input and generates a concise summary:

```
workflow TextSummarizer {
    input: text;
    
    step Summarize {
        model: "gpt-3.5-turbo";
        prompt: "Summarize the following text in a concise way: {{text}}";
        output: summary;
    }
    
    return: summary;
}
```

### Usage

```bash
aiflow text_summarizer.aiflow --input "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to natural intelligence displayed by animals including humans. AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals."
```

## Multi-Step Text Processing

This workflow processes text in multiple steps: first summarizing, then extracting key points:

```
workflow MultiStepProcessor {
    input: text;
    
    step Summarize {
        model: "gpt-3.5-turbo";
        prompt: "Summarize the following text in 1-2 sentences: {{text}}";
        output: summary;
    }
    
    step ExtractKeyPoints {
        model: "gpt-3.5-turbo";
        prompt: "Extract 3-5 key points from this summary: {{summary}}";
        output: key_points;
    }
    
    return: key_points;
}
```

### Usage

```bash
aiflow multi_step_processor.aiflow --input "Your long text here..."
```

## Text Classification

This workflow classifies text into predefined categories:

```
workflow TextClassifier {
    input: text;
    
    step Classify {
        model: "gpt-3.5-turbo";
        prompt: "Classify the following text into one of these categories: Technology, Business, Health, Entertainment, Sports, Politics. Respond with just the category name: {{text}}";
        output: category;
    }
    
    return: category;
}
```

### Usage

```bash
aiflow text_classifier.aiflow --input "Apple announced its new iPhone model today, featuring improved camera capabilities and longer battery life."
```

## Question Answering

This workflow answers questions based on a provided context:

```
workflow QuestionAnswerer {
    input: text;
    
    step ParseInput {
        model: "gpt-3.5-turbo";
        prompt: "Extract the context and question from this input. Format your response as JSON with 'context' and 'question' fields: {{text}}";
        output: parsed_input;
    }
    
    step AnswerQuestion {
        model: "gpt-3.5-turbo";
        prompt: "Using the following parsed input: {{parsed_input}}, answer the question based on the context provided.";
        output: answer;
    }
    
    return: answer;
}
```

### Usage

```bash
aiflow question_answerer.aiflow --input "Context: The Golden Gate Bridge is a suspension bridge spanning the Golden Gate, the one-mile-wide strait connecting San Francisco Bay and the Pacific Ocean. The structure links the U.S. city of San Francisco, California—the northern tip of the San Francisco Peninsula—to Marin County. Question: When was the Golden Gate Bridge built?"
```

## Text Formatting

This workflow reformats text according to specified guidelines:

```
workflow TextFormatter {
    input: text;
    
    step Format {
        model: "gpt-3.5-turbo";
        prompt: "Reformat the following text to be more concise, use bullet points where appropriate, and correct any grammar or spelling errors: {{text}}";
        output: formatted_text;
    }
    
    return: formatted_text;
}
```

### Usage

```bash
aiflow text_formatter.aiflow --input "Your unformatted text here..."
```

## Advanced: Text Processing with Conditional Logic

This workflow processes text differently based on its length:

```
workflow ConditionalProcessor {
    input: text;
    
    step AnalyzeLength {
        model: "gpt-3.5-turbo";
        prompt: "Analyze the length of this text and respond with only 'short' if it's under 100 words or 'long' if it's 100 words or more: {{text}}";
        output: length_category;
    }
    
    if (exists:length_category) {
        step ProcessShortText {
            model: "gpt-3.5-turbo";
            prompt: "The text is {{length_category}}. Summarize it in one sentence: {{text}}";
            output: result;
        }
    } else {
        step ProcessLongText {
            model: "gpt-3.5-turbo";
            prompt: "The text is {{length_category}}. Summarize it in 3-5 bullet points: {{text}}";
            output: result;
        }
    }
    
    return: result;
}
```

### Usage

```bash
aiflow conditional_processor.aiflow --input "Your text here..."
```

## Best Practices

When creating text processing workflows:

1. **Be specific in prompts**: Clearly specify what you want the model to do
2. **Break complex tasks into steps**: Use multiple steps for complex processing
3. **Use appropriate models**: Choose the right model for your task
4. **Test with various inputs**: Ensure your workflow works with different text types
5. **Use mock mode for testing**: Test without making actual API calls

## Next Steps

- Explore [sentiment analysis examples](sentiment-analysis.md)
- Learn about [translation workflows](translation.md)
- Understand [advanced workflow techniques](../advanced/extending.md)
