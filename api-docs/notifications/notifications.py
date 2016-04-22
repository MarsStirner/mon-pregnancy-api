"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine NotificationsListSuccess
@apiSuccess (Success 2xx) {json} 200 ������ ��������.
@apiSuccessExample {json} �������� �����
{
    "meta": {
        "code": "200",
        "name": "��"
    },
    "data": [
    {
    "sender":"bars-mr",
    "receiver": "176", 
    "send_date": "12-12-2001",
    "receive_date": "12-12-2016"
    "notification_text": "��������� �������� ����� �������� (����� 2001/234) �� ��������� ������� ��������� ������������� ���������� ������������."
    }
        ]   
}
"""


"""
@api {Result} /risar/api/integration/<int:api_version>/notifications/list/?date_begin=<date_begin>&date_end=<date_end> �������� ������
@apiName Notifications
@apiGroup Notifications
@apiVersion 0.1.0
@apiDescription �������� ������

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<int:api_version>/notifications/list/?date_begin=<date_begin>&date_end=<date_end> ��������� ������ ���������� ���������� �����
@apiName GetNotifications
@apiGroup Notifications
@apiVersion 0.1.0
@apiDescription ����� ������������ ��� ��������� ������ ���������� �� ���������� ����� �� �������� ���������� �������<br/>
��������� JSON Schema <a href="/json-data/notifications/data/notifications-schema.json">notifications-schema.json</a><br/>
JSON ������ <a href="/json-data/notifications/data/notifications-example.json">notifications-example.json</a>

@apiParam {Number} api_version ������ API, ����� ������������� �����
@apiParam {Date} date_begin ���� ������ � ������� yyyy-mm-dd.
@apiParam {Date} date_end ���� ���������� � ������� yyyy-mm-dd.

@apiUse NotificationsSuccess
"""