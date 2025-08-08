import gradio as gr

def greet(name):
    return "Hello " + name + "!"

# Create a new Gradio interface
demo = gr.Interface(
    fn=greet,           # The function to wrap
    inputs="text",      # The input component
    outputs="text",     # The output component
    title="Greeting App",
    description="Enter your name and get a personalized greeting!"
)

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)
