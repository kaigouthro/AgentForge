from agents.testagent import TestAgent
from agentforge.utils.function_utils import Functions

var = TestAgent()
string = "testing 123"
functions = Functions()

result = var.run(context=string)
functions.print_result(result, "Test Results")