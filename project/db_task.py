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


def user_belongs_to_group(username: str):
    conn = psycopg2.connect(host='127.0.0.1',
                            user='postgres',
                            password='postgres'
                            )

    try:
        cursor = conn.cursor()
        query = "SELECT auth_user.username " \
                "FROM auth_user_groups RIGHT Join  auth_user on auth_user_groups.user_id = auth_user.id " \
                "WHERE auth_user_groups.group_id = (SELECT id from auth_group where name = 'akhtsei')"
        cursor.execute(query)
        u_name = cursor.fetchone()
        for names in u_name:
            u_name == names
        assert names == username, f"Oops... User name {names} does not match to {username}!"

    finally:
        conn.close()


def user_presents_at_users_table(username: str):
    conn = psycopg2.connect(host='127.0.0.1',
                            user='postgres',
                            password='postgres'
                            )

    try:
        cursor = conn.cursor()
        query = "SELECT username FROM auth_user WHERE username = 'akhtsei2'"
        cursor.execute(query)
        u_name = cursor.fetchone()
        for names in u_name:
            u_name == names
        assert names == username, f"Oops... User name {names} does not match to {username}!"

    finally:
        conn.close()