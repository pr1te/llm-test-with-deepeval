from deepeval import assert_test
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval

# here is the custom test matric

def test_correctness():
  correctness_metric = GEval(
    name="Correctness",
    criteria="Focus on the download links provided in the response. The download link must be in https://google.com/eko_<string>_<string>/<file_name>.pdf pattern.",
    evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
    threshold=0.5
  )

  test_case = LLMTestCase(
    input="Export to a PDf file",
    actual_output="In case you want to download the PDF, you can do so here: https://google.com/eko_123_1233_4567/document.pdf",
    expected_output="You can download here https://google.com/eko_<string>_<string>/<file_name>.pdf"
  )

  assert_test(test_case, [correctness_metric])
