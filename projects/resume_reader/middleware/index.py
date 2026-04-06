from fastapi import Request, HTTPException
import fitz  # PyMuPDF
import tempfile

ALLOWED_TYPES = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
]

async def resume_validation_middleware(request: Request, call_next):
    if request.method == "POST":
        form = await request.form()
        file = form.get("file")

        if not file:
            raise HTTPException(status_code=400, detail="No file uploaded")

        # ✅ Check file type
        if file.content_type not in ALLOWED_TYPES:
            raise HTTPException(
                status_code=400,
                detail="Only PDF and DOCX files are allowed"
            )

        # ✅ Check if PDF is machine-readable
        if file.content_type == "application/pdf":
            contents = await file.read()

            with tempfile.NamedTemporaryFile(delete=True) as tmp:
                tmp.write(contents)
                tmp.flush()

                doc = fitz.open(tmp.name)
                text = ""

                for page in doc:
                    text += page.get_text()

                if not text.strip():
                    raise HTTPException(
                        status_code=400,
                        detail="Scanned PDF detected. Please upload a digital resume."
                    )

    response = await call_next(request)
    return response