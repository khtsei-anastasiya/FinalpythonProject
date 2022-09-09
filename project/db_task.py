import psycopg2


def group_adding():
    conn = psycopg2.connect(host='127.0.0.1',
                            user='postgres',
                            password='postgres'
                            )

    try:
        cursor = conn.cursor()
        query = "INSERT INTO auth_group (id, name) VALUES (default, 'akhtsei')"
        cursor.execute(query)
        conn.commit()
    finally:
        conn.close()


def user_belongs_to_group():
    conn = psycopg2.connect(host='127.0.0.1',
                            user='postgres',
                            password='postgres'
                            )

    try:
        cursor = conn.cursor()
        query = "SELECT * FROM auth_group WHERE name='akhtsei'"
        cursor.execute(query)
        u_name = cursor.fetchall()
        assert u_name == 'akhtsei', 'Oops... User name doesn\'t match!'

    finally:
        conn.close()



