import os
from typing import Optional, Union

from kittycad.api.ai import create_text_to_cad
from kittycad.client import ClientFromEnv
from kittycad.models import Error, TextToCad
from kittycad.models.file_export_format import FileExportFormat
from kittycad.models.text_to_cad_create_body import TextToCadCreateBody

def example_create_text_to_cad():
    # Read the API key from environment variable
    # Set KITTYCAD_API_TOKEN in your environment or .env
    token = os.environ.get('KITTYCAD_API_TOKEN', '')
    if not token:
        print("Please set the KITTYCAD_API_TOKEN environment variable.")
        return

    # Create our client.
    client = ClientFromEnv()

    # Call the API to create the 3D model
    result: Optional[Union[TextToCad, Error]] = create_text_to_cad.sync(
        client=client,
        output_format=FileExportFormat.STL,
        body=TextToCadCreateBody(
            prompt="create a 3d of electrical kettle with red color",
        ),
    )

    # Check for errors in the response
    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    # Assuming the result is valid, proceed with saving the output
    body: TextToCad = result
    print("Model created successfully!")
    print(f"Model ID: {body.id}")
    print(f"Status: {body.status}")

    # Save the STL file
    try:
        # Assuming the body contains a URL or binary data for the STL file
        if hasattr(body, 'output_data') and body.output_data is not None:
            with open('electrical_kettle.stl', 'wb') as f:
                f.write(body.output_data)  # Write binary data to file
            print("STL file saved as 'electrical_kettle.stl'")
        else:
            print("No output data available to save.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

# Call the function to test
example_create_text_to_cad()