from google import genai
import json

#tools
def deliver_book(location:str,isbn:str):
    """
    Creates a book delivery request, delivering a book when a request comes up.
    """
    return {
        "status":"Delivered",
        "message": f"Book {isbn}, has been delieverd to {location}."
    }

#tool definitions
#function declaration
book_delivery = {
    "type": "function",
    "name": "deliver_book",
    "description": "Delivers book when a book delivery request comes up.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
            "isbn":{
                "type":"string",
                "description": "The books unique number, the ISBN number e.g. 978-3-16-148410-0"
            }
        },
        "required": ["location","isbn"],
    },
}

client = genai.Client()

user_request = input("Please make a request for delivery: ")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=user_request,
    tools=[book_delivery],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")

#call model with function declarations
fc_step = next(s for s in interaction.steps if s.type == "function_call")
print(fc_step)


#execute the function
result = None
if fc_step.name == "deliver_book":
    result = deliver_book(**fc_step.arguments)
    print(f"Function execution result: {result}")

#sending results back to model

final_interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "function_result",
            "name": fc_step.name,
            "call_id": fc_step.id,
            "result": [{"type": "text", "text": json.dumps(result)}],
        }
    ],
    tools=[book_delivery],
    previous_interaction_id=interaction.id,
)

print(final_interaction.output_text)

