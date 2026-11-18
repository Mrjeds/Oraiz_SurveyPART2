import hashlib

from sqlmodel import Session

from database import create_db_and_tables, engine
from models import Users , book


def main():
    create_db_and_tables()
    # what you want to do here

    # demo account: login with name=demo password=demo123 (stored hashed)
    demo_user = Users(name='demo', password=hashlib.sha256(b'demo123').hexdigest())

    book1 = book(Name='The Great Gatsby', Price=299.5, Note='Classic novel')
    book2 = book(Name='To Kill a Mockingbird', Price=350, Note='Required reading')
    book3 = book(Name='1984', Price=275, Note='Dystopian classic')

    with Session(engine) as session:
        session.add(demo_user)
        session.add(book1)
        session.add(book2)
        session.add(book3)
        session.commit()


if __name__ == "__main__":
    main()
