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
@api {post} /risar/api/integration/<int:api_version>/card/<external_system_id>/<external_card_id>/epicrisis/ Регистрация эпикриза
@apiName PostEpicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных эпикриза случая беременности.<br/>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/epicrisis/data/epicrisis-register-scheme.json">epicrisis-register-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/epicrisis/data/epicrisis-register-example.json">epicrisis-register-example.json</a>.



@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты пациента во внешней учетной системе.

@apiParamExample {json} Request-Example:
{}

@apiUse CreateSuccess

@apiUse CreateError

"""


"""
@api {put} /risar/api/integration/<int:api_version>/card/<external_system_id>/<external_card_id>/epicrisis/ Изменение эпикриза
@apiName PutEpicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных эпикриза случая беременности.<br/>
Валидация JSON Scheme _.<br/>
JSON пример _.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<external_system_id>/<external_card_id>/epicrisis/ Удаление эпикриза
@apiName DeleteEpicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных данных эпикриза случая беременности.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе

@apiUse CreateSuccess

@apiUse CreateError
"""