"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine ScheduleFullSuccess
@apiSuccess (Success 2xx) {json} 200 Данные.
@apiSuccessExample {json} Успешный ответ
{
    "meta":{
        "code": "200",
        "name": "ОК"
    },
    "data": {
        "schedule_id": "123",
        "hospital": "doctor_code_123",
        "doctor": "hospital_code_123",
        "date": "2011-11-11",
        "time_begin": "09:00",
        "time_end": "10:00",
        "schedule_tickets": [
            {
                "time_begin": "09:00",
                "time_end": "09:30"
            },
            {
                "time_begin": "09:30",
                "time_end": "10:00",
                "patient": "patient_id_123"
            }
        ]
    }
}

"""

"""
@api {Result} /risar/api/integration/<int:api_version>/schedule/full/ Описание ошибок
@apiName ScheduleFull
@apiGroup ScheduleFull
@apiVersion 0.1.0
@apiDescription Описание ошибок

@apiUse CreateError
"""


"""
@api {post} /risar/api/integration/<int:api_version>/schedule/full/ Регистрация расписания (рабочего промежутка) специалиста
@apiName PostScheduleFull
@apiGroup ScheduleFull
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных расписания (рабочего промежутка) специалиста<br/>
Валидация JSON Schema <a href="/json-data/schedule/data/schedule_full-schema.json">schedule_full-schema.json</a><br/>
JSON пример <a href="/json-data/schedule/data/schedule_full-example.json">schedule_full-example.json</a>
JSON пример успешного ответа <a href="/json-data/schedule/data/schedule_full-success-example.json">schedule_full-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительное число


@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {put} /risar/api/integration/<api_version>/schedule/full/<schedule_id> Изменение расписания (рабочего промежутка) специалиста
@apiName PutScheduleFull
@apiGroup ScheduleFull
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Метод предназначен для изменения данных расписания (рабочего промежутка) специалиста<br/>
Валидация JSON Schema <a href="/json-data/schedule/data/schedule_full-schema.json">schedule_full-schema.json</a><br/>
JSON пример <a href="/json-data/schedule/data/schedule_full-example.json">schedule_full-example.json</a>
JSON пример успешного ответа <a href="/json-data/schedule/data/schedule_full-success-example.json">schedule_full-success-example.json</a>


@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} schedule_id Код расписания (рабочего промежутка)

"""

"""
@api {delete} /risar/api/integration/<api_version>/schedule/full/<schedule_id> Удаление расписания (рабочего промежутка) специалиста
@apiName DeleteScheduleFull
@apiGroup ScheduleFull
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Метод предназначен для удаления расписания приема специалиста на выбранную дату<br/>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} schedule_id Код расписания (рабочего промежутка)

"""