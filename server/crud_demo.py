#!/usr/bin/env python3

from app import app
from models import db, Pet
from sqlalchemy import func

def main():
    with app.app_context():
        # Clear existing data
        Pet.query.delete()
        db.session.commit()
        
        print("=== Flask-SQLAlchemy CRUD Demo ===\n")
        
        # CREATE operations
        print("1. Creating pets...")
        pet1 = Pet(name="Fido", species="Dog")
        print(f"Created pet1: {pet1}")
        print(f"pet1.id before commit: {pet1.id}")
        
        db.session.add(pet1)
        db.session.commit()
        print(f"pet1.id after commit: {pet1.id}")
        
        pet2 = Pet(name="Whiskers", species="Cat")
        db.session.add(pet2)
        db.session.commit()
        print(f"Created pet2: {pet2}\n")
        
        # READ operations
        print("2. Querying pets...")
        print(f"All pets: {Pet.query.all()}")
        print(f"First pet: {Pet.query.first()}")
        print(f"Cats only: {Pet.query.filter(Pet.species == 'Cat').all()}")
        print(f"Names starting with 'F': {Pet.query.filter(Pet.name.startswith('F')).all()}")
        print(f"Filter by species: {Pet.query.filter_by(species='Cat').all()}")
        print(f"Get by ID: {db.session.get(Pet, 1)}")
        print(f"Ordered by species: {Pet.query.order_by('species').all()}")
        
        count = db.session.query(func.count(Pet.id)).first()
        print(f"Total pets: {count[0]}\n")
        
        # UPDATE operations
        print("3. Updating pet...")
        pet1.name = "Fido the mighty"
        db.session.commit()
        print(f"Updated pet1: {pet1}\n")
        
        # DELETE operations
        print("4. Deleting pet...")
        db.session.delete(pet1)
        db.session.commit()
        print(f"Remaining pets after deletion: {Pet.query.all()}")
        
        # Delete all pets
        remaining_count = Pet.query.delete()
        db.session.commit()
        print(f"Deleted {remaining_count} remaining pets")
        print(f"Final pet count: {Pet.query.all()}")
        
        print("\n=== CRUD operations completed successfully! ===")

if __name__ == "__main__":
    main()