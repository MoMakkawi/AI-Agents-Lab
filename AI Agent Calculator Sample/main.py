# Load HF modules
from huggingface_hub import login
from smolagents import CodeAgent, tool, InferenceClientModel

# Load Custom modules
from tools import *
from Helper import *

#Check Configurations 
try_configure()

# Alfred, the smart calculator, preparing the results for the calculation
agent = CodeAgent(tools=[Add, Multiply], model=InferenceClientModel())

# Run the smart calculator agent to solve this problem
result = agent.run("Add the numbers -1, 2, 3, 4, 5. Then multiply the result by 2.")

# Print the final result
print("🧮 Final result:", result)
