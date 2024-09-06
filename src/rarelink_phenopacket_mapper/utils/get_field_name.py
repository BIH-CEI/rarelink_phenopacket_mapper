from rarelink_phenopacket_mapper.data_standards import DataField


def get_field_name(field):
    return field.__name__


if __name__ == "__main__":
    print(get_field_name(DataField.data_type))
