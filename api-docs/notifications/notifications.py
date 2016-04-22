"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine NotificationsSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
    "data": [
    {
    "sender":"bars-mr",
    "receiver": "176", 
    "send_date": "12-12-2001",
    "receive_date": "12-12-2016"
    "notification_text": "У пациентки Ивановой Анны Ивановны карта (2015/453). изменилась степень риска на высокую.\n----\nПожалуйста, не отвечайте на это письмо, оно было сгенирировано автоматически "
    }
        ]   
}
"""


"""
@api {Result} /risar/api/integration/<int:api_version>/notifications/list/?date_begin=<date_begin>&date_end=<date_end> Описание ошибок
@apiName Notifications
@apiGroup Notifications
@apiVersion 0.1.0
@apiDescription Описание ошибок

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<int:api_version>/notifications/list/?date_begin=<date_begin>&date_end=<date_end> Получение списка оповещений по внутренней почте
@apiName GetNotifications
@apiGroup Notifications
@apiVersion 0.1.0
@apiDescription Получение списка оповещений по внутренней почте за заданный промежуток времени<br/>
Валидация JSON Schema <a href="/json-data/notifications/data/notifications-schema.json">notifications-schema.json</a><br/>
JSON пример <a href="/json-data/notifications/data/notifications-example.json">notifications-example.json</a>

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {Date} date_begin Дата начала в формате yyyy-mm-dd.
@apiParam {Date} date_end Дата завершения yyyy-mm-dd.

@apiUse NotificationsSuccess
"""