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
@apiDefine PuerperaExaminationCreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного осмотра.
@apiSuccessExample {json} Успешный ответ
{
  "status":{
    "code": "200",
    "name": "ОК",
    "exam_puerpera_id": "123456"
    },
  "data": {
    "date": "2011-11-12",
    "time": "18:00",
    "date_of_childbirth": "2011-11-11",
    "hospital": "ЛПУ",
    "doctor": "Иванов И.И.",
    "time_since_childbirth": 1,
    "state": "srednejtajesti",
    "ad_right_high": 120,
    "ad_left_high": 120,
    "ad_right_low": 80,
    "ad_left_low": 80,
    "veins": "noma",
    "diagnosis": "Q00.0",
    "contraception_recommendations": "01",
    "recommendations": "апельсиновый сок 3 р.д. натощак"
  }
}
"""

"""
------------------------------------------------------------------------------------------
Current Errors.
------------------------------------------------------------------------------------------

@apiDefine CreateError
@apiVersion 0.1.0
@apiError (Error 5xx) {json} 500 исключительная ситуация, ошибка: внутренняя ошибка сервера
@apiError (Error 4xx) {json} 406 исключительная ситуация, ошибка валидации переданных данных
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
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/checkup/ Описание ошибок и успешных ответов.
@apiName PuerPeraExamination
@apiGroup PuerPera-Examination
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiUse PuerperaExaminationCreateSuccess

@apiUse CreateError
"""

"""
@api {post} /risar/api/integration/<api_version>/card/<card_id>/checkup/puerpera/ Регистрация осмотров родильницы
@apiName PostPuerPeraExamination
@apiGroup PuerPera-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Регистрация данных осмотра родильницы.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/puerperacheckout/data/puerperacheckout-all-scheme.json">puerperacheckout-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/puerperacheckout/data/puerperacheckout-all-example.json">puerperacheckout-all-example.json</a>.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
"""

"""
@api {put} /risar/api/integration/<api_version>/card/<card_id>/checkup/puerpera/<exam_puerpera_id>/ Изменение осмотров родильницы
@apiName PutPuerPeraExamination
@apiGroup PuerPera-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Изменение данных осмотра родильницы.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/puerperacheckout/data/puerperacheckout-all-scheme.json">puerperacheckout-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/puerperacheckout/data/puerperacheckout-all-example.json">puerperacheckout-all-example.json</a>.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
@apiParam {String} external_exam_puerpera_id Код осмотра родильницы во внешней учетной системе.
"""

"""
@api {delete} /risar/api/integration/<api_version>/card/<card_id>/checkup/puerpera/<exam_puerpera_id> Удаление осмотров родильницы
@apiName DeletePuerPeraExamination
@apiGroup PuerPera-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Удаление данных осмотра родильницы.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
@apiParam {String} external_exam_puerpera_id Код осмотра родильницы во внешней учетной системе.
"""

"""
@api {get} /risar/api/integration/<api_version>/card/<card_id>/checkup/puerpera/ Получение списка осмотров родильницы
@apiName GetPuerPeraExamination
@apiGroup PuerPera-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Получение списка осмотров родильницы.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
"""