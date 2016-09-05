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
                    "end_time": "13:00",
                    "quantity": 2
                },
                {
                    "begin_time": "14:00",
                    "end_time": "18:00",
                    "quantity": 2
                }
            ]
        },
        {
            "date": "2012-12-12",
            "intervals": [
                {
                    "begin_time": "10:00",
                    "end_time": "17:00",
                    "quantity": 4
                }
            ]
        }
    ]
}

"""

"""
@api {Result} /risar/api/integration/<int:api_version>/schedule/<hospital_code>/<doctor_code> Описание ошибок
@apiName Schedule
@apiGroup Schedule
@apiVersion 0.1.0
@apiDescription Описание ошибок

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<int:api_version>/schedule/<hospital_code>/<doctor_code>/?date_begin=<date_begin>&date_end=<date_end> Получение расписания специалиста
@apiName GetScheduleList
@apiGroup Schedule
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения расписания приема специалиста за заданный промежуток дат<br/>
Валидация JSON Schema <a href="/json-data/schedule/data/schedule-schema.json">schedule-schema.json</a><br/>
JSON пример <a href="/json-data/schedule/data/schedule-success-example.json">schedule-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} hospital_code Код ЛПУ
@apiParam {Int} doctor_code Код специалиста
@apiParam {Date} date_begin Дата начала в формате yyyy-mm-dd.
@apiParam {Date} date_end Дата завершения в формате yyyy-mm-dd.

@apiUse ScheduleSuccess
"""

"""
@api {post} /risar/api/integration/<int:api_version>/schedule/<hospital_code>/<doctor_code>/ Регистрация расписания специалиста
@apiName PostScheduleList
@apiGroup Schedule
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных расписания приема специалиста<br/>
Валидация JSON Schema <a href="/json-data/schedule/data/schedule-schema.json">schedule-schema.json</a><br/>
JSON пример <a href="/json-data/schedule/data/schedule-success-example.json">schedule-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {Int} hospital_code Код ЛПУ
@apiParam {Int} doctor_code Код специалиста

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {put} /risar/api/integration/<api_version>/schedule/<hospital_code>/<doctor_code>/ Изменение расписания специалиста
@apiName PutScheduleList
@apiGroup Schedule
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Метод предназначен для изменения данных расписания приема специалиста<br/>
Валидация JSON Schema <a href="/json-data/schedule/data/schedule-schema.json">schedule-schema.json</a><br/>
JSON пример <a href="/json-data/schedule/data/schedule-success-example.json">schedule-success-example.json</a>


@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} hospital_code Код ЛПУ
@apiParam {Int} doctor_code Код специалиста

"""

"""
@api {delete} /risar/api/integration/<api_version>/schedule/<hospital_code>/<doctor_code>/<date> Удаление расписания специалиста
@apiName DeleteSchedule
@apiGroup Schedule
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Метод предназначен для удаления расписания приема специалиста на выбранную дату<br/>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} hospital_code Код ЛПУ
@apiParam {Int} doctor_code Код специалиста
@apiParam {Date} date Дата в формате yyyy-mm-dd

"""