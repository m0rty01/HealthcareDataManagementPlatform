from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.db.mongodb import get_database
from app.blockchain.connection import blockchain

router = APIRouter()

@router.post("/")
async def create_health_record(record_data: dict, db = Depends(get_database)):
    """
    Create a new health record.
    """
    # Store data on blockchain
    tx_hash = await blockchain.store_data(record_data)
    
    # Store reference in MongoDB
    record = {
        "data_hash": tx_hash,
        "patient_id": record_data["patient_id"],
        "created_at": record_data.get("created_at"),
        "record_type": record_data.get("record_type"),
    }
    
    result = await db.health_records.insert_one(record)
    return {"id": str(result.inserted_id), "tx_hash": tx_hash}

@router.get("/{patient_id}")
async def get_patient_records(patient_id: str, db = Depends(get_database)):
    """
    Get all health records for a patient.
    """
    records = await db.health_records.find({"patient_id": patient_id}).to_list(1000)
    return records

@router.get("/{record_id}/verify")
async def verify_record(record_id: str, db = Depends(get_database)):
    """
    Verify a health record's integrity using blockchain.
    """
    record = await db.health_records.find_one({"_id": record_id})
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    # Verify data on blockchain
    is_valid = await blockchain.verify_data(record["data_hash"], record)
    return {"is_valid": is_valid}