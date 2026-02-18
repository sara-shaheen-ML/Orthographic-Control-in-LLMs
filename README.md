Orthographic Control in Large Language Models
Teaching Token-Based LLMs to Spell at the Character Level

Large Language Models can generate full reports, structured code, and coherent long-form reasoning — yet they may fail at a task taught in early primary school: spelling a single word correctly, letter by letter.

This repository accompanies our research on:

Why token-based LLMs struggle with character-level orthographic precision, and how far parameter-efficient fine-tuning (LoRA) can push this capability.

🔍 Motivation

LLMs are optimized for contextual fluency, not exact character reconstruction.

This leads to surprising behaviour:

spell: necessary
→ n e c e s a r y   ❌

spell: accommodation
→ a c o m o d a t i o n   ❌


This is not a reasoning failure — it is a representation and tokenization limitation.

However, in domains such as:

early literacy

spelling instruction

educational assessment

controlled generation

character-level accuracy is the task itself.

❓ Research Questions

Can token-based LLMs reliably perform character-level spelling?

Is the limitation caused by tokenization and contextual decoding?

Can parameter-efficient fine-tuning (LoRA) improve orthographic control without full retraining?

✨ Contributions

✔ A controlled evaluation pipeline for LLM spelling
✔ Character-level orthographic metrics
✔ Exact-match and error analysis
✔ LoRA fine-tuning for spelling adaptation
✔ Empirical evidence of:

significant improvement after PEFT

persistent unsolved failure modes

This shows that:

Orthographic knowledge exists in LLMs — but its externalization is unstable.

🧠 Method Overview

We evaluate spelling generation using:

1️⃣ Prompt-based inference

Zero-shot

Few-shot

2️⃣ Parameter-efficient fine-tuning

LoRA adaptation

Low training cost

No full model retraining

3️⃣ Evaluation metrics

Exact Match Accuracy

Character Error Rate (CER)

Position-wise character accuracy

Word-length generalization

📊 Example Outcome

LoRA significantly:

improves exact-match spelling

reduces character-level errors

stabilizes output format

But:

❗ The problem is not completely solved, revealing a deeper modeling limitation.

📂 Repository Structure
.
├── notebooks/        # Main experimental pipeline
├── data/             # Training and evaluation word lists
├── src/              # Training and evaluation scripts (optional modular version)
├── results/          # Output metrics and logs
├── figures/          # Plots used in the paper
├── requirements.txt
└── README.md

⚙️ Installation
git clone https://github.com/YOUR_USERNAME/orthographic-control-llm.git
cd orthographic-control-llm

pip install -r requirements.txt

▶️ Quick Start

Run the main experiment:

jupyter notebook notebooks/your_notebook.ipynb


or (if modular scripts are used):

python src/run_evaluation.py

🧪 Reproducing the Experiments

Prepare the dataset

Run baseline prompting evaluation

Fine-tune using LoRA

Run post-training evaluation

All steps are provided in the notebook for full reproducibility.

🎯 Key Insight

Scaling model size does not guarantee fine-grained control.

This project highlights a fundamental gap between:

semantic fluency
and

symbolic precision

🏫 Why This Matters

This research is particularly relevant for:

AI for education

controllable text generation

human-AI alignment at the symbolic level

tokenization design

character-aware language modeling

🔗 Paper & Citation

If you use this code, please cite:

@article{shaheen2026orthographic,
  title   = {Orthographic Control in Token-Based Large Language Models},
  author  = {Shaheen, Sara},
  year    = {2026}
}

🤝 Collaboration

I am currently expanding this research toward:

character-aware decoding strategies

hybrid token/character representations

educational LLM applications

If you are working in:

LLM controllability

PEFT methods

NLP for education

let’s collaborate.

📬 Author

Dr. Sara Shaheen
PhD in Computer Science – Artificial Intelligence
AI Researcher | LLMs | Computer Vision | AI for Education

Google Scholar: https://scholar.google.com/citations?user=pBgJOiEAAAAJ

⭐ If you find this useful

Star the repo, open an issue, or try the spelling test yourself 😄
