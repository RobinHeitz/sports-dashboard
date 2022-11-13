import webserver as ws
import uvicorn

from data_management import data_controller, model

import threading
import time



def data_func():
    ...

    while True:
        time.sleep(5)

        with data_controller.session_context() as session:
            ...

            session.add(model.Competition())
            session.commit()







if __name__ == "__main__":
    ...

    # threading.Thread(target=data_func, args=(), daemon=True).start()

    uvicorn.run("webserver.main:app",host="0.0.0.0", port=80, log_level="info", reload=True)


