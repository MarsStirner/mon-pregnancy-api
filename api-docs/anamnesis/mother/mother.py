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
@api {post} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/mother/ Регистрация анамнеза матери
@apiName PostMother
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных анамнеза матери

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {String} card_id Код карты пациента

@apiParamExample {json} Request-Example:
{}

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/mother/<anamnesis_id> Изменение анамнеза матери
@apiName PutMother
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных анамнеза матери

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {String} card_id Код карты пациента
@apiParam {String} anamnesis_id Код документа анамнеза

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<card_id>/anamnesis/mother/<anamnesis_id> Удаление анамнеза матери
@apiName DeleteMother
@apiGroup Anamnesis
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных анамнеза матери.

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {String} card_id Код карты пациента
@apiParam {String} anamnesis_id Код документа анамнеза

@apiUse CreateSuccess

@apiUse CreateError
"""