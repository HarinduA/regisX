from graphics import *

pass_count = 0
trailer_count = 0
module_retriever_count = 0
exclude_count = 0
all_data = []

# Input section
user_type = input("Are you a student (S) or staff (T)? ").lower()

if user_type == 's':  # For a single student
    while True:
        try:
            pass_credits = int(input("Enter your total PASS credits: "))

            # Check if the input is an integer
            if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range")
                continue

            defer_credits = int(input("Enter your total DEFER credits: "))
            fail_credits = int(input("Enter your total FAIL credits: "))

            # Check if credits are in the valid range
            if defer_credits not in [0, 20, 40, 60, 80, 100, 120] or fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range")
                continue

            total_credits = pass_credits + defer_credits + fail_credits

            # Evaluate outcome
            if total_credits != 120:
                print("Total incorrect")
                continue

            if pass_credits == 120:
                outcome = "Progress"
                pass_count += 1
            elif pass_credits == 100 and fail_credits <= 20:
                outcome = "Progress (module trailer)"
                trailer_count += 1
            elif pass_credits == 0 and defer_credits == 60 and fail_credits == 60:
                outcome = "Module retriever"
                module_retriever_count += 1
            elif pass_credits in [80, 60, 20] and (defer_credits + fail_credits) in [40, 60, 80]:
                outcome = "Module retriever"
                module_retriever_count += 1
            elif pass_credits == 40 and defer_credits == 80 and fail_credits == 0:
                outcome = "Module retriever"
                module_retriever_count += 1
            elif pass_credits == 40:
                outcome = "Exclude"
                exclude_count += 1
            elif pass_credits == 20 and defer_credits == 0 and fail_credits == 100:
                outcome = "Exclude"
                exclude_count += 1
            else:
                outcome = "Do not progress - module retriever"

            print("Your predicted outcome is:", outcome)

            all_data.append((pass_credits, defer_credits, fail_credits, outcome))
            break  # Break out of the loop if all conditions are met

        except ValueError:
            print("Integer required for credits.")
            # Loop continues until valid integer inputs are provided

elif user_type == 't':
    try:
        while True:
            pass_credits = input("Enter total PASS credits: ")

            # Checking if inputs are integers
            if not pass_credits.isdigit():
                print("Integer required for credits.")
                continue

            pass_credits = int(pass_credits)

            # Check if pass_credits is in the valid range
            if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range")
                continue

            defer_credits = input("Enter total DEFER credits: ")
            fail_credits = input("Enter total FAIL credits: ")

            # Checking if inputs are integers
            if not (defer_credits.isdigit() and fail_credits.isdigit()):
                print("Integer required for credits.")
                continue

            defer_credits, fail_credits = int(defer_credits), int(fail_credits)

            total_credits = pass_credits + defer_credits + fail_credits
            if total_credits != 120:
                print("Total credits incorrect for this student.")
                continue

            outcome = ""  # Initialize outcome variable

            if pass_credits == 120:
                outcome = "Progress"
                pass_count += 1
            elif pass_credits == 100 and fail_credits <= 20:
                outcome = "Progress (module trailer)"
                trailer_count += 1
            elif pass_credits == 0 and defer_credits == 60 and fail_credits == 60:
                outcome = "Module retriever"
                module_retriever_count += 1
            elif pass_credits in [80, 60, 20] and (defer_credits + fail_credits) in [40, 60, 80]:
                outcome = "Module retriever"
                module_retriever_count += 1
            elif pass_credits == 40 and defer_credits == 80 and fail_credits == 0:
                outcome = "Module retriever"
                module_retriever_count += 1
            elif pass_credits == 40:
                outcome = "Exclude"
                exclude_count += 1
            elif pass_credits == 20 and defer_credits == 0 and fail_credits == 100:
                outcome = "Exclude"
                exclude_count += 1
            else:
                outcome = "Do not progress - module retriever"

            #  evaluation conditions...
            all_data.append((pass_credits, defer_credits, fail_credits, outcome))

            print("\nOutcome Data:")
            for data in all_data:
                print(f"Outcome: {data[3]}")

            with open('progression_data.txt', 'w') as file:
                for data in all_data:
                    file.write(f"Pass: {data[0]}, Defer: {data[1]}, Fail: {data[2]}, Outcome: {data[3]}\n")

            decision = input("Enter 'continue' to input for another student or 'quit' to show histogram: ")
            if decision.lower() == 'quit':
                break

        # Histogram calculation
        win = GraphWin("Results", 800, 600)
        win.setBackground("Mint Cream")
        display1 = Text(Point(150, 50), "Histogram Results")
        display1.setStyle("bold")
        display1.setSize(20)
        display1.draw(win)

        aLine = Line(Point(100, 500), Point(600, 500))
        aLine.draw(win)

        # Function to create bars in the histogram
        def create_bar(start_x, end_x, height, color, label):
            bar = Rectangle(Point(start_x, 500), Point(end_x, 500 - (height * 20)))
            bar.setFill(color)
            bar.draw(win)
            display = Text(Point((start_x + end_x) // 2, 515), label)
            display.draw(win)

       

        # Inside the histogram section
        create_bar(100, 150, pass_count, color_rgb(70, 130, 180), "Progress")
        create_bar(200, 250, trailer_count, color_rgb(100,149,237), "Trailer")
        create_bar(300, 350, module_retriever_count, color_rgb(0, 191, 255), "Retriever")
        create_bar(400, 450, exclude_count, color_rgb(30, 144, 255), "Excluded")

        pass_count_text = Text(Point(125, 450 - (pass_count * 10) - 15), pass_count)
        pass_count_text.draw(win)

        trailer_count_text = Text(Point(225, 450 - (trailer_count * 10) - 15), trailer_count)
        trailer_count_text.draw(win)

        retriever_count_text = Text(Point(325, 450 - (module_retriever_count * 10) - 15), module_retriever_count)
        retriever_count_text.draw(win)

        exclude_count_text = Text(Point(425, 450 - (exclude_count * 10) - 15), exclude_count)
        exclude_count_text.draw(win)

        # Calculate and display total count
        total_count = pass_count + trailer_count + module_retriever_count + exclude_count
        total_count_text = Text(Point(300, 550), str(total_count) + " Outcomes in total")
        total_count_text.draw(win)

        win.getMouse()
        win.close()
        
    except ValueError:
        print("Integer required for credits.")

else:
    print("Invalid user type. Please enter 'S' for student or 'T' for staff.")
