from fastapi import Request, HTTPException

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

async def file_size_validator(request: Request, call_next):
    if request.method == "POST":
        content_length = request.headers.get("content-length")

        if content_length and int(content_length) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=413,
                detail="File too large. Max allowed size is 5MB."
            )

    response = await call_next(request)
    return response