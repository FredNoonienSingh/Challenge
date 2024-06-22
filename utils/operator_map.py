
operator_map = {
    'eq': lambda field, value: field == value,
    'gt': lambda field, value: field > value,
    'lt': lambda field, value: field < value,
    'gte': lambda field, value: field >= value,
    'lte': lambda field, value: field <= value,
    'like': lambda field, value: field.like(f'%{value}%'),  # For partial string matches
    'in': lambda field, value: field.in_(value),  # For filtering based on a list of values
}
