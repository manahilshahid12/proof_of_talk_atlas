from transformers import pipeline

def generate_local_summary(text, model_name="facebook/bart-large-cnn"):
    """
    Generate a summary for the given text using a local model.
    Args:
        text (str): The input text to summarize.
        model_name (str): The Hugging Face model to use (default: bart-large-cnn).
    Returns:
        str: The generated summary.
    """
    summarizer = pipeline("summarization", model=model_name)
    summary = summarizer(text, max_length=60, min_length=10, do_sample=False)
    return summary[0]["summary_text"]

if __name__ == "__main__":
    # Example usage
    input_text = (
        "Person A: Amara Okafor, allocator, Goal: Deploy $200M into tokenised real-world assets with institutional partners. "
        "Person B: Marcus Chen, builder, Goal: Scale custody infrastructure globally and onboard institutional clients. "
        "Meeting Value Score: 0.85. "
        "Create a short professional pre-meeting only 1-line brief explaining: Who they are, Why they match, Suggested discussion points."
    )
    summary = generate_local_summary(input_text)
    print("Summary:", summary)
