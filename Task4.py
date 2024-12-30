questions = []

while True:
    print("\n1. Add a question")
    print("2. Show the latest 5 questions")
    choice = input("Enter your choice: ")

    if choice == '1':
        question = input("Enter your question: ")
        questions.append(question)
        print("Question added!")

    elif choice == '2':  
        print("Latest 5 Questions:")
        for q in questions[-5:]:  
            print(q)


    else:
        print("Invalid choice. Please try again.")