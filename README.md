# XChat

A minimal chatbot for handling conversations.

## Features

- Basic chatbot responses
- Interactive **Gradio** UI
- Easily extendable with AI models

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sapk-pa1/chatbot.git
cd chatbot_project
```

### 2. Set Up a Virtual Environment

It is recommended to create a virtual environment before installing dependencies to ensure a clean workspace.

#### Using `venv` (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

#### Using `conda`

```bash
conda create --name xchat_env python=3.9
conda activate xchat_env
```

### 3. Configure Environment Variables

There is an `.env.example` file in the repository. Copy it to create a `.env` file and set up your API key.

```bash
cp .env.example .env
```

Edit the `.env` file and replace `your_gemini_api_key` with your actual API key:

```
GEMINI_API=your_gemini_api_key
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Chatbot

```bash
python app.py
```

Once the script runs, a **Gradio UI** will open in your browser. You can then start interacting with the chatbot.

## Future Enhancements

- Integration with **LLM models** for improved responses
- Implementation of a **memory system** for maintaining conversation context
- Deployment on **Hugging Face Spaces** or as a **Flask API**

## License

This project is licensed under the **AGPL 3.0 License**.

## Contact

For any questions or suggestions, reach out via [email](mailto:sapkotapawan099@gmail.com).
