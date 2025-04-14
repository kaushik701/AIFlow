# Performance Optimization

This page provides strategies for optimizing the performance of your AIFlow workflows.

## Optimizing API Calls

### Choose the Right Model

Different OpenAI models have different performance characteristics:

| Model | Speed | Cost | Capability |
|-------|-------|------|------------|
| gpt-3.5-turbo | Faster | Lower | Good for most tasks |
| gpt-4 | Slower | Higher | Better for complex tasks |

Choose the most appropriate model for your task:

- Use `gpt-3.5-turbo` for simple tasks and when speed is important
- Use `gpt-4` only when you need its advanced capabilities

### Minimize Token Usage

OpenAI models process text as tokens, and you pay for both input and output tokens:

1. **Keep prompts concise**: Remove unnecessary text from prompts
2. **Limit output length**: Set appropriate `max_tokens` values
3. **Use efficient prompt templates**: Design prompts that require fewer tokens
4. **Batch similar requests**: Process multiple items in a single API call when possible

### Example: Efficient vs. Inefficient Prompts

❌ **Inefficient prompt**:
```
prompt: "You are a helpful assistant that summarizes text. Please take the following text and create a summary that captures the main points while being concise and clear. The summary should be about 3-4 sentences long. Here is the text to summarize: {{text}}";
```

✅ **Efficient prompt**:
```
prompt: "Summarize in 3-4 sentences: {{text}}";
```

## Workflow Optimization

### Multi-Step Workflows

Break complex tasks into multiple steps for better results:

1. **Progressive refinement**: Start with a basic output and refine it in subsequent steps
2. **Specialized steps**: Use different steps for different aspects of a task
3. **Conditional execution**: Only execute steps when necessary

### Parallel Processing

For independent tasks, consider implementing parallel processing:

```
workflow ParallelProcessor {
    input: text;
    
    // These steps could be processed in parallel
    step Summarize {
        model: "gpt-3.5-turbo";
        prompt: "Summarize: {{text}}";
        output: summary;
    }
    
    step ExtractKeywords {
        model: "gpt-3.5-turbo";
        prompt: "Extract keywords: {{text}}";
        output: keywords;
    }
    
    // Combine results
    step CombineResults {
        model: "gpt-3.5-turbo";
        prompt: "Combine summary and keywords: Summary: {{summary}}. Keywords: {{keywords}}";
        output: result;
    }
    
    return: result;
}
```

Note: AIFlow currently processes steps sequentially, but future versions may support parallel execution.

## Caching Strategies

### Implement Result Caching

Cache results to avoid redundant API calls:

1. **Cache based on input**: Store results keyed by input text
2. **Set appropriate TTL**: Define how long cached results remain valid
3. **Invalidate cache when needed**: Clear cache when dependencies change

### Example Caching Implementation

```python
import hashlib
import json
import os
import time

class ResultCache:
    def __init__(self, cache_dir="./cache", ttl=3600):
        self.cache_dir = cache_dir
        self.ttl = ttl
        os.makedirs(cache_dir, exist_ok=True)
    
    def get_cache_key(self, input_text, model):
        # Create a unique key based on input and model
        key = f"{input_text}:{model}"
        return hashlib.md5(key.encode()).hexdigest()
    
    def get_cached_result(self, input_text, model):
        key = self.get_cache_key(input_text, model)
        cache_file = os.path.join(self.cache_dir, key)
        
        if not os.path.exists(cache_file):
            return None
        
        # Check if cache is expired
        if time.time() - os.path.getmtime(cache_file) > self.ttl:
            return None
        
        with open(cache_file, "r") as f:
            return json.load(f)
    
    def cache_result(self, input_text, model, result):
        key = self.get_cache_key(input_text, model)
        cache_file = os.path.join(self.cache_dir, key)
        
        with open(cache_file, "w") as f:
            json.dump(result, f)
```

## Mock Mode for Development

Use mock mode during development to avoid API costs and speed up testing:

```bash
aiflow your_workflow_file.aiflow --input "Your input text" --mock
```

Benefits of mock mode for performance:

1. **Instant responses**: No network latency
2. **No API costs**: Test without incurring charges
3. **Offline development**: Develop without an internet connection

## Monitoring and Profiling

### Monitor Performance Metrics

Track key performance metrics:

1. **API call latency**: Time taken for API calls
2. **Token usage**: Number of tokens used per request
3. **Step execution time**: Time taken for each step
4. **Total workflow time**: Time taken for the entire workflow

### Example Monitoring Implementation

```python
import time
import logging

class PerformanceMonitor:
    def __init__(self):
        self.start_times = {}
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("performance")
    
    def start_timer(self, name):
        self.start_times[name] = time.time()
    
    def end_timer(self, name, metadata=None):
        if name not in self.start_times:
            self.logger.warning(f"Timer {name} was never started")
            return
        
        duration = time.time() - self.start_times[name]
        log_message = f"{name}: {duration:.2f}s"
        
        if metadata:
            log_message += f" | {metadata}"
        
        self.logger.info(log_message)
        return duration
```

## Batch Processing

For processing large amounts of data, use batch processing:

1. **Split large inputs**: Break large inputs into smaller chunks
2. **Process in batches**: Process chunks in batches
3. **Combine results**: Combine results from all batches

### Example Batch Processing Script

```python
def batch_process(items, batch_size=10):
    results = []
    
    for i in range(0, len(items), batch_size):
        batch = items[i:i+batch_size]
        batch_results = process_batch(batch)
        results.extend(batch_results)
    
    return results

def process_batch(batch):
    # Process each item in the batch
    return [process_item(item) for item in batch]

def process_item(item):
    # Process a single item using AIFlow
    # This could involve running a workflow
    return result
```

## Next Steps

- Learn about [extending AIFlow](extending.md)
- Understand [security best practices](security.md)
- Explore [advanced workflow examples](../examples/text-processing.md)
