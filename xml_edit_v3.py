import xml.etree.ElementTree as ET

def update_price_in_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Условия для обновления
    target_rtpl_id = input("Введите значение для RTPL_RTPL_ID: ")
    target_pack_id = '0'
    target_srls_id = '4'
    target_lcal_ids = {'37', '38', '39', '40', '41', '42', '43', '44', '31021', '31024', '31027', '31028', '31029', '31034', '31037', '31039', '31044', '31047'}
    new_price = '125'

    found = False
    for row in root.findall("row"):
        # Получение значений тегов
        rtpl_value = row.find("./column[@name='RTPL_RTPL_ID']").text if row.find("./column[@name='RTPL_RTPL_ID']") is not None else None
        pack_value = row.find("./column[@name='PACK_PACK_ID']").text if row.find("./column[@name='PACK_PACK_ID']") is not None else None
        srls_value = row.find("./column[@name='SRLS_SRLS_ID']").text if row.find("./column[@name='SRLS_SRLS_ID']") is not None else None
        lcal_value = row.find("./column[@name='LCAL_LCAL_ID']").text if row.find("./column[@name='LCAL_LCAL_ID']") is not None else None

        # Проверка условий
        if (rtpl_value == target_rtpl_id and pack_value == target_pack_id and
                srls_value == target_srls_id and lcal_value in target_lcal_ids):
            price_column = row.find("./column[@name='PRICE_$']")
            if price_column is not None:
                # Если PRICE_$ задан, но отличается от 125, то обновить его
                if price_column.text != new_price:
                    price_column.text = new_price
                    found = True
            else:
                # Если PRICE_$ отсутствует, добавить его
                new_price_column = ET.Element("column", name="PRICE_$")
                new_price_column.text = new_price
                row.append(new_price_column)
                found = True

    # Сохранение изменений
    if found:
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"Значения PRICE_$ успешно обновлены на {new_price} для заданных условий.")
    else:
        print("Элементы с указанными параметрами не найдены.")

# Укажите путь к XML-файлу
file_path = "TRAFIC_HISTORIES_VOICE_INTOUT.xml"
update_price_in_xml(file_path)
