"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine MeasuresListSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "ОК"
    },
    "data": [
        {
            "measure_id": "7654321",
            "measure_type_code": "000123",
            "begin_datetime": "2012-04-23",
            "end_datetime": "2012-04-23",
            "status": "012",
            "result_action_id": "1234567"
        },
        {
            "measure_id": "7654322",
            "measure_type_code": "000123",
            "begin_datetime": "2012-04-23",
            "end_datetime": "2012-04-23",
            "status": "012",
            "result_action_id": "1234568"
        }        
    ]
}
"""


"""
@api {Result} /risar/api/integration/<int:api_version>/card/<card_id>/measures/ Описание ошибок
@apiName MeasuresList
@apiGroup Measures
@apiVersion 0.1.0
@apiDescription Описание ошибок

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<int:api_version>/card/<card_id>/measures/list/?date_begin=<date_begin>&date_end=<date_end> Получение списка мероприятий
@apiName GetMeasuresList
@apiGroup Measures
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения списка мероприятий за заданный промежуток времени<br/>
Валидация JSON Schema <a href="/json-data/measures/data/measures-list-schema.json">measures-list-schema.json</a><br/>
JSON пример <a href="/json-data/measures/data/measures-list-success-example.json">measures-list-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Date} date_begin Дата начала в формате yyyy-mm-dd.
@apiParam {Date} date_end Дата завершения в формате yyyy-mm-dd.

@apiUse MeasuresListSuccess
"""