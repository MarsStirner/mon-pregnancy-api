"""
@apiVersion 0.1.0
"""


"""
@api {Result} /risar/api/integration/<api_version>/reference_books/ Описание ошибок и успешных ответов
@apiName ErrorReferenceBook
@apiGroup ReferenceBooks
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiSuccess (Success 2xx) {json} 200 Данные справочника
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
     "data": {
        "code": "asnoe", 
        "value": "ясное"
    }
}


@apiUse CreateError
"""


"""
@api {post} /risar/api/integration/<api_version>/reference_books/<reference_book_code> Регистрация значения справочника
@apiName PostReferenceBook
@apiGroup ReferenceBooks
@apiVersion 0.1.0
@apiDescription Метод предназначен для добавление записи в справочник<br/>
Валидация JSON Schema <a href="/json-data/reference_books/data/reference_book_item-schema.json">reference_book_item-schema.json</a><br/>
JSON пример <a href="/json-data/reference_books/data/reference_book_item-example.json">reference_book_item-example.json</a><br/>
JSON пример успешный ответ: <a href="/json-data/reference_books/data/reference_book_item-success-example.json">reference_book_item-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {String} reference_book_code Код справочника

@apiParamExample {json} Request-Example:
{
    "code": "asnoe", 
    "value": "ясное"
}
"""


"""
@api {put} /risar/api/integration/<api_version>/reference_books/<reference_book_code>/<item_code> Изменение значения справочника
@apiName PutReferenceBook
@apiGroup ReferenceBooks
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения записи справочника<br/>
Валидация JSON Schema <a href="/json-data/reference_books/data/reference_book_item-schema.json">reference_book_item-schema.json</a><br/>
JSON пример <a href="/json-data/reference_books/data/reference_book_item-example.json">reference_book_item-example.json</a><br/>
JSON пример успешный ответ: <a href="/json-data/reference_books/data/reference_book_item-success-example.json">reference_book_item-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {String} reference_book_code Код справочника
@apiParam {String} item_code Код значения справочника
"""


"""
@api {delete} /risar/api/integration/<api_version>/reference_books/<reference_book_code>/<item_code> Удаление значения справочника
@apiName DeleteReferenceBook
@apiGroup ReferenceBooks
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления значения из справочника

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {String} reference_book_code Код справочника
@apiParam {String} item_code Код значения справочника
"""