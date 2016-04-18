"""
@apiVersion 0.1.0
"""

"""
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/errands/ Описание ошибок.
@apiName Errand
@apiGroup Errands
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiUse CreateError
"""


"""
@api {post} /risar/api/integration/<int:api_version>/card/<card_id>/errands/<errand_id> Регистрация результатов поручения
@apiName PostErrand
@apiGroup Errands
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации результатов поручения.<br/>
Валидация JSON Schema: <a href="/json-data/errand/data/errand-all-schema.json">errand-all-schema.json</a>.<br/>
JSON пример: <a href="/json-data/errand/data/errand-all-example.json">errand-all-example.json</a>.


@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} errand_id Код поручения.

@apiParamExample {json} Request-Example:
{
    "execution_date": "2011-11-11",
    "execution_comment": "комментарий"
}


@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{
    "meta":{
        "code": "200",
        "name": "ОК"
    },
    "data": {
        "execution_date": "2011-11-11",
        "execution_comment": "комментарий"
    }
}
"""


"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id>/errands/<errand_id> Изменение результатов поручения
@apiName PutErrand
@apiGroup Errands
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения результатов поручения.<br/>
Валидация JSON Schema: <a href="/json-data/errand/data/errand-all-schema.json">errand-all-schema.json</a>.<br/>
JSON пример: <a href="/json-data/errand/data/errand-all-example.json">errand-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} errand_id Код поручения.
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<card_id>/errands/<errand_id> Удаление результатов поручения
@apiName DeleteErrand
@apiGroup Errands
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления результатов поручения.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} errand_id Код поручения.
"""