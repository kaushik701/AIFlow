# Translation Examples

This page provides examples of AIFlow workflows for translation tasks.

## Basic Translation

This workflow translates text from one language to another:

```
workflow BasicTranslator {
    input: text;
    
    step Translate {
        model: "gpt-3.5-turbo";
        prompt: "Translate the following English text to Spanish: {{text}}";
        output: translation;
    }
    
    return: translation;
}
```

### Usage

```bash
aiflow basic_translator.aiflow --input "Hello, how are you today? I hope you're doing well."
```

## Multi-Language Translator

This workflow translates text to multiple languages at once:

```
workflow MultiLanguageTranslator {
    input: text;
    
    step TranslateMultiple {
        model: "gpt-3.5-turbo";
        prompt: "Translate the following English text to Spanish, French, and German. Format your response as JSON with language codes as keys: {{text}}";
        output: translations;
    }
    
    return: translations;
}
```

### Usage

```bash
aiflow multi_language_translator.aiflow --input "Welcome to our international conference. We're glad you could join us."
```

## Language Detection and Translation

This workflow first detects the language of the input text, then translates it to the target language:

```
workflow AutoDetectTranslator {
    input: text;
    
    step DetectLanguage {
        model: "gpt-3.5-turbo";
        prompt: "Detect the language of the following text. Respond with only the language name: {{text}}";
        output: source_language;
    }
    
    step Translate {
        model: "gpt-3.5-turbo";
        prompt: "Translate the following text from {{source_language}} to English: {{text}}";
        output: translation;
    }
    
    return: translation;
}
```

### Usage

```bash
aiflow auto_detect_translator.aiflow --input "Hola, ¿cómo estás hoy? Espero que estés bien."
```

## Translation with Formality Control

This workflow translates text with control over the formality level:

```
workflow FormalityTranslator {
    input: text;
    
    step ParseInput {
        model: "gpt-3.5-turbo";
        prompt: "Parse the following input which contains a text to translate and a formality level (formal/informal) separated by '|||'. Format your response as JSON with 'text' and 'formality' fields: {{text}}";
        output: parsed_input;
    }
    
    step Translate {
        model: "gpt-3.5-turbo";
        prompt: "Translate the following text to Spanish using the specified formality level from the parsed input: {{parsed_input}}";
        output: translation;
    }
    
    return: translation;
}
```

### Usage

```bash
aiflow formality_translator.aiflow --input "Could you please assist me with this matter? ||| formal"
```

## Translation with Context Preservation

This workflow translates text while preserving specific context or terminology:

```
workflow ContextPreservingTranslator {
    input: text;
    
    step ParseInput {
        model: "gpt-3.5-turbo";
        prompt: "Parse the following input which contains a text to translate, a target language, and a context/domain (e.g., medical, legal, technical) separated by '|||'. Format your response as JSON with 'text', 'target_language', and 'context' fields: {{text}}";
        output: parsed_input;
    }
    
    step Translate {
        model: "gpt-3.5-turbo";
        prompt: "Translate the text from the parsed input to the specified target language, ensuring that domain-specific terminology and context are preserved: {{parsed_input}}";
        output: translation;
    }
    
    return: translation;
}
```

### Usage

```bash
aiflow context_preserving_translator.aiflow --input "The patient presents with acute myocardial infarction and requires immediate intervention. ||| Spanish ||| medical"
```

## Translation with Explanation

This workflow translates text and provides explanations for idiomatic expressions or cultural references:

```
workflow ExplainedTranslator {
    input: text;
    
    step TranslateWithExplanation {
        model: "gpt-3.5-turbo";
        prompt: "Translate the following English text to Japanese. For any idiomatic expressions or cultural references, provide explanations in parentheses. Format your response as JSON with 'translation' and 'explanations' fields: {{text}}";
        output: result;
    }
    
    return: result;
}
```

### Usage

```bash
aiflow explained_translator.aiflow --input "It's raining cats and dogs outside, so I'll just Netflix and chill tonight instead of going to the baseball game."
```

## Best Practices

When creating translation workflows:

1. **Specify the source and target languages**: Be clear about which languages you're translating between
2. **Consider context and domain**: Translations can vary based on context (medical, legal, technical, etc.)
3. **Be aware of formality levels**: Many languages have different formality levels that affect translation
4. **Preserve cultural nuances**: Be mindful of cultural references and idioms
5. **Use structured output formats**: Request JSON or structured formats for complex translations
6. **Test with diverse inputs**: Ensure your workflow works with different types of text and languages

## Next Steps

- Explore [text processing examples](text-processing.md)
- Learn about [sentiment analysis workflows](sentiment-analysis.md)
- Understand [advanced workflow techniques](../advanced/extending.md)
