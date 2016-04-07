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
@api {get} /risar/api/integration/<int:api_version>/anamnesis/prevpregnancy/schema.json json-schema prevpregnancy
@apiName PrevPregnancySchema
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Получение данных json-schema по предыдущим беременностям

@apiParam {Number} api_version Версия API, целое положительной число

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {post} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/prevpregnancy/ Регистрация предыдущих беременностей матери
@apiName PostPreviousPregnancy
@apiGroup Anamnesis-Pregnancy
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных предыдущих беременностей матери<br/>
Валидация JSON Scheme <a href="/json-data/anamnesis/previous-pregnancy/data/anamnesis-prev-pregnancy-schema.json">anamnesis-prev-pregnancy-schema.json</a><br/>
JSON пример запроса <a href="/json-data/anamnesis/previous-pregnancy/data/anamnesis-prev-pregnancy-example.json">anamnesis-prev-pregnancy-example.json</a><br/>
JSON пример ответа <a href="/json-data/anamnesis/previous-pregnancy/data/anamnesis-prev-pregnancy-response.json">anamnesis-prev-pregnancy-response.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {String} card_id Код карты пациента

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/prevpregnancy/<prevpregnancy_id> Изменение предыдущих беременностей матери
@apiName PutPreviousPregnancy
@apiGroup Anamnesis-Pregnancy
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных предыдущих беременностей матери<br/>
Валидация JSON Scheme <a href="/json-data/anamnesis/previous-pregnancy/data/anamnesis-prev-pregnancy-schema.json">anamnesis-prev-pregnancy-schema.json</a><br/>
JSON пример запроса <a href="/json-data/anamnesis/previous-pregnancy/data/anamnesis-prev-pregnancy-example.json">anamnesis-prev-pregnancy-example.json</a><br/>
JSON пример ответа <a href="/json-data/anamnesis/previous-pregnancy/data/anamnesis-prev-pregnancy-response.json">anamnesis-prev-pregnancy-response.json</a>

@apiParam {Number} api_version Версия API от целое положительной число
@apiParam {String} card_id Код карты пациента
@apiParam {String} prevpregnancy_id Код документа предыдущей беременности

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/prevpregnancy/<prevpregnancy_id> Удаление предыдущих беременностей матери
@apiName DeletePreviousPregnancy
@apiGroup Anamnesis-Pregnancy
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных предыдущих беременностей матери

@apiParam {Number} api_version Версия API от целое положительной число
@apiParam {String} card_id Код карты пациента
@apiParam {String} prevpregnancy_id Код документа предыдущей беременности

@apiUse CreateSuccess

@apiUse CreateError
"""
