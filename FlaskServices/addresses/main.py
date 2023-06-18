# Simple user service
import logging
from sqlalchemy import Column, Integer, String, Boolean, DateTime


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    name_or_number = Column(String)

    address1 = Column(String)
    address2 = Column(String)
    address3 = Column(String)
    address4 = Column(String)

    post_code = Column(String)

    enabled = Column(Boolean)
    deleted = Column(Boolean)

    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __repr__(self):
        return "<Address (name_or_number='%s', address1='%s', address2='%s')>" % 
            (self.name_or_number, self.address1, self.address2)


def main():
    print('In main...')

    
if __name__ == '__main__':
    main()
