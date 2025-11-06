#----------------------------------------------------------------------
# CCM CODE AI BLUEPRINT: AI FEEDBACK SUMMARIZER (PROOF OF CONCEPT)
#----------------------------------------------------------------------
# This script demonstrates the core NLP logic for the case study.
# It uses the Hugging Face 'transformers' library to perform
# abstractive summarization, turning a long text block into a
# concise summary.
#
# This is the logic that would be deployed inside the FastAPI endpoint.
#----------------------------------------------------------------------

# We use the high-level 'pipeline' for fast, effective results.
# This is the modern, standard-practice way to use these models.
from transformers import pipeline

def summarize_feedback(text_block):
    """
    Uses a pre-trained BART model to summarize a block of text.
    """
    print("--- Loading AI Summarization Model (one-time setup)...")
    # This model is excellent for summarizing articles and feedback.
    # It's an encoder-decoder model, which is why it's used for
    # summarization, as opposed to an encoder-only model like BERT.
    summarizer = pipeline("summarization", 
                          model="facebook/bart-large-cnn"
                          # use cpu
                          #,device=-1
                          )
    
    print("--- Model loaded. Generating summary...")
    
    # We set min/max length to ensure a useful, concise summary.
    summary = summarizer(text_block, 
                         max_length=150, 
                         min_length=30, 
                         do_sample=False)
    
    print("--- Summary Complete.")
    return summary[0]['summary_text']

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# EXAMPLE USAGE:
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

# This is a long block of text (over 200 words) that simulates
# unstructured feedback from a team survey or customer reviews.
long_feedback = """
The Q4 project was a mixed bag. On one hand, the new deployment pipeline
is significantly faster, and we appreciate the reduction in build times.
The documentation for the new microservice was clear and well-written.
However, we had significant issues with communication. Key decisions were
made in silos, and the product team was often out of sync with engineering.
Several critical dependencies were missed during the planning phase, leading
to a last-minute scramble. The weekly sync-ups were not effective and
often felt like a waste of time. We need a better system for tracking cross-team
dependencies and a clearer channel for escalating blockers. The tooling is
better, but the process needs a major overhaul if we're going to hit our
Q1 targets.
"""

print(f"Original Text Length: {len(long_feedback.split())} words")
print("-" * 20)

ai_summary = summarize_feedback(long_feedback)

print("\n" + "=" * 20)
print("AI-Generated Summary:")
print(ai_summary)
print(f"Summary Length: {len(ai_summary.split())} words")
print("=" * 20)