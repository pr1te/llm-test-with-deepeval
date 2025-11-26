from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric

test_case = LLMTestCase(
    input="What is AmitySolutions?",
    actual_output="AmitySolutions is a public social media app.",
    retrieval_context=["We are Thailand's industry-leading Platform as a Service (PaaS) specializing in tailored, enterprise-grade AI applications and AI agents."]
)

metric = FaithfulnessMetric(threshold=0.8, include_reason=True)

evaluate(test_cases=[test_case], metrics=[metric])
