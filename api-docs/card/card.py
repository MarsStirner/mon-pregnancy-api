"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine CreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного клиента.
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

@apiErrorExample {json} Ошибка
{
  "meta": {
    "code": 406,
    "errors": [
      {
        "instance": {
          "insurance_document_series": "0944",
          "insurance_document_issuing_authority": "22001",
          "insurance_document_beg_date": "03-02-02",
          "insurance_document_number": "7837833"
        },
        "path": "insurance_documents/0",
        "error": "'insurance_document_type' is a required property"
      }
    ],
    "name": "Не валидные данные",
    "traceback": [

    ]
  },
  "result": null
}
"""

"""
@api {post} /risar/api/integration/<int:api_version>/card/<external_system_id>/ Регистрация медицинской карты
@apiName PostCard
@apiGroup Card
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации медицинской карты и постановки на учет<br/>
Валидация JSON Scheme _.<br/>
JSON пример _.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_client_id Код пациента во внешней учетной системе.

@apiParamExample {json} Request-Example:
{}

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {put} /risar/api/integration/<int:api_version>/card/<external_system_id>/<external_card_id> Изменение медицинской карты
@apiName PutCard
@apiGroup Card
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных медицинской карты.<br/>
Валидация JSON Scheme _.<br/>
JSON пример _.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<external_system_id>/<external_card_id> Удаление медицинской карты
@apiName DeleteCard
@apiGroup Card
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных медицинской карты.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе

@apiUse CreateSuccess

@apiUse CreateError
"""