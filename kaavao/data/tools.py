from PyQt5.QtWidgets import QMessageBox

from ..database.db_tools import get_active_db_and_schema


def parse_value(value):
    str_value = str(value)
    val = str_value
    if str_value.upper() == "NULL":
        val = None
    elif str_value.lower() == "true":
        val = True
    elif str_value.lower() == "false":
        val = False
    return val


def query_results_to_str_list(result: list) -> [list]:
    """Parses sql query results to list of strings. One row per item.

    :param result: list of tuples containing results for sql query.
    :return:
    """
    output = []
    for row in result:
        row_list = []
        for item in row:
            if isinstance(item, str):
                row_list.append(item)
            elif item is None:
                item = "Null"
                row_list.append(item)
            else:
                row_list.append(str(item))
        output.append(row_list)
    return output


def parse_filter_ids(results: dict):
    for key, value in results.items():
        i = 0
        for item in results[key]:
            item = str(item)
            if item == "None":
                value.pop(i)
            else:
                results[key][i] = item
                i += 1


def save_alert_msg():
    db, project = get_active_db_and_schema()
    msg = QMessageBox()
    msg.setText("Haluatko tallentaa työtilan " + project + "?")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
    return msg.exec_()


def parse_layer_source(source: str) -> dict:
    params = {}

    key_index_start = source.find("key='") + len("key='")
    key_index_end = source.find("'", key_index_start)
    params["key"] = source[key_index_start:key_index_end]

    schema_index_start = source.find('table="') + len('table="')
    schema_index_end = source.find('"', schema_index_start)
    params["schema"] = source[schema_index_start:schema_index_end]

    table_index_start = schema_index_end + 3
    table_index_end = source.find('"', table_index_start)
    params["table"] = source[table_index_start:table_index_end]

    params["geom"] = "geom" if source[-6:] == "(geom)" else None
    return params
