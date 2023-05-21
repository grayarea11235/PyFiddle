# Simple user service
import logging
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    family_namename = Column(String)
    given = Column(String)
#    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)

def main():
    print('In main...')

    
if __name__ == '__main__':
    main()
