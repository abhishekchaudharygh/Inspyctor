from transformers import AutoTokenizer, AutoModelForCausalLM


def analyze_code_with_ai(code):
    """
    Analyze Python code using a free Hugging Face model.
    """
    try:
        # Load pre-trained model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained("codeparrot/codegen-350M-mono")
        model = AutoModelForCausalLM.from_pretrained("codeparrot/codegen-350M-mono")

        # Prepare the input
        prompt = (
            "Review the following Python code and provide suggestions for improvement:\n\n"
            f"{code}\n\n"
        )
        inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)

        # Generate a response
        outputs = model.generate(
            inputs["input_ids"], max_length=512, temperature=0.7, do_sample=True
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return response.strip()
    except Exception as e:
        return f"Error while analyzing code with AI: {str(e)}"
