def generate_id() -> str:
    """Generate a unique identifier."""
    import uuid
    return str(uuid.uuid4())