import sqlite3
from helpers import azure, config as config
from logger.logger import event_logger


def build_local_key_store():
    event_logger.info("Building local key store.")
    con = sqlite3.connect(".store/store.db")
    cur = con.cursor()
    event_logger.info("Creating key table.")
    cur.execute("create table if not exists store (key, value)")
    cur.execute("insert into store(key, value) values (system, system)")

    if config.use_local_store == "False":

        secrets_dict = retrieve_vault_secrets()
        if secrets_dict:
            event_logger.info("Inserting keys into local key store.")
            for name, value in secrets_dict.items():
                cur.execute(f"insert into store(key, value) values ({name}, {value})")
                cur.close()
                con.close()

def retrieve_vault_secrets():
    event_logger.info("Retrieving secrets from Az Vault.")
    secret_client = azure.build_secret_client()

    if secret_client:
        secret_list = secret_client.list_properties_of_secrets()
        secrets_dict = {}
        for secret in secret_list:
            if secret.name:
                secrets_dict[secret.name] = secret_client.get_secret(secret.name)

                return secrets_dict
    else:

        return None

def retieve_secret_local(local_secret_name: str):
    event_logger.info("Retrieving secret from local store.")
    con = sqlite3.connect(".store/store.db")
    cur = con.cursor()
    cur.execute("select value from store where name = ?", (local_secret_name,))
    result = cur.fetchone()
    cur.close()
    con.close()

    if result:
        return result[0]
    else:
        return ""
