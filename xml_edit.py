import xml.etree.ElementTree as ET
def update_price_in_xml(file_path):
    # Загружаем XML-файл
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Запрашиваем у пользователя параметры для поиска и новое значение для PRICE_$
    rtpl_id = input("Введите значение для RTPL_RTPL_ID: ")
    pack_id = input("Введите значение для PACK_PACK_ID: ")
    srls_id = input("Введите значение для SRLS_SRLS_ID: ")
    lcal_id = input("Введите значение для LCAL_LCAL_ID: ")
    new_price = input("Введите новое значение для PRICE_$: ")

    # Поиск нужного <row>
    found = False
    for row in root.findall("row"):
        # Проверка значений в row
        if (row.find("./column[@name='RTPL_RTPL_ID']").text == rtpl_id and
                row.find("./column[@name='PACK_PACK_ID']").text == pack_id and
                row.find("./column[@name='SRLS_SRLS_ID']").text == srls_id and
                row.find("./column[@name='LCAL_LCAL_ID']").text == lcal_id):

            # Находим и обновляем PRICE_$ внутри найденного <row>
            price_column = row.find("./column[@name='PRICE_$']")
            if price_column is not None:
                price_column.text = new_price
                found = True
                break

    # Сохраняем изменения, если элемент найден и изменён
    if found:
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"Значение PRICE_$ успешно обновлено на {new_price}")
    else:
        print("Элемент с указанными параметрами не найден.")


# Укажите путь к вашему XML-файлу
file_path = "xml_conf.xml"
update_price_in_xml(file_path)
