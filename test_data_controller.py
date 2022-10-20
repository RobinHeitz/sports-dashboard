from webserver.data_management.data_controller import get_something, session_context

if __name__ == "__main__":

    with session_context() as session:

        val = get_something(session, 5)
        print(val)