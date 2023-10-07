################################################################################
### Step 1
################################################################################


import os
import pandas as pd
import openai
import numpy as np
from openai.embeddings_utils import distances_from_embeddings
from ast import literal_eval

def init_api():
     with open(".env") as env:
         for line in env:
             key, value = line.strip().split("=")
             os.environ[key] = value

     openai.api_key = os.environ.get("API_KEY")
     openai.organization = os.environ.get("ORG_ID")
init_api()

class ChatGpt:
    def __init__(self):
        self.state = "LOADING"
        
    
    def load_data(self):
        self.df=pd.read_csv('processed/embeddings.csv', index_col=0)
        self.df['embeddings'] = self.df['embeddings'].apply(literal_eval).apply(np.array)
        self.df.head()
        self.state = "READY"


    def create_context(
        self,question, df, max_len=1800, size="ada"
    ):
        """
        Create a context for a question by finding the most similar context from the dataframe
        """

        # Get the embeddings for the question
        q_embeddings = openai.Embedding.create(input=question, engine='text-embedding-ada-002')['data'][0]['embedding']

        # Get the distances from the embeddings
        self.df['distances'] = distances_from_embeddings(q_embeddings, df['embeddings'].values, distance_metric='cosine')


        returns = []
        cur_len = 0

        # Sort by distance and add the text to the context until the context is too long
        for i, row in df.sort_values('distances', ascending=True).iterrows():
            
            # Add the length of the text to the current length
            cur_len += row['n_tokens'] + 4
            
            # If the context is too long, break
            if cur_len > max_len:
                break
            
            # Else add it to the text that is being returned
            returns.append(row["text"])

        # Return the context
        return "\n\n###\n\n".join(returns)

    def answer_question(
        self,
        model="gpt-3.5-turbo-instruct",
        question="Am I allowed to publish model outputs to Twitter, without a human review?",
        max_len=1800,
        size="ada",
        debug=False,
        max_tokens=150,
        stop_sequence=None
    ):
        """
        Answer a question based on the most similar context from the dataframe texts
        """
        context = self.create_context(
            question,
            self.df,
            max_len=max_len,
            size=size,
        )
        # If debug, print the raw model response


        try:
            # Create a completions using the questin and context
            response = openai.Completion.create(
                prompt=f"Answer the question based on the context below, and if the question can't be answered based on the context, say \"I don't know\"\n\nContext: {context}\n\n---\n\nQuestion: {question}\nAnswer:",
                temperature=0,
                max_tokens=max_tokens,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=stop_sequence,
                model=model,
            )
            return response["choices"][0]["text"].strip()
        except Exception as e:
            print(e)
            return ""


if __name__ == "__main__":
    chat = ChatGpt()

    print(chat.answer_question(question="What day is it?", debug=False))

    print(chat.answer_question(question="What is our newest embeddings model?"))