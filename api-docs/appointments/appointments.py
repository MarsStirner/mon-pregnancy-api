"""
@apiVersion 0.1.0
"""


"""
@api {Result} /risar/api/integration/<int:api_version>/card/<card_id>/appointments/ Описание ошибок
@apiName Appointment
@apiGroup Appointments
@apiVersion 0.1.0
@apiDescription Описание ошибок

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<int:api_version>/card/<card_id>/appointments/ Получение списка направлений
@apiName GetAppointmentList
@apiGroup Appointments
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения списка id направлений пациентки<br/>
Валидация JSON Schema <a href="/json-data/appointments/data/appointments-list-schema.json">appointments-list-schema.json</a><br/>
JSON пример <a href="/json-data/appointments/data/appointments-list-success-example.json">appointments-list-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.

@apiSuccess (Success 2xx) {json} 200 Данные.
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
    "data": [
        "appointment_id_0123456",
        "appointment_id_1234567"
    ]
}
"""


"""
@api {get} /risar/api/integration/<int:api_version>/card/<card_id>/appointments/<appointment_id> Получение данных направления
@apiName GetAppointment
@apiGroup Appointments
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения детальной информации о направлении<br/>
Валидация JSON Schema <a href="/json-data/appointments/data/appointment-schema.json">appointment-schema.json</a><br/>
JSON пример <a href="/json-data/appointments/data/appointment-success-example.json">appointment-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} appointment_id Код направления

@apiSuccess (Success 2xx) {json} 200 Данные.
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
    "data": {
        "measure_code": "1",
        "diagnosis": "Q00.0",
        "time": "11:11",
        "date": "2011-11-11",
        "parameters": "",
        "referral_lpu": "hospital_code_012345",
        "referral_date": "2011-11-11",
        "comment": "йцук"
    }
}
"""