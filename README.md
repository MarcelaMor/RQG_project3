# Random Quote Generator

In a world filled with constant distractions and challenges, finding a moment of clarity and inspiration can be difficult.

Enter the Stoic Quote Generator , your personal guide to daily motivation rooted in the timeless wisdom of Stoic philosophy.

This Quote Generator is designed to help you cultivate inner strength and self-control, essential pillars for leading a resilient and balanced life.

## FEATURES

- Quote Categories: The script categorizes quotes into different themes. Currently, it supports two categories: 'Inner Strength' and 'Self Control'.

- Random Quote Selection: Within each category, the script randomly selects a quote to display to the user. This is done using the random.choice() function.

- User Interaction: The script interacts with the user through the console. It prompts the user to choose a category and then displays a quote from the chosen category.

- Continuous Operation: The script operates in a continuous loop, allowing the user to keep choosing categories and receiving quotes until they decide to stop the script.

- It ends by saying "Bye!" when entering "No".

## USAGE

To run the script, simply follow the link:

https://random-quote-generator-11873979e468.herokuapp.com/

## TESTING

Python code was manually tested and linted:

- Passed the code through a PEP8 at https://pep8ci.herokuapp.com/ and corrected each outputed errors.

- Testing the app I noticed that it terminated after an invalid input not giving me a second chance. Same was noticed after a succesful run. Loops where added to achieve desired behavior.

- Test runs where done in the IDE terminal and verified that the app behaved the same in the deployed heroku version.  

#### BUGS

Loops werent behaving as expected.
The outerloop (firt loop) wasn't triggered when invalid input was typed in, instead it proceeded to end of the inner loop (second loop).
My intention was for it to go back to the start and ask for a valid input.

To achieve this a "continue" statement was added to the outer loop and the desired behavior was achieved.

#### UNSOLVED BUGS

None.
No errors where returned from https://pep8ci.herokuapp.com/ either.

#### DEPLOYMENT

![deploy](https://github.com/MarcelaMor/RQG_project3/assets/159925451/d782087a-6072-431b-bc00-a2721e1dde3d)
- Navigate to the "settings" tab in the repository
- Click the "pages" link on the left side bar
- Choose the main branch and deploy

## NOTES

The quotes used in this program are attributed to famous philosophers such as Epictetus, Seneca, and Marcus Aurelius.

## LICENSE

This project is open-source and available under the MIT License. Feel free to modify and distribute as needed.

## ACKNOWLEDGEMENTS

Inspired by projects and tutorials from Hackr.io and Javatpoint.
I have also used help from: https://www.w3schools.com/python/python_while_loops.asp
