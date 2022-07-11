class NotAvailableEquipment(Exception):
    def __init__(self, equipment):
        self.equipment = equipment

    def __str__(self):
        return f'{self.equipment} -> equipment is not available in warehouse'


class EquipmentWarehouse:
    eq_in_warehouse = {'Printer': [], 'Scanner': [], 'Copier': []}
    eq_in_office = {'Printer': [], 'Scanner': [], 'Copier': []}
    __warehouse_brand_model = []
    __office_brand_model = []

    @classmethod
    def __get_eq_index(cls, eq_type, brand_model, place):
        check_list = []
        if place == 'warehouse':
            check_list = cls.eq_in_warehouse
        elif place == 'office':
            check_list = cls.eq_in_office
        index = None
        for i in range(len(check_list[eq_type])):
            w_brand_model = f"{check_list[eq_type][i]['brand']} {check_list[eq_type][i]['model']}"
            if w_brand_model == brand_model:
                index = i
                break
        return index

    @classmethod
    def add_equipment_warehouse(cls, equipment):
        brand_model = f'{equipment.brand} {equipment.model}'
        if brand_model not in cls.__warehouse_brand_model:  # check the same equipment is already exist or not
            cls.__warehouse_brand_model.append(brand_model)  # add equipment to internal dict
            eq = {}
            for att in equipment.__dict__.keys():
                if att != 'eq_type':
                    eq[att] = getattr(equipment, att)
            eq['count'] = 1
            cls.eq_in_warehouse[equipment.eq_type].append(eq)

        else:  # increase count if same equipment exists
            index = cls.__get_eq_index(equipment.eq_type, brand_model, 'warehouse')
            cls.eq_in_warehouse[equipment.eq_type][index]['count'] += 1

    @classmethod
    def add_equipment_office(cls, equipment):
        brand_model = f'{equipment.brand} {equipment.model}'
        try:
            if brand_model not in cls.__warehouse_brand_model:  # check equipment is available in warehouse
                raise NotAvailableEquipment(brand_model)
            else:
                if brand_model not in cls.__office_brand_model:  # check the same equipment exist or not in office
                    cls.__office_brand_model.append(brand_model)  # add equipment to internal dict
                    eq = {}
                    for att in equipment.__dict__.keys():
                        if att != 'eq_type':
                            eq[att] = getattr(equipment, att)
                    eq['count'] = 1
                    cls.eq_in_office[equipment.eq_type].append(eq)
                else:  # increase count if same equipment exists
                    index = cls.__get_eq_index(equipment.eq_type, brand_model, 'office')
                    cls.eq_in_office[equipment.eq_type][index]['count'] += 1

                cls.__remove_eq_from_warehouse(equipment)  # remove or decrease count in warehouse

        except NotAvailableEquipment as e:
            print(e)

    @classmethod
    def __remove_eq_from_warehouse(cls, equipment):
        brand_model = f'{equipment.brand} {equipment.model}'
        index = cls.__get_eq_index(equipment.eq_type, brand_model, 'office')
        if cls.eq_in_warehouse[equipment.eq_type][index]['count'] == 1:
            cls.__warehouse_brand_model.remove(brand_model)
            cls.eq_in_warehouse[equipment.eq_type].pop(index)
        else:
            cls.eq_in_warehouse[equipment.eq_type][index]['count'] -= 1

    @classmethod
    def get_eq_in_warehouse(cls):
        return cls.eq_in_warehouse

    @classmethod
    def get_eq_in_office(cls):
        return cls.eq_in_office


class Equipment:
    def __init__(self, eq_type, brand, model):
        self.eq_type = eq_type
        self.brand = brand
        self.model = model


class Printer(Equipment):
    def __init__(self, brand, model, print_speed, color_print, eq_type='Printer'):
        super().__init__(eq_type, brand, model)
        self.print_speed = print_speed
        self.color_print = color_print


class Scanner(Equipment):
    def __init__(self, brand, model, resolution, color_scan, eq_type='Scanner'):
        super().__init__(eq_type, brand, model)
        self.resolution = resolution
        self.color_scan = color_scan


class Copier(Equipment):
    def __init__(self, brand, model, two_side_print, eq_type='Copier'):
        super().__init__(eq_type, brand, model)
        self.two_side_print = two_side_print


printer_1 = Printer('HP', 'One', '20 pages/sec', True)
printer_2 = Printer('HP', 'One', '20 pages/sec', True)
printer_3 = Printer('Canon', 'XXX', '17 pages/sec', False)
scaner_1 = Scanner('Plustek', 'OpticPro A320', '1600x1600', True)
copier_1 = Copier('Copier1', 'ABC', False)

print('Warehouse:')
print(EquipmentWarehouse.get_eq_in_warehouse())
print('Office:')
print(EquipmentWarehouse.get_eq_in_office())
print('-' * 30)

EquipmentWarehouse.add_equipment_warehouse(printer_1)
EquipmentWarehouse.add_equipment_warehouse(printer_2)
EquipmentWarehouse.add_equipment_warehouse(printer_3)
EquipmentWarehouse.add_equipment_warehouse(scaner_1)
EquipmentWarehouse.add_equipment_warehouse(copier_1)

print('Warehouse:')
print(EquipmentWarehouse.get_eq_in_warehouse())
print('Office:')
print(EquipmentWarehouse.get_eq_in_office())
print('-' * 30)

EquipmentWarehouse.add_equipment_office(printer_1)
EquipmentWarehouse.add_equipment_office(copier_1)
EquipmentWarehouse.add_equipment_office(printer_3)

print('Warehouse:')
print(EquipmentWarehouse.get_eq_in_warehouse())
print('Office:')
print(EquipmentWarehouse.get_eq_in_office())
print('-' * 30)

# check Warehouse validation
EquipmentWarehouse.add_equipment_office(copier_1)
print('Warehouse:')
print(EquipmentWarehouse.get_eq_in_warehouse())
print('Office:')
print(EquipmentWarehouse.get_eq_in_office())
