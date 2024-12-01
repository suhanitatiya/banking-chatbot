import pandas as pd
from transformers import pipeline
import os

class Chatbot:
    def __init__(self, dataset_path):
        print("Initializing Chatbot...")  # Confirm initialization

        # Debugging: Print absolute path of dataset
        absolute_path = os.path.abspath(dataset_path)
        print("Expected dataset path:", absolute_path)

        # Load dataset
        try:
            self.dataset = pd.read_csv(r"C:\chatbot-codes\banking-chatbot\data\dataset.csv")
            print("Dataset loaded successfully!")
            print("Dataset preview:", self.dataset.head())  # Show first few rows for verification
        except FileNotFoundError:
            print("FileNotFoundError: The dataset file is missing.")
            raise FileNotFoundError("Dataset file not found at the specified path.")
        except pd.errors.EmptyDataError:
            print("EmptyDataError: The dataset file is empty or corrupted.")
            raise pd.errors.EmptyDataError("Dataset file is empty or corrupted.")
        except Exception as e:
            print("Unexpected error while loading dataset:", e)
            raise e  # Re-raise exception to avoid silent failures

        # Initialize the LLM pipeline (e.g., Blenderbot)
        print("Loading the language model...")
        self.llm = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")
        print("Language model loaded successfully!")

    def get_response(self, user_input):
        print(f"Received user input: {user_input}")  # Debug user input

        # Search dataset for a match
        matched_responses = self.dataset[self.dataset['Query'].str.contains(user_input, case=False, na=False)]
        if not matched_responses.empty:
            print("Match found in dataset.")  # Debug match
            return matched_responses.iloc[0]['Response']
        else:
            print("No match found in dataset. Using language model.")  # Debug fallback
            # Generate response using the language model
            response = self.llm(user_input)[0]['generated_text']
            print(f"LLM response: {response}")  # Debug LLM response
            return response

if __name__ == "__main__":
    dataset_path = os.getenv("DATASET_PATH", r"C:\chatbot-codes\banking-chatbot\data\dataset.csv")
    chatbot = Chatbot(dataset_path)



    # Test a query
    user_query = "What is my account balance?"
    print(f"User Query: {user_query}")
    response = chatbot.get_response(user_query)
    print(f"Chatbot Response: {response}")

