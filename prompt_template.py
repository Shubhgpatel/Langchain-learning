from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""You are an expert research paper explainer. Summarize the research paper "{paper_input}" in a {style_input} style.

Your summary should include:
1. **Core Idea**: What problem does this paper solve?
2. **Key Contributions**: What are the main innovations?
3. **How It Works**: Explain the methodology using the requested style:
   - If Math-Oriented: include relevant equations and mathematical intuition.
   - If Code-Based: include short Python pseudocode or snippets to illustrate concepts.
   - If Beginner Friendly: use simple real-world analogies and avoid heavy jargon.
4. **Impact**: Why does this paper matter in the field of AI/ML?

Keep the summary concise but insightful (around 300-400 words).
""",
    input_variables=['paper_input', 'style_input'],
    validate_template=True
)

template.save("template.json")