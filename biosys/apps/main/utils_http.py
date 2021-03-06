from __future__ import absolute_import, unicode_literals, print_function, division

from django.http import HttpResponse


class CSVFileResponse(HttpResponse):
    def __init__(self, file_name=None):
        content_type = 'text/csv'
        content_disposition = 'attachment;'

        if file_name is not None:
            if not file_name.lower().endswith('.csv'):
                file_name += '.csv'
            content_disposition += ' filename=' + file_name

        super(CSVFileResponse, self).__init__(content_type=content_type)
        self['Content-Disposition'] = content_disposition


class ExcelFileResponse(HttpResponse):
    def __init__(self, file_name=None):
        content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        content_disposition = 'attachment;'

        if file_name is not None:
            if not file_name.lower().endswith('.xlsx'):
                file_name += '.xlsx'
            content_disposition += ' filename=' + file_name

        super(ExcelFileResponse, self).__init__(content_type=content_type)
        self['Content-Disposition'] = content_disposition


class WorkbookResponse(ExcelFileResponse):
    def __init__(self, wb, file_name=None):
        super(WorkbookResponse, self).__init__(file_name=file_name)
        wb.save(self)


