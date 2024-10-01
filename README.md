Web-Based Agent using Streamlit
Setup Instructions
1. Create and Activate Virtual Environment
First, create a Python virtual environment and activate it. You can do this using the following commands:

# Create virtual environment
python -m venv env

# Activate virtual environment (Windows)
.\env\Scripts\activate

# Activate virtual environment (Mac/Linux)
source env/bin/activate
2. Install Dependencies
Once the virtual environment is activated, install the required dependencies by running:

pip install -r requirements.txt
3. Create .env File
You need to create a .env file in the root directory of your project to store your API keys and environment variables.

Create the .env file and add your OpenAI API key like this:

makefile
OPENAI_API_KEY=your-openai-key-here
4. Run the Application
After completing the above steps, run the Streamlit application using the following command:

streamlit run app.py
Now you should be able to access the web-based agent via the Streamlit interface!
