# bookGPT

This script generates a book with a given subject and number of chapters, using OpenAI's GPT-3 natural language processing API. The book is saved in Markdown format.

## Installation

Before running the script, you need to install the openai library. You can do this by running:

```
pip install -r requirements.txt

```

You will also need an OpenAI API key, which you can obtain from the OpenAI website.

## Usage

To run the script, use the following command:

```
python book.py

```

You will be prompted to enter the subject of the book and the number of chapters to generate.

After generating the book, it will be saved in a new folder named output in the same directory as the script.

## Parameters

The script has the following parameters:

- subject: The subject of the book. This is entered by the user when prompted.
- num_chapters: The number of chapters to generate. This is entered by the user when prompted.
- chapter_titles: A list of the titles of the generated chapters.
- chapter_content: A list of the content of the generated chapters, in Markdown format.

## License

This script is released under the MIT License.
