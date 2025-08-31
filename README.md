```markdown
# Deep Research System

## Overview

This project implements a multi-agent deep research system designed to simulate the workflow of professional researchers. It can break down complex questions, gather information from multiple sources, synthesize findings, and generate comprehensive reports with citations. The system is built with Python and is designed to be compatible with Windows operating systems.

## Features

*   **Lead Researcher:** Orchestrates the entire research process, delegates tasks to other agents, and compiles the final report.
*   **Planning Agent:** Breaks down complex research questions into smaller, manageable sub-tasks.
*   **FactFinder:** Gathers raw information related to specific tasks, simulating web searches.
*   **SourceChecker:** Evaluates the reliability of information sources (simulated based on URL domain).
*   **Summarizer:** Condenses raw findings into concise summaries.
*   **Synthesis Reporter:** Combines and organizes findings from various agents into a coherent synthesis.
*   **Report Writer:** Formats the synthesized information and citations into a professional research report.

## Setup and Installation

### Prerequisites

*   **Python 3.10+:** Ensure you have Python version 3.10 or newer installed on your system. Download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
*   **API Keys:** You will need API keys for the following services:
    *   **Tavily API Key:** For web search capabilities. Obtain yours from [https://tavily.com/](https://tavily.com/).
    *   **OpenAI API Key:** For advanced language model (LLM) capabilities (e.g., text generation, summarization, translation).

### Step-by-Step Installation

1.  **Clone the Repository:**

    Open your terminal or command prompt and run the following command:

    ```bash
    git clone [YOUR_REPOSITORY_URL_HERE]
    cd [YOUR_REPOSITORY_NAME]
    ```

    *(Replace `[YOUR_REPOSITORY_URL_HERE]` with the actual URL of this repository and `[YOUR_REPOSITORY_NAME]` with the name you choose for the cloned directory.)*

2.  **Create a Virtual Environment (Recommended):**

    It's good practice to create a virtual environment to manage project dependencies. This prevents conflicts with other Python projects on your system.

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**

    *   **On Windows (Command Prompt):**

        ```bash
        .\venv\Scripts\activate.bat
        ```

    *   **On Windows (PowerShell):**

        ```bash
        .\venv\Scripts\Activate.ps1
        ```

    *   **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**

    With your virtual environment activated, install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    *(This will install `python-dotenv` and `tavily-python`.)*

5.  **Configure API Keys:**

    Create a file named `.env` in the root directory of the project (the same directory where `deep_research_system.py` is located). Add your API keys to this file in the following format:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    TAVILY_API_KEY=your_tavily_api_key_here
    ```

    Replace `your_openai_api_key_here` and `your_tavily_api_key_here` with your actual API keys.

## How to Use the System

To initiate a research query, you will run the `deep_research_system.py` script from your terminal. The system is designed to be run from the command line.

1.  **Navigate to the Project Directory:**

    Ensure your terminal is in the root directory of the project where `deep_research_system.py` is located.

2.  **Execute the Script:**

    You can modify the `if __name__ == '__main__':` block in `deep_research_system.py` to change the research query. By default, it's set to:

    ```python
    if __name__ == '__main__':
        lead_researcher = LeadResearcher()
        report = lead_researcher.conduct_research("Compare the environmental impact of electric vs hybrid vs gas cars")
        print("\n--- Final Research Report ---\n")
        print(report)
    ```

    Modify the `conduct_research` call with your desired research question.

### Understanding the Output

As the system runs, you will see print statements in your terminal indicating which agent is performing what task. This provides a basic tracing mechanism to understand the research process. Finally, a comprehensive research report will be printed to the console, including synthesized findings and simulated citations.

## Example Research Questions

Here are some example research questions you can use to test the system at different complexity levels:

### Level 1: Basic Research

*   "What are the benefits of electric cars?"

### Level 2: Comparative Analysis

*   "Compare the environmental impact of electric vs hybrid vs gas cars"

### Level 3: Complex Investigation

*   "How has artificial intelligence changed healthcare from 2020 to 2024, including both benefits and concerns from medical professionals?"

### Level 4: Expert Challenge

*   "Analyze the economic impact of remote work policies on small businesses vs large corporations, including productivity data and employee satisfaction trends"

## Troubleshooting

*   **`TAVILY_API_KEY not found` error:** Ensure you have created the `.env` file in the correct directory and that the `TAVILY_API_KEY` variable is set correctly within it.
*   **`ModuleNotFoundError`:** Make sure you have activated your virtual environment and installed all dependencies using `pip install -r requirements.txt`.
*   **No output or unexpected behavior:** Review the `deep_research_system.py` file and the individual agent files (`research_agents.py`, `planning_agent.py`, etc.) to understand the simulated logic. For real-world research, you would integrate actual API calls and more sophisticated NLP models.

## Future Enhancements

This system provides a strong foundation for a deep research agent. Potential future enhancements include:

*   Integration with actual web search APIs (beyond basic Tavily).
*   Advanced natural language processing (NLP) for more sophisticated summarization and synthesis.
*   Conflict detection and resolution mechanisms for contradictory information.
*   A more robust citation management system.
*   A graphical user interface (GUI) for easier interaction.

---

*Manus AI, August 2025*
```

