from common.schemas import Competition
from data_management import model as mdl, data_controller as dc

if __name__ == "__main__":

    with dc.session_context() as session:
        ...

        query = session.query(mdl.Competition).all()
        print(query)

        session.add(mdl.Competition())
        session.commit()

    