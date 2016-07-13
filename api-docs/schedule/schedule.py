"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine ScheduleSuccess
@apiSuccess (Success 2xx) {json} 200 Данные.
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
    "data": [
        {
            "date": "2011-11-11",
            "intervals": [
                {
                    "begin_time": "11:00",
                    "end_time": "13:00"
                },
                {
                    "begin_time": "14:00",
                    "end_time": "18:00"
                }
            ]
        },
        {
            "date": "2012-12-12",
            "intervals": [
                {
                    "begin_time": "10:00",
                    "end_time": "17:00"
                }
            ]
        }
    ]
}

"""

"""
@api {Result} /risar/api/integration/<int:api_version>/schedule/<doctor_id> Описание ошибок
@apiName Schedule
@apiGroup Schedule
@apiVersion 0.1.0
@apiDescription Описание ошибок

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<int:api_version>/schedule/<doctor_id>/?date_begin=<date_begin>&date_end=<date_end> Получение расписания специалиста
@apiName GetScheduleList
@apiGroup Schedule
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения расписания приема специалиста за заданный промежуток дат<br/>
Валидация JSON Schema <a href="/json-data/schedule/data/schedule-schema.json">schedule-schema.json</a><br/>
JSON пример <a href="/json-data/schedule/data/schedule-success-example.json">schedule-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} doctor_id Код специалиста
@apiParam {Date} date_begin Дата начала в формате yyyy-mm-dd.
@apiParam {Date} date_end Дата завершения в формате yyyy-mm-dd.

@apiUse ScheduleSuccess
"""