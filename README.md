### Made by Diego Pacheco
# LangGraph Template 

A basic template for building intelligent agents using LangGraph with memory persistence and tool usage capabilities.

## Overview

This project provides a template for creating conversational AI agents with LangGraph. It features:

- A graph-based workflow for agent decision-making
- Built-in arithmetic operation tools
- Memory capabilities for storing and retrieving user preferences
- Error handling mechanisms

## Installation

### Prerequisites

- Python 3.11+
- pip (Python package installer)

### Setup

1. **Clone the repository:**

    ```bash
   git clone https://github.com/dpacheco2001/LangGraphTemplate.git
   cd LangGraphTemplate
   ```

2. **Create a virtual environment:**

    ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**

    ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** with your API keys:

   ```ini
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

Run the main application:

```bash
python app/main.py
```

The application starts an interactive chat session where you can:

- Ask the agent to perform arithmetic operations
- Type `see_memory` to view stored memories
- Type `exit` to close the application

### Example Interaction

```bash
Enter a message: Can you multiply 5 and 6? 

--------------------------

Human:  Can you multiply 5 and 6?

--------------------------

Assistant:  The result of multiplying 5 and 6 is 30.

--------------------------

Enter a message: add 289 and then, the result divide it by 7  

--------------------------

Human:  add 289 and then, the result divide it by 7

--------------------------

Assistant:  First, I added 289 and 30, which gives us 319. Then, dividing 319 by 7 results in approximately 45.57.

--------------------------

Enter a message: Please remember that I prefer detailed explanations 

--------------------------

Human:  Please remember that I prefer detailed explanations

--------------------------

Assistant:  I've noted that you prefer detailed explanations. I'll make sure to provide more thorough responses in the future! If you have any more questions or need assistance, feel free to ask.     

--------------------------

Enter a message: see_memory

------------Memories stored-------------

[Item(namespace=['memories', '1'], key='7d738310-089c-43c3-903f-9f82d78ad985', value='User prefers detailed explanations.', created_at='2025-03-13T22:42:44.751191+00:00', updated_at='2025-03-13T22:42:44.751191+00:00', score=None)]

------------Memories stored-------------

Enter a message: now, multiply 130 x 180  

--------------------------

Human:  now, multiply 130 x 180

--------------------------

Assistant:  The result of multiplying 130 by 180 is 23,400.

Here's a breakdown of the multiplication:
- You can think of it as (130 × 180 = 130 × (100 + 80)).
- This can be calculated as ((130 × 100) + (130 × 80)).
- So, (130 × 100 = 13,000) and (130 × 80 = 10,400).
- Adding those together gives (13,000 + 10,400 = 23,400).

If you have any more questions or need further assistance, just let me know!

--------------------------
```

## Project Structure

```bash
LangGraphTemplate/
├── .env                    # Environment variables (API keys)
├── requirements.txt        # Python dependencies
├── app/
│   ├── main.py             # Application entry point
│   └── myagent/            # Agent implementation
│       ├── graph.py        # Graph definition and compilation
│       └── utils/          # Utility modules
│           ├── configuration.py  # Agent configuration
│           ├── models.py         # LLM models setup
│           ├── nodes_edges.py    # Graph nodes and edges
│           ├── prompts.py        # System prompts
│           ├── state.py          # State management
│           └── tools.py          # Tool definitions

```

### Key Components
- **Graph:** The main workflow defined in `graph.py` 
- **Tools:** Tools are defined here with the decorator @tool
- **State Management:** Uses extended `MessagesState` for maintaining conversation context
- **Models:** Configurable LLM integration with tool binding

## Contributing

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Submit a pull request**


