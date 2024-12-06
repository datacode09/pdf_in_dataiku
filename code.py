# -*- coding: utf-8 -*-
import dataiku
from reportlab.pdfgen import canvas
import io
import datetime

# Step 1: Generate a PDF in memory
def create_pdf(content="Hello, this is a dynamically generated PDF!"):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer)
    c.drawString(100, 750, content)
    c.drawString(100, 730, f"Generated at runtime in Dataiku at {datetime.datetime.now()}.")
    c.save()
    buffer.seek(0)  # Reset buffer position for reading
    return buffer

# Step 2: Access the managed folder
folder = dataiku.Folder("8IbFLs31")  # Replace with your managed folder ID

# Step 3: Upload (or overwrite) the PDF to the folder
pdf_name = "runtime_generated.pdf"  # Name of the PDF file to store
pdf_buffer = create_pdf(content="This PDF will overwrite existing ones if the same name is used.")

# Overwrite the existing PDF by simply uploading with the same name
folder.upload_stream(pdf_name, pdf_buffer)

# Step 4: List all files in the managed folder to verify
files_in_folder = folder.list_paths_in_partition()
print("Files in folder:", files_in_folder)

# Optional: Retrieve and display information about the managed folder
folder_info = folder.get_info()
print("Folder Info:", folder_info)
