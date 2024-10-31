import xml.etree.ElementTree as ET

def update_price_in_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    rtpl_id = input("Введите значение для RTPL_RTPL_ID: ")
    pack_id = input("Введите значение для PACK_PACK_ID: ")
    srls_id = input("Введите значение для SRLS_SRLS_ID: ")
    lcal_id = input("Введите значение для LCAL_LCAL_ID: ")
    new_price = input("Введите новое значение для PRICE_$: ")

    found = False
    for row in root.findall("row"):
        # Получение значений тегов для отладки
        rtpl_value = row.find("./column[@name='RTPL_RTPL_ID']").text if row.find("./column[@name='RTPL_RTPL_ID']") is not None else None
        pack_value = row.find("./column[@name='PACK_PACK_ID']").text if row.find("./column[@name='PACK_PACK_ID']") is not None else None
        srls_value = row.find("./column[@name='SRLS_SRLS_ID']").text if row.find("./column[@name='SRLS_SRLS_ID']") is not None else None
        lcal_value = row.find("./column[@name='LCAL_LCAL_ID']").text if row.find("./column[@name='LCAL_LCAL_ID']") is not None else None

        # Вывод текущих значений для отладки
        print(f"Проверка строки: RTPL_RTPL_ID={rtpl_value}, PACK_PACK_ID={pack_value}, SRLS_SRLS_ID={srls_value}, LCAL_LCAL_ID={lcal_value}")

        # Проверка значений
        if (rtpl_value == rtpl_id and pack_value == pack_id and srls_value == srls_id and lcal_value == lcal_id):
            price_column = row.find("./column[@name='PRICE_$']")
            if price_column is not None:
                price_column.text = new_price
                found = True
                break

    # Сохранение изменений
    if found:
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"Значение PRICE_$ успешно обновлено на {new_price}")
    else:
        print("Элемент с указанными параметрами не найден.")

# Укажите путь к XML-файлу
file_path = "xml_conf.xml"
update_price_in_xml(file_path)
