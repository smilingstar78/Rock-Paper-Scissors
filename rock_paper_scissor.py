import random

print("WELCOME TO MY ROCK, PAPER, SCISSORS GAME!")

choice = {1: "rock", 2: "paper", 3: "scissors"}

user_score = 0
ai_score = 0

while True:
    game = input("Do you want to play this game? (yes/no): ").lower()
    
    if game == "no":
        print("Thanks for playing! 🌸")
        
        if user_score > ai_score:
            print(f"🏆 Your Score: {user_score}")
            print(f"📊 AI Score: {ai_score}")
        elif user_score == ai_score:
            print(f"🏆 Your Score: {user_score}")
            print(f"🏆 AI Score: {ai_score}")  
        else:
            print(f"📊 Your Score: {user_score}")
            print(f"🏆 AI Score: {ai_score}")
            
        quit()
    
    elif game == "yes":
        while True:
            try:
                user_choice = int(input("Select 1 for rock, 2 for paper, and 3 for scissors: "))
                
                if user_choice not in choice:
                    print("🛑 Enter a number between 1 and 3.")
                else:
                    break  
            except ValueError:
                print("🛑 Invalid input, please enter a number between 1 and 3.")
        
        ai_choice = random.randint(1, 3)
        
        print(f"\nYou selected: {choice[user_choice]}")
        print(f"AI selected: {choice[ai_choice]}\n")
        
        if user_choice == ai_choice:
            print("It's a Tie! 🤝")
        elif (user_choice == 1 and ai_choice == 3) or (user_choice == 2 and ai_choice == 1) or (user_choice == 3 and ai_choice == 2):
            print("🎉 You won!")
            user_score += 1  
        else:
            print("❌ AI won!")
            ai_score += 1  
    
    else:
        print("🛑 Please enter 'yes' or 'no'.")
