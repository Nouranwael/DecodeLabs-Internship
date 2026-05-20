# 🤖 Rule-Based AI Chatbot

> **DecodeLabs — Week 1 Internship Project**

A simple yet functional chatbot built with **Python** that uses predefined rules to understand what you say and respond accordingly. No machine learning or external libraries needed — just clean Python logic!

---

## 📝 Short Description

This chatbot works by matching your input against a set of known phrases (called **intents**) stored in a Python dictionary. When you type something like `"hello"` or `"tell me a joke"`, it finds the matching intent and replies with a predefined response. If it doesn't understand your input, it gives a friendly fallback message suggesting what you can try.

---

## ✨ Features

- **Greeting recognition** — responds to "hello", "hi", "hey", "hola", and more.
- **Self-awareness** — can tell you its name and what it can do.
- **Joke telling** — ask for a joke and get a programmer-themed laugh! 🐛
- **Thank-you handling** — politely acknowledges your gratitude.
- **Weather intent** — a placeholder response ready for future upgrades.
- **Creator info** — tells you who built it.
- **Graceful exit** — type "bye", "exit", or "quit" to leave the chat.
- **Input cleaning** — handles extra spaces and uppercase letters automatically.
- **Empty input handling** — prompts you to type something if you press Enter without input.
- **Fallback response** — gives a helpful suggestion when it doesn't understand you.

---

## 📋 Requirements

| Requirement | Details             |
|-------------|---------------------|
| Language    | Python 3.x          |
| Libraries   | None (standard library only) |
| OS          | Windows, macOS, or Linux |

> **Note:** No external packages need to be installed. If you have Python installed, you're good to go!

### How to check if Python is installed

Open a terminal or command prompt and type:

```bash
python --version
```

If you see something like `Python 3.x.x`, you're ready. If not, download Python from [python.org](https://www.python.org/downloads/).

---

## 🚀 How to Run the Project

1. **Open a terminal / command prompt.**

2. **Navigate to the project folder:**
   ```bash
   cd "C:\Users\Admin\Downloads\DecodeLabs Proj. 1"
   ```

3. **Run the chatbot:**
   ```bash
   python chatbot.py
   ```

4. **Start chatting!** Type your message and press Enter. Type `bye`, `exit`, or `quit` to end the conversation.

---

## 💬 Example Inputs and Outputs

```
==================================================
   🤖  Rule-Based AI Chatbot  🤖
   Type 'bye', 'exit', or 'quit' to leave.
==================================================

You: hello
ChatBot: Hello! 👋 Welcome! How can I help you today?

You: what is your name
ChatBot: I'm ChatBot v1.0 — a simple rule-based AI assistant built with Python! 🤖

You: tell me a joke
ChatBot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂

You: how are you
ChatBot: I'm just a program, but I'm running smoothly! 😄 How about you?

You: thanks
ChatBot: You're welcome! Happy to help! 😊

You: what's the meaning of life
ChatBot: 🤔 I'm sorry, I don't understand that yet. Try saying 'hello', 'joke', or 'help' to see what I can do!

You: bye
ChatBot: Goodbye! 👋 It was nice chatting with you. See you next time!
```

---

## ⚙️ How the Chatbot Works

Here's a step-by-step breakdown of the logic:

### 1. Knowledge Base (Dictionary)
All the chatbot's knowledge lives in a Python dictionary called `responses`. Each entry maps a **tuple of keywords** (the things a user might say) to a **response string** (what the bot replies).

```python
responses = {
    ("hello", "hi", "hey"): "Hello! 👋 Welcome!",
    ("tell me a joke", "joke"):  "Why do programmers prefer dark mode? ...",
    # ... more intents
}
```

### 2. Input Cleaning
When you type something, the program:
- Removes extra spaces with `.strip()`
- Converts everything to lowercase with `.lower()`

This means `"  HELLO  "` becomes `"hello"` — so matching works regardless of formatting.

### 3. Intent Matching
The `get_response()` function loops through every key in the dictionary. If your cleaned input matches any keyword in a tuple, it returns the paired response.

### 4. Fallback Response
If no intent matches your input, the bot returns a default message suggesting things you *can* ask.

### 5. Chat Loop
The `main()` function runs a `while True` loop that:
- Reads your input
- Cleans it
- Checks if it's an exit command (`bye`, `exit`, `quit`, etc.)
- Otherwise, looks up and prints the matching response

### Flow Diagram

```
┌─────────────────────┐
│   Program Starts    │
│  (Welcome Banner)   │
└────────┬────────────┘
         ▼
┌─────────────────────┐
│  Wait for User      │◄──────────────────┐
│  Input              │                    │
└────────┬────────────┘                    │
         ▼                                 │
┌─────────────────────┐                    │
│  Clean Input        │                    │
│  (strip + lower)    │                    │
└────────┬────────────┘                    │
         ▼                                 │
┌─────────────────────┐    Yes             │
│  Empty Input?       ├──────► Print       │
│                     │      "Type         │
└────────┬────────────┘      something!"───┘
         │ No                              │
         ▼                                 │
┌─────────────────────┐    Yes             │
│  Exit Command?      ├──────► Print       │
│                     │      "Goodbye!" ──►│ END
└────────┬────────────┘                    │
         │ No                              │
         ▼                                 │
┌─────────────────────┐                    │
│  Match Intent in    │                    │
│  Dictionary         │                    │
└────────┬────────────┘                    │
         ▼                                 │
┌─────────────────────┐                    │
│  Print Response     │                    │
│  (or Fallback)      ├───────────────────►┘
└─────────────────────┘
```

---

## 🔮 Future Improvement Ideas

Here are some ways this project could be expanded:

| Idea | Description |
|------|-------------|
| **Partial / fuzzy matching** | Use substring matching or the `difflib` library so the bot understands inputs like `"helo"` (typos). |
| **Multiple responses per intent** | Store a list of responses per intent and pick one at random for variety. |
| **Conversation memory** | Remember the user's name or previous messages for a more personal experience. |
| **Time & date** | Use Python's `datetime` module to tell the user the current time or date. |
| **Live weather** | Integrate a weather API (e.g., OpenWeatherMap) to give real forecasts. |
| **GUI interface** | Build a graphical chat window using `tkinter` or a web interface with Flask. |
| **File-based knowledge** | Load intents from a JSON or CSV file so non-programmers can add responses. |
| **Sentiment detection** | Detect if the user is happy, sad, or frustrated and adjust responses. |
| **NLP upgrade** | Use libraries like `spaCy` or `NLTK` for smarter natural language understanding. |
| **Voice input** | Add speech recognition with the `speech_recognition` library. |

---

## 📁 Project Structure

```
DecodeLabs Proj. 1/
├── chatbot.py      # Main chatbot source code
└── README.md       # Project documentation (this file)
```

---

## 📄 License

This project was created as part of a learning internship. Feel free to use, modify, and share it!

---
