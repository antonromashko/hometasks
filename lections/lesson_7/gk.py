import datetime
import decimal


def fix_data_type(self, value, dot_notation_field):
    this_type = self.dest_field_types[dot_notation_field]

    if value == '':
        return None
    if this_type == 'double':
        return decimal.Decimal(value if value != '' else 0)
    elif this_type == 'date' or this_type == 'datetime':
        try:
            return datetime.datetime.strptime(value, cfg.global_date_format).date()
        except:
            try:
                return datetime.datetime.strptime(value, "%d/%m/%y").date()
            except:
                try:
                    return datetime.datetime.strptime(value, "%Y-%m-%d").date()
                except:
                    try:
                        return datetime.datetime.strptime(value, "%d-%m-%y").date()
                    except:
                        try:
                            return datetime.datetime.strptime(value, "%d-%m-%Y").date()
                        except:
                            raise Exception('I have tried everything but that date don\'t like me: ' + value)

    return value
