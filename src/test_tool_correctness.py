from deepeval import evaluate
from deepeval.test_case import LLMTestCase, ToolCall
from deepeval.metrics import ToolCorrectnessMetric

test_case = LLMTestCase(
    input="Export to a PDF file",
    actual_output="To re-export the content to a PDF file, I will create a PDF file containing the same random paragraph. Please wait a moment.",

    # Replace this with the tools that was actually used by your LLM agent
    tools_called=[ToolCall(name="mcp_tool")],

    expected_tools=[ToolCall(name="mcp_tool")],
)

metric = ToolCorrectnessMetric()

evaluate(test_cases=[test_case], metrics=[metric])
