"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine ScheduleTicketsListSuccess
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
            "patient": "patient_code_012345",
            "date": "2011-11-11",
            "time": "15:00"
        },
        {
            "schedule_ticket_id": "schedule_ticket_code_012346",
            "hospital": "hospital_code_012345",
            "doctor": "doctor_code_012345",
            "patient": "patient_code_012345",
            "date": "2011-11-11",
            "time": "16:00"
        }
    ]
}
"""


"""
@api {Result} /risar/api/integration/<int:api_version>/schedule_tickets/ Описание ошибок
@apiName ScheduleTickets
@apiGroup ScheduleTickets
@apiVersion 0.1.0
@apiDescription Описание ошибок

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<int:api_version>/schedule_tickets/<hospital_code>/<doctor_code>/?date_begin=<date_begin>&date_end=<date_end> Получение списка записей на прием
@apiName GetScheduleTickets
@apiGroup ScheduleTickets
@apiVersion 0.1.0
@apiDescription Получение списка записей пациента на прием<br/>
Валидация JSON Schema <a href="/json-data/schedule_tickets/data/schedule_tickets-list-schema.json">schedule_tickets-list-schema.json</a><br/>
JSON пример <a href="/json-data/schedule_tickets/data/schedule_tickets-list-schema.json">schedule_tickets-list-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} hospital_code Код ЛПУ
@apiParam {Int} doctor_code Код специалиста
@apiParam {Date} date_begin Дата начала в формате yyyy-mm-dd.
@apiParam {Date} date_end Дата завершения в формате yyyy-mm-dd.

@apiUse ScheduleTicketsListSuccess
"""



"""
@api {post} /risar/api/integration/<int:api_version>/schedule_tickets/ Регистрация записи на прием
@apiName PostScheduleTickets
@apiGroup ScheduleTickets
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации записи на прием<br/>
Валидация JSON Schema <a href="/json-data/schedule_tickets/data/schedule_tickets-schema.json">schedule_tickets-schema.json</a><br/>
JSON пример <a href="/json-data/schedule_tickets/data/schedule_tickets-success-example.json">schedule_tickets-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительное число


@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
    "data":{
        "schedule_ticket_id": "schedule_ticket_code_012345",
        "hospital": "hospital_code_012345",
        "doctor": "doctor_code_012345",
        "patient": "patient_code_012345",
        "date": "2011-11-11",
        "time": "15:00"
    }
}



@apiUse CreateError
"""



"""
@api {put} /risar/api/integration/<int:api_version>/schedule_tickets/<schedule_ticket_id> Изменение записи на прием
@apiName PutScheduleTickets
@apiGroup ScheduleTickets
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения записи на прием<br/>
Валидация JSON Schema <a href="/json-data/schedule_tickets/data/schedule_tickets-schema.json">schedule_tickets-schema.json</a><br/>
JSON пример <a href="/json-data/schedule_tickets/data/schedule_tickets-success-example.json">schedule_tickets-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {Int} schedule_ticket_id Идентификатор записи на прием

@apiUse CreateSuccess

@apiUse CreateError
"""



"""
@api {delete} /risar/api/integration/<int:api_version>/schedule_tickets/<schedule_ticket_id> Удаление записи на прием
@apiName DelScheduleTickets
@apiGroup ScheduleTickets
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления записи на прием<br/>

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {Int} schedule_ticket_id Идентификатор записи на прием
"""