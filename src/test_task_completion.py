from deepeval.tracing import observe
from deepeval.dataset import Golden, EvaluationDataset
from deepeval.metrics import TaskCompletionMetric

@observe()
def file_export_agent (input):
  return "Can you confirm the file extension you would like to export to?";

# Create dataset
dataset = EvaluationDataset(goldens=[Golden(input="Export to a PDF file")])

# Initialize metric
task_completion = TaskCompletionMetric(threshold=0.7, model="o4-mini")

# Loop through dataset
for golden in dataset.evals_iterator(metrics=[task_completion]):
  file_export_agent(golden.input)
