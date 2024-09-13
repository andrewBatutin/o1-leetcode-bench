import os
from openai import OpenAI
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

list_of_models = {
    "open_ai_o1": ["o1-preview", "o1-mini"],
    "open_ai": ["gpt-4o-mini", "gpt-4o"],
    "anthropic": ["claude-3-5-sonnet-20240620"]
}

# Initialize OpenAI and Anthropic clients
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
open_ai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_file_content(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    return content


def generate_openai_response(prompt, model):
    response = open_ai_client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

def generate_openai_legacy_response(prompt, model):
    response = open_ai_client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ],
        temperature=0.01,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )
    return response.choices[0].message.content

def generate_anthropic_response(prompt, model):
    message = anthropic_client.messages.create(
        model=model,
        max_tokens=4096,
        temperature=0.01,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )
    return message.content[0].text

def get_llm_results(prompt, task_name):
    results = []
    for model_type, models in list_of_models.items():
        for model in models:
            if model_type == "open_ai":
                solution = generate_openai_legacy_response(prompt, model)
                result_type = "open_ai_legacy"
            elif model_type == "open_ai_o1":
                solution = generate_openai_response(prompt, model)
                result_type = "open_ai"
            elif model_type == "anthropic":
                solution = generate_anthropic_response(prompt, model)
                result_type = "anthropic"
            
            results.append({
                "model": model,
                "task": task_name,
                "solution": solution,
                "result_type": result_type
            })
    
    return results

def write_results_to_filesystem(results, result_folder):
    for result in results:
        folder = os.path.join(result_folder, result["result_type"], result["model"], result["task"])
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "solution.md"), "w") as f:
            f.write(result["solution"])
        
        print(f"Model: {result['model']}")
        print(f"Task: {result['task']}")
        print("Solution saved to:", os.path.join(folder, "solution.md"))
        print("\n" + "="*50 + "\n")

def process_leetcode_files():
    resource_folder = "resources"
    result_folder = "result"

    for filename in os.listdir(resource_folder):
        if filename.endswith(".md"):
            file_path = os.path.join(resource_folder, filename)
            content = read_file_content(file_path)
            
            prompt = f"Given the following LeetCode problem, provide a Python solution:\n\n{content}"
            task_name = os.path.splitext(filename)[0]
            
            results = get_llm_results(prompt, task_name)
            write_results_to_filesystem(results, result_folder)

if __name__ == "__main__":
    process_leetcode_files()
