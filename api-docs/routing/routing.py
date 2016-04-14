"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine RoutingSuccess
@apiSuccess (Success 2xx) {json} 200 Данные.
@apiSuccessExample {json} Успешный ответ
{
    "meta":{
        "code": "200",
        "name": "ОК"
    },
    "data": {
        "hospital_planned": "hospital_code_012345",
        "hospital_emergency": "hospital_code_012346",
        "hospital_planned_list": [],
        "hospital_emergency_list": ["hospital_code_012348", "hospital_code_012349"]
    }
}
"""


"""
@api {Result} /risar/api/integration/<int:api_version>/card/<card_id>/routing/ Описание ошибок
@apiName Routing
@apiGroup Routing
@apiVersion 0.1.0
@apiDescription Описание ошибок

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<int:api_version>/card/<card_id>/routing/ Получение списка ЛПУ
@apiName GetRouting
@apiGroup Routing
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения информации об ЛПУ для госпитализации пациентки<br/>
Валидация JSON Schema <a href="/json-data/routing/data/routing-schema.json">routing-schema.json</a><br/>
JSON пример <a href="/json-data/routing/data/routing-success-example.json">routing-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.

@apiUse RoutingSuccess
"""