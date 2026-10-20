
from itertools import count

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="SHMC API",
    description="Smart Hostel Maintenance & Complaint Management",
    version="1.0.0",
)

complaints = {}
complaint_ids = count(1)

VALID_CATEGORIES = {"plumbing", "electrical", "wifi", "furniture"}
VALID_STATUSES = {"open", "assigned", "in_progress", "resolved"}


class ComplaintCreate(BaseModel):
    student_id: str = Field(min_length=1)
    room_number: str = Field(min_length=1)
    category: str
    description: str = Field(min_length=5)


class StatusUpdate(BaseModel):
    status: str


@app.get("/health")
def health():
    return {"status": "healthy", "service": "SHMC"}


@app.post("/complaints", status_code=201)
def create_complaint(data: ComplaintCreate):
    category = data.category.strip().lower()

    if category not in VALID_CATEGORIES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid category. Choose from {sorted(VALID_CATEGORIES)}",
        )

    complaint_id = next(complaint_ids)

    complaint = {
        "id": complaint_id,
        "student_id": data.student_id,
        "room_number": data.room_number,
        "category": category,
        "description": data.description,
        "status": "open",
        "technician_id": None,
    }

    complaints[complaint_id] = complaint
    return complaint


@app.get("/complaints")
def list_complaints():
    return list(complaints.values())


@app.get("/complaints/{complaint_id}")
def get_complaint(complaint_id: int):
    complaint = complaints.get(complaint_id)

    if complaint is None:
        raise HTTPException(status_code=404, detail="Complaint not found")

    return complaint


@app.patch("/complaints/{complaint_id}/status")
def update_status(complaint_id: int, data: StatusUpdate):
    complaint = complaints.get(complaint_id)

    if complaint is None:
        raise HTTPException(status_code=404, detail="Complaint not found")

    if data.status not in VALID_STATUSES:
        raise HTTPException(status_code=400, detail="Invalid status")

    complaint["status"] = data.status
    return complaint
