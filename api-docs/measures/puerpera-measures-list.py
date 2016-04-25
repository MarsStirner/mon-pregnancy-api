"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine PuerperaMeasuresListSuccess
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
            "status": "012"
        },
        {
            "measure_id": "7654322",
            "measure_type_code": "000123",
            "begin_datetime": "2012-04-23",
            "end_datetime": "2012-04-23",
            "status": "012"
        }        
    ]
}
"""


"""
@api {Result} /risar/api/integration/<int:api_version>/card/<card_id>/puerpera_measures/ Описание ошибок
@apiName PuerperaMeasuresList
@apiGroup Measures
@apiVersion 0.1.0
@apiDescription Описание ошибок

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<int:api_version>/card/<card_id>/measures/list/puerpera_checkup_date Получение списка мероприятий родильницы
@apiName GetPuerperaMeasuresList
@apiGroup Measures
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения списка мероприятий родильницы, которые были созданы в указанную дату осмотра<br/>
Валидация JSON Schema <a href="/json-data/measures_list/data/measures-list-schema.json">measures-list-schema.json</a><br/>
JSON пример <a href="/json-data/measures_list/data/measures-list-success-example.json">measures-list-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Date} puerpera_checkup_date Дата осмотра родильницы в формате yyyy-mm-dd.

@apiUse PuerperaMeasuresListSuccess
"""