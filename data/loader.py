from datasets import load_dataset
import pandas as pd
import os

def fetch_med_dialog_sample(limit=5):
    """
    Fetches a small sample from the MedDialog dataset to use as context.
    """
    print(f"Fetching {limit} dialogues from MedDialog...")
    try:
        # Loading a small portion of the English MedDialog dataset
        dataset = load_dataset("OpenMed/MedDialog", split="train", streaming=True)
        samples = []
        for i, entry in enumerate(dataset):
            if i >= limit:
                break
            samples.append(entry)
        
        return samples
    except Exception as e:
        print(f"Error fetching dataset: {e}")
        return []

def format_dialogue_context(samples):
    context = "Here are some examples of medical dialogues for reference:\n\n"
    for sample in samples:
        # Adjust based on actual dataset structure (checking common fields)
        dialogue = sample.get('utterances', sample.get('description', ''))
        context += f"- {dialogue}\n"
    return context

if __name__ == "__main__":
    # Test fetch
    data = fetch_med_dialog_sample(2)
    print(format_dialogue_context(data))
