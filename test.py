class RecommendedResourcesDatabase:
    def __init__(self):
        self.resources = {}
       
        

    def add_resource(self, topic, resources):
        self.resources[topic] = resources
   

class ToDoList:
    def __init__(self):
        self.resource_db = RecommendedResourcesDatabase()

        self.topics = {
            "Adaptability": [
                "Describe a major change that occurred in a job that you held. How did you adapt to this change?",
                "Tell us about a situation in which you had to adjust to changes over which you had no control. How did you handle it?",
                "Tell us about a time that you had to adapt to a difficult situation.",
            ],
            "Ambition": [
                "Describe a project or idea that was implemented primarily because of your efforts. What was your role?.What was the outcome?",
                "Describe a time when you made a suggestion to improve the work in your organization.",
                "Give an example of an important goal that you set in the past. Tell about your success in reaching it.",
                "Give two examples of things you’ve done in previous jobs that demonstrate your willingness to work hard.",
                "How many hours a day do you put into your work? What were your study patterns at school?",
                "Tell us about a time when you had to go above and beyond the call of duty in order to get a job done.",
                "Tell us about a time when a job had to be completed and you were able to focus your attention and efforts to get it done.",
                "Tell us about a time when you were particularly effective on prioritizing tasks and completing a project on schedule.",
                "Tell us about the last time that you undertook a project that demanded a lot of initiative.",
                "Tell us how you keep your job knowledge current with the ongoing changes in the industry.",
                "There are times when we work without close supervision or support to get the job done. Tell us about a time when you found yourself in such a situation and how things turned out.",
                "What impact did you have in your last job?",
                "What is the most competitive work situation you have experienced? How did you handle it? What was the result?",
                "What is the riskiest decision you have made? What was the situation? What happened?",
                "What kinds of challenges did you face on your last job? Give an example of how you handled them.",
                "What projects have you started on your own recently? What prompted you to get started?",
                "What sorts of things have you done to become better qualified for your career?",
                "What was the best idea that you came up with in your career? How did you apply it?",
                "When you disagree with your manager, what do you do? Give an example.",
                "When you have a lot of work to do, how do you get it all done? Give an example."
            ],
            "Analytical Thinking": [
                "Describe the project or situation which best demonstrates your analytical abilities. What was your role?",
                "\nDeveloping and using a detailed procedure is often very important in a job. Tell about a time when you needed to develop and use a detailed procedure to successfully complete a project.",
                "Give a specific example of a time when you used good judgment and logic in solving a problem.",
                "Give me a specific example of a time when you used good judgment and logic in solving a problem.",
                "Give me an example of when you took a risk to achieve a goal. What was the outcome?",
                "How did you go about making the changes (step by step)? Answer in depth or detail such as 'What were you thinking at that point?' or 'Tell me more about meeting with that person,' or 'Lead me through your decision process'.",
                "Relate a specific instance when you found it necessary to be precise in your work in order to complete the job.",
                "Tell us about a job or setting where great precision to detail was required to complete a task. How did you handle that situation?",
                "Tell us about a time when you had to analyze information and make a recommendation. What kind of thought process did you go through? What was your reasoning behind your decision?",
                "Tell us about your experience in past jobs that required you to be especially alert to details while doing the task involved."
            ],
            "Building Relationships": [
                "Give a specific example of a time when you had to address an angry customer. What was the problem and what was the outcome? How would you assess your role in diffusing the situation?",
                "It is very important to build good relationships at work but sometimes it doesn’t always work. If you can, tell about a time when you were not able to build a successful relationship with a difficult person.",
                "Tell us about a time when you built rapport quickly with someone under difficult conditions.",
                "What, in your opinion, are the key ingredients in guiding and maintaining successful business relationships? Give examples of how you made these work for you."
            ],
            "Business Systems Thinking": [
                "Describe how your position contributes to your organization’s/unit’s goals. What is the unit’s goals/mission?",
                "Tell us about a politically complex work situation in which you worked."
            ],
            "Caution": [
                "Have you ever worked in a situation where the rules and guidelines were not clear? Tell me about it. How did you feel about it? How did you react?",
                "Some people consider themselves to be “big picture people” and others are “detail-oriented”. Which are you? Give an example of a time when you displayed this.",
                "Tell us about a situation when it was important for you to pay attention to details. How did you handle it?",
                "Tell us about a time when you demonstrated too much initiative?"
            ],
            "Communication": [
                "Describe a situation in which you were able to effectively “read” another person and guide your actions by your understanding of their individual needs or values.",
                "Describe a situation when you were able to strengthen a relationship by communicating effectively. What made your communication effective?",
                "Describe a situation where you felt you had not communicated well. How did you correct the situation?",
                "Describe a time when you were able to effectively communicate a difficult or unpleasant idea to a superior.",
                "Describe the most significant written document, report, or presentation which you had to complete.",
                "Give me an example of a time when you were able to successfully communicate with another person, even when that individual may not have personally liked you, or vice versa.",
                "Give me an example of a time when you were able to successfully communicate with another person, even when that individual may not have personally liked you.",
                "Have you ever had to “sell” an idea to your co-workers or group? How did you do it? Did they “buy” it?",
                "Have you had to “sell” an idea to your co-workers, classmates, or group? How did you do it? Did they “buy” it?",
                "How do you keep subordinates informed about information that affects their jobs?",
                "How do you keep your manager informed about what is being done in your work area?",
                "How do you go about explaining a complex technical problem to a person who does not understand technical jargon? What approach do you take in communicating with people?",
                "What kinds of communication situations cause you difficulty? Give an example.",
                "Tell us about a recent successful experience in making a speech or presentation. How did you prepare? What obstacles did you face? How did you handle them?",
                "Tell us about a time when you and your current/previous supervisor disagreed but you still found a way to get your point across.",
                "Tell us about a time when you had to present complex information. How did you ensure that the other person understood?",
                "Tell us about a time when you had to use your verbal communication skills in order to get a point across that was important to you.",
                "Tell us about a time when you were particularly effective in a talk you gave or a seminar you taught.",
                "Tell us about an experience in which you had to speak up in order to be sure that other people knew what you thought or felt.",
                "Tell us me about a situation when you had to speak up (be assertive) in order to get a point across that was important to you.",
                "Tell us me about a time in which you had to use your written communication skills in order to get an important point across.",
                "What challenges have occurred while you were coordinating work with other units, departments, and/or divisions?",
                "What have you done to improve your verbal communication skills?",
                "How have you persuaded people through a document you prepared?",
                "What are the most challenging documents you have done? What kinds of proposals have you written?",
                "What kinds of writing have you done? How do you prepare written communications?"
            ],
            "conflict resolution": [
                "Describe a time when you took personal accountability for a conflict and initiated contact with the individual(s) involved to explain your actions."
            ]
            }

    def recommend_resources(self, study_topic, ):
        if study_topic in self.resource_db.resources:
            print(f"\nRecommended Resources for {study_topic}:")
            for i, resource in enumerate(self.resource_db.resources[study_topic], 1):
                print(f"{i}. {resource}")
        else:
            print("No recommendations available for this topic.")
    def recommend_questions(self, question_topic):
        print(self.topics[question_topic][random.randint(0,len(self.topics[question_topic])-1)])



# Sample resources and questions data
resource_db = RecommendedResourcesDatabase()
resource_db.add_resource("Book recommendation", [
    "Book by Gayle Laackmann: Cracking the Coding Interview",
    "Book by Alex Xu: System Design Interview Part 1 and 2",
    # Add more resources as needed
])

questions_db = ToDoList()

def main():
    todo_list = ToDoList()
    todo_list.resource_db.add_resource("Book recommendation", [
        "Book by Gayle Laackmann: Cracking the Coding Interview",
        "Book by Alex Xu: System Design Interview Part 1 and 2",
        "Book by Eric Giguere, John Mongan, and Noah Kindler: Programming Interviews Exposed",
        "Book by Steven S. Skiena: The Algorithm Design Manual",
        "Book by Adnan Aziz: Elements of Programming Interviews",
        "Book by Jon Bentley: Programming Pearls",
        "Book by Noel Markham: Java Programming Interview Exposed",
        "Book by Meenakshi & Kamal Rawat: Dynamix Programming for Coding Interviews",
        "Book by Adnan Aziz: Algorithms for Interview",
        "Book by Joe Celkos: SQL Puzzles & Answers",
    ])

    while True:
        print("\nMenu:")
        print("1. Information about Interviews")
        print("2. Book Recommendations")
        print("3. Interview Questions")
        print("4. Hackathon Events")
        # print("5. Job Recommendations")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"The truth\n")
            print("""Students preparing for coding interviews should be aware of several truths to help them navigate the process more effectively. Remember that coding interviews are just one part of the job application process. While they are important, they are not the only factor that determines your worth as a developer. Stay persistent, keep learning, and approach interviews as opportunities to showcase your skills and experience.
                """)
        elif choice == "2":
            study_topic = "Book recommendation"  # Fixed topic for book recommendations
            todo_list.recommend_resources(study_topic)
        elif choice == "3":
            print("Ambition")
            print("Adaptability")
            print("Analytical thinking")
            print("Building relationships")
            print("Building business systems")
            print("Caution")
            print("Communication")
            print("Conflict resolution")
            study_topic = input("Enter your question topic: ")
            todo_list.recommend_questions(study_topic)
        elif choice == "4":
            print("Hackathon Events:\n", 
                "13-15 October: Data Hackfest (Virtual)\n",
                "16-23 October: Global Hack Week: Open Source Week (Virtual)\n"
                "20 October: Brizy No-code Hackathon (Virtual)\n",
                "21 October: EasyA x Stacks Bitcoin Hackathon (London)\n",
                "21 October: All In for Students Hackathon (Virtual)\n"
                "25 October: Cloudflare AI hack night (London)\n",
                "27-29 October: Web3Apps (Virtual)")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

