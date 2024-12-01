from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from torch.nn.functional import softmax
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face access token from the environment
HF_ACCESS_TOKEN = os.getenv("HF_ACCESS_TOKEN")

# Ensure the token exists
if HF_ACCESS_TOKEN is None:
    raise ValueError("Hugging Face access token not found in environment variables")

# Load the tokenizer and model using the access token
tokenizer = AutoTokenizer.from_pretrained("google/shieldgemma-2b", token=HF_ACCESS_TOKEN)
model = AutoModelForCausalLM.from_pretrained(
    "google/shieldgemma-2b",
    torch_dtype=torch.float32,  # Use float32 for compatibility
    token=HF_ACCESS_TOKEN  # Pass the token to authenticate
).to("cpu")  # Use CPU since CUDA is not available


async def check_offensive_content(user_text):
    # Define the safety policy
    safety_policy = """
    * "No Dangerous Content": The prompt shall not contain or seek generation of content that is harmful to oneself and/or others (e.g., accessing or building firearms and explosive devices, promotion of terrorism, instructions for suicide).
    * "No Harassment": The prompt shall not contain or seek generation of content that is malicious, intimidating, bullying, or abusive content targeting another individual (e.g., physical threats, denial of tragic events, disparaging victims of violence).
    * "No Hate Speech": The prompt shall not contain or seek generation of content that targets identity and/or protected attributes (e.g., racial slurs, promotion of discrimination, calls to violence against protected groups) or dehumanizing/belittling/vilifying on the basis of race, ethnicity, religion, disability, age, nationality, veteran status, sexual orientation, gender, gender identity, caste, or any other protected status. We do allow content that includes a reference to a protected individual or group in a positive manner.
    * "No Sexually Explicit Information": The prompt shall not contain or seek generation of content that contains references to sexual acts or other lewd content (e.g., sexually graphic descriptions, content aimed at causing arousal). Medical or scientific terms related to human anatomy or sex education are permitted.
    """

    # Format the evaluation prompt
    prompt = f"""You are a policy expert trying to help determine whether a text
    contains offensive language in violation of the defined safety policies.

    <start_of_turn>
    Text to Evaluate: {user_text.strip()}
    <end_of_turn>

    Our safety principle is defined as follows:

    {safety_policy.strip()}

    Does the text violate the above principle? Your answer must start with 'Yes' or 'No'. Provide reasoning for your conclusion.
    """

    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt").to("cpu")  # Run on CPU

    with torch.no_grad():
        logits = model(**inputs).logits

    # Extract the logits for the Yes and No tokens
    vocab = tokenizer.get_vocab()
    selected_logits = logits[0, -1, [vocab['Yes'], vocab['No']]]

    # Convert these logits to a probability with softmax
    probabilities = softmax(selected_logits, dim=0)

    # Return probability of 'Yes'
    score = probabilities[0].item()
    return score > 0.01  # Return True if offensive, False if not offensive