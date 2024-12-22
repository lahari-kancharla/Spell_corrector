#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from textblob import TextBlob

def main():
    print("Welcome to the Spell Corrector!")
    print("Type 'exit' to quit the program.\n")

    while True:
        # Take input from the user
        user_input = input("Enter a text to check and correct spelling: ")
        
        # Exit condition
        if user_input.lower() == "exit":
            print("Thank you for using the Spell Corrector. Goodbye!")
            break
        
        # Display the original text
        print("Original text: " + user_input)

        # Create a TextBlob object and correct the text
        corrected_text = TextBlob(user_input).correct()

        # Display the corrected text
        print("Corrected text: " + str(corrected_text))
        print("-" * 50)

if __name__ == "__main__":
    main()


# In[ ]:




