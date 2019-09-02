import os

from suds import Client


class WrongIdError(Exception):
    pass


class PackageData:
    url = 'http://tracking.russianpost.ru/rtm34?wsdl'
    headers = {'Content-Type': 'application/soap+xml; charset=utf-8'}

    def __init__(self, barcode, login=os.environ['LOGIN'], password=os.environ['PASSWORD']):
        self.client = Client(self.url, headers=self.headers)
        self.login = login
        self.password = password
        self.barcode = barcode

    def _get_history(self):
        msg = f'<?xml version="1.0" encoding="UTF-8"?>\
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" ' \
              f'xmlns:oper="http://russianpost.org/operationhistory" ' \
              f'xmlns:data="http://russianpost.org/operationhistory/data" ' \
              f'xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">\
           <soap:Header/>\
           <soap:Body>\
              <oper:getOperationHistory>\
                 <data:OperationHistoryRequest>\
                    <data:Barcode>{self.barcode}</data:Barcode>\
                    <data:MessageType>0</data:MessageType>\
                    <data:Language>RUS</data:Language>\
                 </data:OperationHistoryRequest>\
                 <data:AuthorizationHeader soapenv:mustUnderstand="1">\
                    <data:login>{self.login}</data:login>\
                    <data:password>{self.password}</data:password>\
                 </data:AuthorizationHeader>\
              </oper:getOperationHistory>\
           </soap:Body>\
        </soap:Envelope>'
        result = self.client.service.getOperationHistory(__inject={'msg': msg})
        if result:
            return result.historyRecord
        else:
            raise WrongIdError

    @property
    def history_record(self):
        return self._get_history()

    def __len__(self):
        return len(self.history_record)
