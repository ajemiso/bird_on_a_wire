import bird_on_a_wire


def start_session():
    obj = bird_on_a_wire.Session()
    obj.update_quote()
    return True


if __name__ == '__main__':
    start_session()