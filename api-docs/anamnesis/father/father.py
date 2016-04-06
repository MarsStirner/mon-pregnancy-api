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
@api {get} /risar/api/integration/<int:api_version>/anamnesis/father/schema.json json-schema
@apiName AnamnesisFatherSchema
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Получение данных json-schema по анамнезу отца

@apiParam {Number} api_version Версия API, целое положительной число

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {post} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/father/ Регистрация анамнеза отца
@apiName PostFather
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных анамнеза отца<br/>
Валидация JSON Scheme <a href="/json-data/anamnesis/father/data/father_anamnesis_schema.json">father_anamnesis_schema.json</a><br/>
JSON пример <a href="/json-data/anamnesis/father/data/father_anamnesis_example.json">father_anamnesis_example.json</a>

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {String} card_id Код карты пациента

@apiParamExample {json} Request-Example:
{}

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/father/<anamnesis_id> Изменение анамнеза отца
@apiName PutFather
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных анамнеза отца<br/>
Валидация JSON Scheme <a href="/json-data/anamnesis/father/data/father_anamnesis_schema.json">father_anamnesis_schema.json</a><br/>
JSON пример <a href="/json-data/anamnesis/father/data/father_anamnesis_example.json">father_anamnesis_example.json</a>

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {String} card_id Код карты пациента
@apiParam {String} anamnesis_id Код документа анамнеза

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/father/<anamnesis_id> Удаление анамнеза отца
@apiName DeleteFather
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных анамнеза отца

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {String} card_id Код карты пациента
@apiParam {String} anamnesis_id Код документа анамнеза

@apiUse CreateSuccess

@apiUse CreateError
"""