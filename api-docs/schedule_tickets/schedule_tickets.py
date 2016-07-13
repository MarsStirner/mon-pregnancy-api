"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine ScheduleTicketsSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
    "data": [
        {
            "schedule_ticket_id": "schedule_ticket_code_012345",
            "hospital": "hospital_code_012345",
            "doctor": "doctor_code_012345",
            "date": "2011-11-11",
            "time": "15:00"
        },
        {
            "schedule_ticket_id": "schedule_ticket_code_012346",
            "hospital": "hospital_code_012345",
            "doctor": "doctor_code_012345",
            "date": "2011-11-11",
            "time": "16:00"
        }
    ]
}
"""


"""
@api {Result} /risar/api/integration/<int:api_version>/card/<card_id>/schedule_tickets/ Описание ошибок
@apiName ScheduleTickets
@apiGroup ScheduleTickets
@apiVersion 0.1.0
@apiDescription Описание ошибок

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<int:api_version>/card/<card_id>/schedule_tickets/ Получение списка записей пациента на прием
@apiName GetScheduleTickets
@apiGroup ScheduleTickets
@apiVersion 0.1.0
@apiDescription Получение списка записей пацииента на прием<br/>
Валидация JSON Schema <a href="/json-data/schedule_tickets/data/schedule_tickets-schema.json">schedule_tickets-schema.json</a><br/>
JSON пример <a href="/json-data/schedule_tickets/data/schedule_tickets-success-example.json">schedule_tickets-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {Int} card_id Код карты пациента.

@apiUse ScheduleTicketsSuccess
"""