from deepeval import evaluate
from deepeval.metrics import MCPUseMetric
from deepeval.test_case import LLMTestCase
from deepeval.test_case.mcp import MCPServer
from mcp.types import Tool

output = """
  To re-export the content to a PDF file, I will create a PDF file containing the same random paragraph. Please wait a moment.



<tool name = "mcp_tool" label = "Task completed" status = "done" >

<toolinput>

{
"name": "mcp_tool",
"server_name": "file_creation",
"query": "Create a PDF file containing a random paragraph",
"payload": {
"file_content": "This is a randomly generated paragraph. It serves as an example of how text can be structured in a coherent and meaningful way. The paragraph is designed to demonstrate the ability to create and save content in a PDF file format for various purposes."
}
}

</toolinput>


<toolresponse>



file_creation:


<thinkingdot>

<thinkingtitle>Planning...</thinkingtitle>

<thinkingcontent>

<plan>1. Sub-questions
- What exact content should go into the PDF?
- What filename should be used for the PDF?
- Where should the PDF be saved locally?
- Which Azure Storage container and blob name should be used for uploading?
- How will we generate and return the SAS URL?

2. Entity Extraction
- Content: “This is a randomly generated paragraph. It serves as an example of how text can be structured in a coherent and meaningful way. The paragraph is designed to demonstrate the ability to create and save content in a PDF file format for various purposes.”
- File type: PDF
- Local directory: /tmp/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009
- Azure container: mcp-file-created
- Blob name prefix: 519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/
- Desired output: SAS URL

3. Relevant Tools and Approaches
========== START of Relevant Tools ==========
- Tool: pandoc_convert-contents – Convert the provided paragraph into a PDF file, saving it to a specified path.
- Tool: filesystem_write_file – (optional) Write intermediate content to a file if needed before conversion.
- Tool: ekoai-mcp_upload_from_file – Upload the generated PDF to Azure Blob Storage under the required container and blob name.
- Tool: ekoai-mcp_generate_sas_url – Generate a secure download link (SAS URL) for the uploaded PDF.
========== END of Relevant Tools ==========

4. Constraints
```
- The PDF must be saved under /tmp/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009.
- The file must be uploaded to Azure container "mcp-file-created".
- The blob name must follow: 519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/<filename>.pdf
- The final response must include the generated SAS URL.
- No files outside the specified local directory may be written or uploaded.
```

5. Solution Approach
- Step 1: Choose a filename, e.g., “random_paragraph.pdf”.
- Step 2: Use pandoc_convert-contents to convert the provided paragraph string into PDF, saving to `/tmp/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf`.
- Step 3: Upload the PDF to Azure Blob Storage container “mcp-file-created” with blob name:
`519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf` via ekoai-mcp_upload_from_file.
- Step 4: Generate a SAS URL for that blob using ekoai-mcp_generate_sas_url.
- Step 5: Return the generated SAS URL in the final response.
</plan>

</thinkingcontent>

</thinkingdot>

<thinkingdot>

<thinkingtitle>Step 1:</thinkingtitle>

<thinkingcontent>


<toolcode>

{
"name": "pandoc_convert-contents",
"input": {
"content": "This is a randomly generated paragraph. It serves as an example of how text can be structured in a coherent and meaningful way. The paragraph is designed to demonstrate the ability to create and save content in a PDF file format for various purposes.",
"output_format": "pdf",
"output_path": "/tmp/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf"
}
}

</toolcode>
Processing tool call: pandoc_convert-contents
Asking LLM to generate arguments for tool: pandoc_convert-contents
LLM generated arguments: {
"contents": "This is a randomly generated paragraph. It serves as an example of how text can be structured in a coherent and meaningful way. The paragraph is designed to demonstrate the ability to create and save content in a PDF file format for various purposes.",
"output_format": "pdf",
"output_file": "/tmp/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf"
}
Tool call output: {"content": [{"type": "text", "text": "Error converting contents from markdown to pdf: No pandoc was found: either install pandoc and add it\nto your PATH or or call pypandoc.download_pandoc(...) or\ninstall pypandoc wheels with included pandoc."}], "isError": true}

</thinkingcontent>

</thinkingdot>

<thinkingdot>

<thinkingtitle>Step 2:</thinkingtitle>

<thinkingcontent>

<python>
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import textwrap

# Define output PDF path
output_dir = "/tmp/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "random_paragraph.pdf")

# Paragraph content
paragraph = (
"This is a randomly generated paragraph. It serves as an example of how text "
"can be structured in a coherent and meaningful way. The paragraph is designed "
"to demonstrate the ability to create and save content in a PDF file format "
"for various purposes."
)

# Create PDF
c = canvas.Canvas(output_path, pagesize=letter)
width, height = letter
text_object = c.beginText(40, height - 40)
wrapped_lines = textwrap.wrap(paragraph, width=80)
for line in wrapped_lines:
text_object.textLine(line)
c.drawText(text_object)
c.showPage()
c.save()

print("PDF created at:", output_path)
</python>
Executing code: from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import textwrap

# Define output PDF path
output_dir = "/tmp/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "random_paragraph.pdf")

# Paragraph content
paragraph = (
"This is a randomly generated paragraph. It serves as an example of how text "
"can be structured in a coherent and meaningful way. The paragraph is designed "
"to demonstrate the ability to create and save content in a PDF file format "
"for various purposes."
)

# Create PDF
c = canvas.Canvas(output_path, pagesize=letter)
width, height = letter
text_object = c.beginText(40, height - 40)
wrapped_lines = textwrap.wrap(paragraph, width=80)
for line in wrapped_lines:
text_object.textLine(line)
c.drawText(text_object)
c.showPage()
c.save()

print("PDF created at:", output_path)
Code Output: PDF created at: /tmp/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf


</thinkingcontent>

</thinkingdot>

<thinkingdot>

<thinkingtitle>Step 3:</thinkingtitle>

<thinkingcontent>


<toolcode>

{
"name": "ekoai-mcp_upload_from_file",
"input": {
"container_name": "mcp-file-created",
"blob_name": "519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf",
"file_path": "/tmp/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf"
}
}

</toolcode>
Processing tool call: ekoai-mcp_upload_from_file
Asking LLM to generate arguments for tool: ekoai-mcp_upload_from_file
LLM generated arguments:
```json
{
"containerName": "mcp-file-created",
"blobName": "519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf",
"localFilePath": "/tmp/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf",
"contentType": "application/pdf",
"contentDisposition": "attachment; filename=\"random_paragraph.pdf\""
}
```
Tool call output: {"content": [{"type": "text", "text": "{\"success\":true}"}], "structuredContent": {"success": true}, "isError": false}

</thinkingcontent>

</thinkingdot>

<thinkingdot>

<thinkingtitle>Step 4:</thinkingtitle>

<thinkingcontent>


<toolcode>

{
"name": "ekoai-mcp_generate_sas_url",
"input": {
"container_name": "mcp-file-created",
"blob_name": "519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf"
}
}

</toolcode>
Processing tool call: ekoai-mcp_generate_sas_url
Asking LLM to generate arguments for tool: ekoai-mcp_generate_sas_url
LLM generated arguments: {"containerName":"mcp-file-created","blobName":"519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf"}
Tool call output: {"content": [{"type": "text", "text": "https://ekoaistaging.blob.core.windows.net/mcp-file-created/519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf?sv=2025-07-05&se=2025-11-21T10%3A32%3A05Z&sr=b&sp=r&sig=wcbQhKsbbgQjlk%2Fa1TquR8kxb24tgkjbzHKvd6tYgnQ%3D"}]}

</thinkingcontent>

</thinkingdot>

<thinkingdot>

<thinkingtitle>Step 5:</thinkingtitle>

<thinkingcontent>

<finalanswer>

Here is your PDF file containing the random paragraph:

https://ekoaistaging.blob.core.windows.net/mcp-file-created/519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf?sv=2025-07-05&se=2025-11-21T10%3A32%3A05Z&sr=b&sp=r&sig=wcbQhKsbbgQjlk%2Fa1TquR8kxb24tgkjbzHKvd6tYgnQ%3D
</finalanswer>

</thinkingcontent>

</thinkingdot><finalanswer>

Here is your PDF file containing the random paragraph:

https://ekoaistaging.blob.core.windows.net/mcp-file-created/519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf?sv=2025-07-05&se=2025-11-21T10%3A32%3A05Z&sr=b&sp=r&sig=wcbQhKsbbgQjlk%2Fa1TquR8kxb24tgkjbzHKvd6tYgnQ%3D</finalanswer>



</toolresponse>


</tool>

Here is your PDF file containing the random paragraph:

https://ekoaistaging.blob.core.windows.net/mcp-file-created/519909e80d7735ab7c000002/eko_691575cc70b98d8df1ff5bb1_691eed9999e95854429c5009/random_paragraph.pdf?sv=2025-07-05&se=2025-11-21T10%3A32%3A05Z&sr=b&sp=r&sig=wcbQhKsbbgQjlk%2Fa1TquR8kxb24tgkjbzHKvd6tYgnQ%3D

    """

test_case = LLMTestCase(
    input="re-export to pdf file", # Your input here
    actual_output=output, # Your LLM app's final output here
    mcp_servers=[MCPServer(
        server_name="ekoai-mcp",
        available_tools=[
            Tool(name="generate_sas_url", description="Generate SAS URL", inputSchema={"type": "object", "properties": {}}),
            Tool(name="upload_from_file", description="Upload file", inputSchema={"type": "object", "properties": {}})
        ]
    )] # Your MCP server's data
    # MCP primitives used (if any)
)

metric = MCPUseMetric()

evaluate([test_case], [metric])
