A Markov Model (made from scratch) that uses context (historical data) and a prompt (input) to generate text (output). This project testifies how a simple question (can we statistically determine the future using history and the 'last step'?) can come a long way by leveraging technology (and a good processor). 

The model is simple yet highly effective. It can be used to determine algorithmic bias towards certain words (or phrases) or statistically determine a sequence of words using context and a prompt. I have used Python to make the model from scratch since it is convenient, more readable, NumPy, easy file management. Each of the variables can be changed (token size, prompt length, output length, etc.)

I have used Harry Potter and the Sorcerer's Stone as context for the model and used two (out of as many) prompts to generate a sequence of phrases. Since the context for this model is volatile, it can be changed numerously by simply changing an argument for a function. Also, the same context can be used for multiple prompts. 

Feel free to fork and customize!
