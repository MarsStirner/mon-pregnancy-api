"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
 Current Permissions.
------------------------------------------------------------------------------------------
@apiDefine auth Требуется авторизация
Описание сервиса https://conf.bars-open.ru/pages/viewpage.action?pageId=19839261

@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine ConciliumCreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного консилиума.
@apiSuccessExample {json} Успешный ответ
{
  "meta":{
    "code": "200",
    "name": "ОК"
  },
  "data": {
    "concilium_id": "012345",
    "external_id": "qwerty_012345",
    "date": "2011-11-11",
    "hospital": "hospital_code_012345",
    "doctor": "doctor_code_012345",
    "doctors": [
      "doctor_code_012346",
      "doctor_code_012347"
    ],
    "diagnosis": "Q00.0",
    "reason": "Больной заболел",
    "patient_condition": "Средненькое",
    "decision": "Будем лечить"
  }
}
"""

"""
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/concilium/ Описание ошибок и успешных ответов.
@apiName Concilium
@apiGroup Concilium
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiUse ConciliumCreateSuccess

@apiUse CreateError
"""

"""
@api {post} /risar/api/integration/<api_version>/card/<card_id>/concilium/ Регистрация консилиума
@apiName PostConcilium
@apiGroup Concilium
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Регистрация данных консилиума.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/concilium/data/concilium-all-scheme.json">concilium-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/concilium/data/concilium-all-example.json">concilium-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
"""

"""
@api {put} /risar/api/integration/<api_version>/card/<card_id>/concilium/<concilium_id>/ Изменение консилиума
@apiName PutConcilium
@apiGroup Concilium
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Изменение данных консилиума.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/concilium/data/concilium-all-scheme.json">concilium-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/concilium/data/concilium-all-example.json">concilium-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} concilium_id Код консилиума.
"""

"""
@api {delete} /risar/api/integration/<api_version>/card/<card_id>/concilium/<concilium_id> Удаление консилиума
@apiName DeleteConcilium
@apiGroup Concilium
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Удаление данных консилиума.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} concilium_id Код консилиума.
"""
