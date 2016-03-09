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
@apiError (Error 4xx) {json} 400 ошибка. карта не может быть изменена или удалена, так как зарегистрированны следующие документы по бизнесс процессу.

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
@api {post} /risar/api/integration/<int:api_version>/card/<external_card_id>/anamnesis/prevpregnancy/<external_system_id>/ Регистрация предыдущих беременностей матери
@apiName PostPreviousPregnancy
@apiGroup Anamnesis-Pregnancy
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных предыдущих беременностей матери.<br/>
Валидация JSON Scheme _.<br/>
JSON пример _.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты пациента во внешней учетной системе.

@apiParamExample {json} Request-Example:
{}

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {put} /risar/api/integration/<int:api_version>/card/<external_card_id>/anamnesis/prevpregnancy/<external_prevpregnancy_id>/<external_system_id> Изменение предыдущих беременностей матери
@apiName PutPreviousPregnancy
@apiGroup Anamnesis-Pregnancy
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных предыдущих беременностей матери<br/>
Валидация JSON Scheme _.<br/>
JSON пример _.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
@apiParam {String} external_prevpregnancy_id Код предыдущей беременности во внешней учетной системе.

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<external_card_id>/anamnesis/prevpregnancy/<external_prevpregnancy_id>/<external_system_id> Удаление предыдущих беременностей матери
@apiName DeletePreviousPregnancy
@apiGroup Anamnesis-Pregnancy
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных предыдущих беременностей матери

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе
@apiParam {String} external_prevpregnancy_id Код предыдущей беременности во внешней учетной системе.

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {get} /risar/api/integration/<int:api_version>/card/<external_card_id>/anamnesis/prevpregnancy/ Список предыдущих беременностей матери
@apiName GetPreviousPregnancy
@apiGroup Anamnesis-Pregnancy
@apiVersion 0.5.0
@apiDescription Метод предназначен для получения списка данных предыдущих беременностей матери

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.

@apiUse CreateSuccess

@apiUse CreateError
"""