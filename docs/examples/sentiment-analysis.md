# Sentiment Analysis Examples

This page provides examples of AIFlow workflows for sentiment analysis tasks.

## Basic Sentiment Analysis

This workflow analyzes the sentiment of input text and categorizes it as positive, negative, or neutral:

```
workflow SentimentAnalyzer {
    input: text;
    
    step AnalyzeSentiment {
        model: "gpt-3.5-turbo";
        prompt: "Analyze the sentiment of the following text and respond with only 'positive', 'negative', or 'neutral': {{text}}";
        output: sentiment;
    }
    
    return: sentiment;
}
```

### Usage

```bash
aiflow sentiment_analyzer.aiflow --input "I really love your product! It has made my life so much easier."
```

## Sentiment Analysis with Explanation

This workflow analyzes sentiment and provides an explanation for the classification:

```
workflow SentimentWithExplanation {
    input: text;
    
    step AnalyzeSentiment {
        model: "gpt-3.5-turbo";
        prompt: "Analyze the sentiment of the following text. Respond in JSON format with 'sentiment' (positive, negative, or neutral) and 'explanation' fields: {{text}}";
        output: analysis;
    }
    
    return: analysis;
}
```

### Usage

```bash
aiflow sentiment_with_explanation.aiflow --input "The service was okay, but the staff could have been more attentive."
```

## Sentiment Analysis with Response Generation

This workflow analyzes sentiment and generates an appropriate response based on the sentiment:

```
workflow SentimentResponder {
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

### Usage

```bash
aiflow sentiment_responder.aiflow --input "I've been using your app for a month now and I'm really impressed with how intuitive it is."
```

## Multi-Category Sentiment Analysis

This workflow analyzes sentiment across multiple categories:

```
workflow MultiCategorySentiment {
    input: text;
    
    step AnalyzeMultiCategory {
        model: "gpt-3.5-turbo";
        prompt: "Analyze the sentiment of the following product review across these categories: Product Quality, Customer Service, Value for Money, and Ease of Use. For each category, provide a rating from 1-5 and a brief explanation. Format your response as JSON: {{text}}";
        output: analysis;
    }
    
    return: analysis;
}
```

### Usage

```bash
aiflow multi_category_sentiment.aiflow --input "I purchased the XYZ blender last month. The build quality is excellent and it's very powerful. However, it's quite expensive compared to similar products. The customer service was responsive when I had questions about the warranty. It's fairly easy to use but the instruction manual could be clearer."
```

## Sentiment Trend Analysis

This workflow analyzes sentiment trends across multiple pieces of feedback:

```
workflow SentimentTrendAnalyzer {
    input: text;
    
    step ParseFeedback {
        model: "gpt-3.5-turbo";
        prompt: "Parse the following collection of feedback items. Each item is separated by '---'. For each item, determine the sentiment (positive, negative, or neutral). Then analyze overall trends. Format your response as JSON with 'individual_sentiments' and 'overall_trends' fields: {{text}}";
        output: analysis;
    }
    
    return: analysis;
}
```

### Usage

```bash
aiflow sentiment_trend_analyzer.aiflow --input "The new feature is amazing! It saves me so much time. ---  Why did you change the UI? It's much harder to use now. --- The app is stable and works as expected. --- I'm having trouble finding the settings menu after the update."
```

## Emotion Detection

This workflow goes beyond basic sentiment to detect specific emotions:

```
workflow EmotionDetector {
    input: text;
    
    step DetectEmotions {
        model: "gpt-3.5-turbo";
        prompt: "Analyze the following text and identify the primary emotions expressed (e.g., joy, anger, fear, surprise, sadness, disgust). Provide a confidence level (low, medium, high) for each detected emotion. Format your response as JSON: {{text}}";
        output: emotions;
    }
    
    return: emotions;
}
```

### Usage

```bash
aiflow emotion_detector.aiflow --input "I can't believe they canceled the event at the last minute! I was really looking forward to it and had been planning for weeks. Now I don't know what to do with my weekend."
```

## Best Practices

When creating sentiment analysis workflows:

1. **Be specific about sentiment categories**: Clearly define what constitutes positive, negative, or neutral sentiment
2. **Consider context**: Sentiment can be context-dependent, so provide relevant context in prompts
3. **Use structured output formats**: Request JSON or structured formats for complex analyses
4. **Test with diverse inputs**: Ensure your workflow works with different types of text and sentiments
5. **Consider multiple dimensions**: For product or service feedback, analyze sentiment across multiple dimensions

## Next Steps

- Explore [text processing examples](text-processing.md)
- Learn about [translation workflows](translation.md)
- Understand [advanced workflow techniques](../advanced/extending.md)
