
chunk1 = [
    ["input: hello", "output: hello! iam intelligence team's bot how can i help you today?"],
    ["input: who are you", "output: I’m Intelligence team’s bot, a customized version of Gemini created to serve as an agent for the Intelligence team."],
    ["input: what is intelligence team", "output: A group of Computer Science and artificial intelligence students at Jordan University of Science and Technology collaborate to support the Computer Science department and its students."],
    ["input: who create intelligence app(this application)and customize this chat bot", "output: Intelligence app was developed in 2024 by Yosef Alsheikh Qasem and Dena Tayeh, both from the 2021 batch at Jordan University of Science and Technology."]
]

chunk2 = [
    ["input: where the x building is /where the x is", "output: With our app's location feature, you can find any building on campus."],
    ["input: where can i eat in the university", "output: You have several dining options available, including the Mall Cafeteria and the Stadium Cafeteria."],
    ["input: What is the total number of credit hours required for a degree in Computer Science, and how many credit hours are needed for a specialization in Artificial Intelligence? Additionally, how many years of study are typically required for each program?", "output: 132 hours, 4 years."],
    ["input: How to borrow a book from the library?", "output: You can borrow a book from the library for free using the self-service machines."],
    ["input: how to make an incomplete exam request?", "output: student services->incomplete exam request->select your excuse and upload a file if you have one."]
]

chunk3 = [
    ["input: can you send me x resource/any academic resource please?", "output: You can access our academic resources through the Intelligence app by navigating to Academic Resources."],
    ["input: who is albaraa shehadeh?", "output: a computer science graduate from 2019 batch and the 2nd leader of intelligence team."],
    ["input: How many faculties does Jordan University of Science and Technology have, and what are their names?", "output: 13 faculties."],
    ["input: What are the departments within the Faculty of Computer and Information Technology at Jordan University of Science and Technology, and what programs do they offer?", "output: The Faculty of Computer and Information Technology at Jordan University of Science and Technology comprises six departments."],
    ["input: How do I calculate my GPA?", "output: You can easily calculate your GPA using the GPA calculator feature in our app."],
    ["input: who is the founder of intelligence team?", "output: Intelligence team was founded by Suhaib Alabed."],
    ["input: what is the grading system in just(jordan university of science and technology)?", "output: Each course is graded on a 100-point scale."],
    ["input: how can i found x about x proffessor?", "output: To find detailed information about the academic staff, visit the university's website."],
    ["input: tell me the number of members in intelligence team and the names of computer science 2021 batch members.", "output: intelligence have 32 active members in total."]
]

data = [chunk1, chunk2, chunk3]

import nltk
from nltk.corpus import stopwords

# Download the stopwords if you haven't already
nltk.download('stopwords')

# Define stopwords (common meaningless words)
stop_words = set(stopwords.words('english'))

def find_most_relevant_chunk(user_input, data):
    max_similarity = 0
    most_relevant_chunk = None

    for chunk in data:
        for input_output_pair in chunk:
            input_prompt = input_output_pair[0]
            similarity = calculate_similarity(user_input, input_prompt)

            if similarity > max_similarity:
                max_similarity = similarity
                most_relevant_chunk = chunk

    return most_relevant_chunk

def calculate_similarity(text1, text2):
    # Remove stopwords from both texts
    words1 = set(word for word in text1.lower().split() if word not in stop_words)
    words2 = set(word for word in text2.lower().split() if word not in stop_words)

    # Calculate similarity by common words
    common_words = words1.intersection(words2)
    return len(common_words) / max(len(words1), len(words2))

user_input = "hi"
most_relevant_chunk = find_most_relevant_chunk(user_input, data)

if most_relevant_chunk:
    print("Most relevant chunk:", most_relevant_chunk)
    output = most_relevant_chunk[0][1]
    print("Response:", output)
else:
    print("No relevant chunk found.")
