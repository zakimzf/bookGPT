import openai
import time
import re

openai.api_key = "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"

def generate_chapters(subject, num_chapters):
    # Generate book title
    prompt = (f"Title: A book about {subject}\n"
              "Introduction:\n")
    title = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=50
    ).choices[0].text.strip()

    # Generate chapter titles and content
    chapter_titles = []
    chapter_content = []
    for i in range(num_chapters):
        chapter_title = openai.Completion.create(
            engine="text-davinci-002",
            prompt=(f"Chapter {i+1}: The {subject}\n"
                    "Introduction:\n"),
            temperature=0.5,
            max_tokens=30
        ).choices[0].text.strip()
        chapter_titles.append(chapter_title)

        chapter_text = ""
        while len(chapter_text) < 500:
            prompt = (f"Chapter {i+1}: {chapter_title}\n"
                      "Content:\n")
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                temperature=10,
                max_tokens=1024,
                n=1,
                stop=None,
                timeout=20,
            )
            chapter_text += response.choices[0].text
        chapter_content.append(chapter_text)

    # Display chapter titles and ask for confirmation
    print(f"Generated {num_chapters} chapters for a book about {subject} with the following titles:")
    for i, title in enumerate(chapter_titles):
        print(f"{i+1}. {title}")
    print("\n")

    while True:
        response = input("Are you satisfied with the generated chapters? (y/n) ")
        if response.lower() == "y":
            break
        elif response.lower() == "n":
            chapter_titles, chapter_content = generate_chapters(subject, num_chapters)
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return chapter_titles, chapter_content


def save_book(subject, chapter_titles, chapter_content):
    # Format chapter content as Markdown
    formatted_content = ""
    for i, content in enumerate(chapter_content):
        formatted_content += f"## {chapter_titles[i]}\n\n{content}\n\n"

    # Save book to file
    timestamp = int(time.time())
    filename = f"{subject}_book_{timestamp}.md"
    with open(filename, "w") as f:
        f.write(f"# {subject}: A Book\n\n")
        f.write(formatted_content)

    print(f"Book saved to {filename}")


if __name__ == "__main__":
    subject = input("Enter the subject of the book: ")
    num_chapters = int(input("Enter the number of chapters to generate: "))
    chapter_titles, chapter_content = generate_chapters(subject, num_chapters)
    save_book(subject, chapter_titles, chapter_content)
