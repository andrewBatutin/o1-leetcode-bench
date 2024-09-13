# LeetCode Benchmark for Language Models

This project is a simple benchmark tool to test and compare the performance of various language models (OpenAI, OpenAI O1, and Anthropic) on LeetCode problems.

## Overview

The benchmark tool processes LeetCode problems stored as Markdown files, sends them to different language models, and saves the generated solutions. It allows for easy comparison of solution quality across different models.

## Features

- Supports multiple language models:
  - OpenAI (GPT-4 and variants)
  - OpenAI O1 (Preview and Mini)
  - Anthropic (Claude)
- Processes LeetCode problems from Markdown files
- Generates Python solutions for each problem
- Organizes results in a structured folder hierarchy

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ANTHROPIC_API_KEY=your_anthropic_api_key
     ```

## Usage

1. Place your LeetCode problem descriptions in Markdown format in the `resources` folder.
2. Run the benchmark:
   ```
   python src/leetcode_benchmark.py
   ```
3. Results will be saved in the `result` folder, organized by model type, model name, and task name.

## Project Structure

- `src/leetcode_benchmark.py`: Main script containing the benchmark logic
- `resources/`: Folder for storing LeetCode problem descriptions
- `result/`: Output folder for generated solutions
- `requirements.txt`: List of Python dependencies

## Benchmark Results



| Difficulty                                                                                   | o1-preview     | o1-mini                | gpt-4o-mini            | gpt-4o         | claude-3-5-sonnet-20240620 |
|----------------------------------------------------------------------------------------------|----------------|------------------------|------------------------|----------------|----------------------------|
| [easy](https://leetcode.com/problems/convert-date-to-binary/description/)                    | ✅              | ✅                      | ✅                      | ✅              | ✅                          |
| [medium](https://leetcode.com/problems/reach-end-of-array-with-max-score/description/)       | ❌ Wrong Answer | ⌛️ Time Limit Exceeded | ⌛️ Time Limit Exceeded | ❌ Wrong Answer | ⌛️ Time Limit Exceeded     |
| [hard](https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/description/) | ✅              | ✅                      | ❌ Wrong Answer         | ❌ Wrong Answer | ❌ Wrong Answer             |


## Customization

You can modify the `list_of_models` dictionary in `src/leetcode_benchmark.py` to add or remove models for benchmarking.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

