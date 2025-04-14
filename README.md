## AIFlow: A Language for AI Workflows

AIFlow is a domain-specific language designed to create, manage, and execute AI workflows using OpenAI models. It provides a simple, declarative syntax for chaining together different AI operations, making complex AI pipelines more accessible and maintainable.

### Features

- **Intuitive Workflow Definition**: Create multi-step AI workflows with a readable, declarative syntax
- **OpenAI Integration**: Seamless integration with various OpenAI models (GPT-3.5, GPT-4, etc.)
- **Versatile Input Processing**: Handle various input types including text, files, and structured data
- **Data Transformation**: Transform data between workflow steps to ensure compatibility
- **Templating System**: Dynamic data insertion using a flexible templating mechanism
- **Conditional Logic**: Implement branching workflows based on specific conditions
- **Extensible Architecture**: Easily extend with custom components and integrations

### Installation

```bash
pip install aiflow
```

### Project Structure

```
AIFlow/
├── aiflow/              # Core package directory
├── docs/                # Documentation files
├── examples/            # Example workflows and usage patterns
├── tests/               # Test suite
├── .gitignore           # Git ignore file
├── LICENSE              # MIT License
├── README.md            # Project overview
├── contributing.md      # Contribution guidelines
├── env.py               # Environment configuration
├── mkdocs.yml           # Documentation configuration
├── python-package.yml   # CI/CD configuration
└── setup.py             # Package installation script
```

### Quick Start

```python
from aiflow import Workflow, OpenAIStep

# Define a simple workflow
workflow = Workflow(
    steps=[
        OpenAIStep(
            name="text_generation",
            model="gpt-3.5-turbo",
            prompt="Write a short story about a robot learning to paint.",
            temperature=0.7
        ),
        OpenAIStep(
            name="summarization",
            model="gpt-3.5-turbo",
            prompt="Summarize the following story in one paragraph: {{text_generation.output}}",
            temperature=0.3
        )
    ]
)

# Execute the workflow
result = workflow.run()
print(result["summarization"]["output"])
```

### Advanced Usage

#### Conditional Workflows

```python
from aiflow import Workflow, OpenAIStep, Condition

workflow = Workflow(
    steps=[
        OpenAIStep(
            name="sentiment_analysis",
            model="gpt-4",
            prompt="Analyze the sentiment of this text: '{{input_text}}'. Return POSITIVE, NEGATIVE, or NEUTRAL."
        ),
        Condition(
            name="sentiment_branch",
            condition="{{sentiment_analysis.output}} == 'POSITIVE'",
            if_true=OpenAIStep(
                name="positive_response",
                model="gpt-3.5-turbo",
                prompt="Generate an enthusiastic reply to: '{{input_text}}'"
            ),
            if_false=OpenAIStep(
                name="neutral_response",
                model="gpt-3.5-turbo",
                prompt="Generate a balanced, thoughtful reply to: '{{input_text}}'"
            )
        )
    ]
)
```

#### Data Transformation

```python
from aiflow import Workflow, OpenAIStep, Transform

workflow = Workflow(
    steps=[
        OpenAIStep(
            name="data_extraction",
            model="gpt-4",
            prompt="Extract key information from this text and format as JSON: '{{input_text}}'"
        ),
        Transform(
            name="json_to_dict",
            transform_function="json.loads({{data_extraction.output}})"
        ),
        OpenAIStep(
            name="personalized_response",
            model="gpt-3.5-turbo",
            prompt="Create a personalized message for {{json_to_dict.output.name}}"
        )
    ]
)
```

### Documentation

For comprehensive documentation, visit [https://kaushik701.github.io/AIFlow/](https://kaushik701.github.io/AIFlow/)

### Contributing

Contributions are welcome! Please read our [contributing guidelines](contributing.md) to get started.

### License

AIFlow is released under the [MIT License](LICENSE).

### Support

- GitHub Issues: [Report bugs or request features](https://github.com/kaushik701/AIFlow/issues)
- Documentation: [https://kaushik701.github.io/AIFlow/](https://kaushik701.github.io/AIFlow/)

### Acknowledgements

AIFlow was created to simplify the process of building complex AI workflows with OpenAI models. Special thanks to all contributors who have helped shape this project.
