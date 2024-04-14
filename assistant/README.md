## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/velocitatem/ai_sales_bot.git
   cd ai_sales_bot
   cd assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Bot

To start the AI sales bot, run:

```bash
streamlit run main.py
```

You can also configure `company.yaml` with details of your company to tailor for specific needs.

## How Does It Work?

The YOE AI Sales Bot operates through a combination of advanced AI models and user-friendly interfaces, designed to streamline the experience for both customers and administrators. Here’s a step-by-step breakdown of how the system functions:

### 1. Initialization and Configuration:
- **Initialization**: Upon launching the application, the system initializes by setting up the AI Sales Bot using the `OpenAIAssistantRunnable` with a specified assistant ID. This setup includes establishing a connection with the AI service and preparing the bot for interaction.
- **System Setup**: The system retrieves essential information such as the system language, current time, and user location to customize the interaction based on the client's environment.

### 2. User Interaction:
- **Input Handling**: Through a Streamlit interface, users can input their questions or requests into a chat input box. This input is then processed by the bot.
- **AI Processing**: The AI Sales Bot, powered by the `AgentExecutor`, receives the user input and processes it within the context of previous conversations (maintained in a session state) and the initial configuration. It uses this information to generate an appropriate response.

### 3. Dynamic Response Generation:
- **AI Response**: The bot's response is generated based on the model's understanding of the input and the context of the conversation. This includes detecting emotions, understanding queries, and providing detailed answers.
- **Display**: Responses from the AI are displayed back to the user in the chat interface, facilitating a natural conversation flow.

### 4. Session Management:
- **Message Tracking**: All messages are stored in a session state to keep track of the conversation history, allowing the bot to provide contextually relevant responses.
- **Thread Management**: The system maintains a unique thread for each user session, allowing it to manage and store conversation threads efficiently, ensuring continuity in interactions over time.

### 5. Resource Management:
- **Cached Resources**: Utilizing `st.cache_resource()`, the system efficiently handles resource-intensive tasks such as loading configuration files or initializing the AI model, thereby speeding up response times and reducing system load.

### 6. Additional Features:
- **Sidebar Information**: The Streamlit sidebar is used to display key company information such as the mission statement, headquarters location, and a direct link to the company’s website, enhancing user engagement and providing useful context.

This architecture ensures that the YOE AI Sales Bot not only delivers high-quality, personalized interactions but also does so with efficiency and scalability in mind.
