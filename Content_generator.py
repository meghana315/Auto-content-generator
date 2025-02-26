from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def generate_adventure_story(prompt, max_length=800):
    """
    Generates an adventure story based on the given prompt using GPT-2.

    Args:
        prompt (str): The starting text for the story.
        max_length (int): The maximum length of the generated story.

    Returns:
        str: The generated adventure story.
    """
    # Load GPT-2 model and tokenizer
    model_name = "gpt2-xl"  # Use "gpt2" if memory is a concern
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Ensure padding token is set
    tokenizer.pad_token = tokenizer.eos_token

    # Encode the input prompt
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Generate story
    output = model.generate(
        inputs,
        max_length=max_length,
        do_sample=True,
        top_p=0.92,
        temperature=0.8,
        no_repeat_ngram_size=4,
        repetition_penalty=1.3,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

    # Decode and clean up the generated text
    story = tokenizer.decode(output[0], skip_special_tokens=True).replace(prompt, "").strip()
    
    return story

if __name__ == "__main__":
    # Example prompt
    user_prompt = """The jungle was alive with the sounds of insects and distant howls. 
    Alex wiped the sweat from his brow, his machete slicing through the thick vines blocking his path. 
    Suddenly, the ground beneath him trembled..."""

    # Generate and print the story
    story = generate_adventure_story(user_prompt)
    print("Generated Adventure Story:\n")
    print(story)
