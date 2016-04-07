"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine CreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{}
"""

"""
------------------------------------------------------------------------------------------
Current Errors.
------------------------------------------------------------------------------------------

@apiDefine CreateError
@apiVersion 0.1.0
@apiError (Error 5xx) {json} 500 исключительная ситуация, ошибка: внутренняя ошибка сервера
@apiError (Error 4xx) {json} 404 ошибка, запрашиваемый ресурс не найден

"""

"""
@api {get} /risar/api/integration/<int:api_version>/anamnesis/mother/schema.json json-schema mother
@apiName AnamnesisMotherSchema
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Получение данных json-schema по анамнезу матери

@apiParam {Number} api_version Версия API, целое положительной число

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {post} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/mother/ Регистрация анамнеза матери
@apiName PostMother
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных анамнеза матери<br/>
Валидация JSON Scheme <a href="/json-data/anamnesis/mother/data/mother-anamnesis-schema.json">mother-anamnesis-schema.json</a><br/>
JSON пример запроса <a href="/json-data/anamnesis/mother/data/mother-anamnesis-example.json">mother-anamnesis-example.json</a><br/>
JSON пример ответа <a href="/json-data/anamnesis/mother/data/mother-anamnesis-response.json">mother-anamnesis-response.json</a>

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {String} card_id Код карты пациента

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/mother/ Изменение анамнеза матери
@apiName PutMother
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных анамнеза матери
Валидация JSON Scheme <a href="/json-data/anamnesis/mother/data/mother-anamnesis-schema.json">mother-anamnesis-schema.json</a><br/>
JSON пример запроса <a href="/json-data/anamnesis/mother/data/mother-anamnesis-example.json">mother-anamnesis-example.json</a><br/>
JSON пример ответа <a href="/json-data/anamnesis/mother/data/mother-anamnesis-response.json">mother-anamnesis-response.json</a>

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {String} card_id Код карты пациента

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/mother/ Удаление анамнеза матери
@apiName DeleteMother
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных анамнеза матери

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {String} card_id Код карты пациента

@apiUse CreateSuccess

@apiUse CreateError
"""