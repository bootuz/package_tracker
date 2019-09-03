
def parse(history):
    data = {}
    try:
        data["sender"] = history[0].UserParameters.Sndr
    except AttributeError:
        data["sender"] = "No information"
    try:
        data["recipient"] = history[0].UserParameters.Rcpn
    except AttributeError:
        data["recipient"] = "No information"
    try:
        data["to"] = history[0].AddressParameters.MailDirect.NameRU
    except AttributeError:
        data["to"] = "No information"
    try:
        data["item"] = history[0].ItemParameters.ComplexItemName
    except AttributeError:
        data["item"] = "No information"
    try:
        data["from"] = history[0].AddressParameters.CountryFrom.NameRU
    except AttributeError:
        data["from"] = "No information"

    res = []
    for i in range(len(history)):
        try:
            res.append(f'{history[i].OperationParameters.OperDate.date().isoformat()} '
                       f'{history[i].AddressParameters.OperationAddress.Description} '
                       f'{history[i].OperationParameters.OperAttr.Name}')
        except AttributeError:
            res.append(f'{history[i].OperationParameters.OperDate.date().isoformat()} '
                       f'{history[i].AddressParameters.OperationAddress.Description} '
                       f'{history[i].OperationParameters.OperType.Name}')

    data["points"] = '\n'.join(res)
    return data


def format_dict(data):
    a = f'Отправитель: {data["sender"]}\n' \
        f'Получатель: {data["recipient"]}\n' \
        f'Откуда: {data["from"]}\n' \
        f'Куда: {data["to"]}\n' \
        f'Посылка: {data["item"]}\n' \
        f'\n' \
        f'{data["points"]}'
    return a
