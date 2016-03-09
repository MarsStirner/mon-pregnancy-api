"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine CreateClientSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного клиента.
@apiSuccessExample {json} Успешный ответ
{
  "meta":{
    "code": "200",
    "name": "ОК"
  },
  "result":
  {
    "FIO": {
      "middlename": "Иванова",
      "name": "Василиса",
      "surname": "Петровна"
    },
    "birthday_date": "1990-02-12",
    "gender": 2,
    "document": {
      "document_type_code": 14,
      "document_series": "4004",
      "document_number": "342908",
      "document_beg_date": "2004-10-31",
      "document_issuing_authority": "ТП № 30 отдела УФМС по СПб и Лен.области"
    },
    "residential_address": {
      "KLADR_locality": "7800000000000",
      "KLADR_street": "78000000000076900",
      "house": "12а",
      "flat": "404",
      "locality_type": 1
    },
    "blood_type_info": [
      {
        "blood_type": "B(III)Rh+"
      }
    ],
    "allergies_info": [
      {

        "allergy_power": 4,
        "allergy_substance": "ромашка"
      }
    ],
    "medicine_intolerance_info": [
      {

        "medicine_intolerance__power": 4,
        "medicine_substance": "анальгетики"
      }
    ],
    "patient_external_code": "47584934859034854",
    "patient_risar_id": "347483"
  }
}

"""

"""
------------------------------------------------------------------------------------------
Current Errors.
------------------------------------------------------------------------------------------

@apiDefine CreateClientError
@apiVersion 0.1.0
@apiError (Error 4xx) {json} 406 исключительная ситуация, ошибка валидации переданных данных
@apiError (Error 4xx) {json} 404 ошибка, запрашиваемый ресурс не найден
@apiError (Error 5xx) {json} 500 исключительная ситуация, ошибка: внутренняя ошибка сервера

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
@api {post} /risar/api/integration/<int:api_version>/client/<external_system_id>/ Регистрация пациенток
@apiName PostClient
@apiGroup Client
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации пациентов
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/client/data/client-register-scheme.json">client-register-scheme.json</a>.
JSON пример: <a href="/mon-pregnancy-api/api-docs/client/data/client-register-example.json">client-register-example.json</a>

@apiParam {Number} api_version Версия API от целое положительной число
@apiParam {String} external_system_id Код внешней системы.

@apiParamExample {json} Request-Example:
   {
     "FIO": {
       "middlename": "Иванова",
       "name": "Василиса",
       "surname": "Петровна"
     },
     "birthday_date": "1990-02-12",
     "SNILS":"11223344595",
     "gender": 2,
     "document": {
       "document_type_code": 14,
       "document_series": "4004",
       "document_number": "342908",
       "document_beg_date": "2004-10-31",
       "document_issuing_authority": "ТП № 30 отдела УФМС по СПб и Лен.области"
     },
     "insurance_documents": [
       {
         "insurance_document_type": "2",
         "insurance_document_series": "0944",
         "insurance_document_number":"7837833",
         "insurance_document_beg_date": "03-02-02",
         "insurance_document_issuing_authority": "22001"
       }
     ],
     "residential_address": {
       "KLADR_locality": "7800000000000",
       "KLADR_street": "78000000000076900",
       "house": "12а",
       "flat": "404",
       "locality_type": 1
     },
     "blood_type_info": [
         {
           "blood_type": "B(III)Rh+"
         }
       ],
     "allergies_info": [
         {
           "allergy_power": 4,
           "allergy_substance": "ромашка"
         }
       ],
     "medicine_intolerance_info": [
         {
           "medicine_intolerance__power": 4,
           "medicine_substance": "анальгетики"
         }
      ],
     "patient_external_code": "47584934859034854"
   }

@apiUse CreateClientSuccess

@apiError (Error 4xx) {json} 400 ошибка. Пациент уже зарегистрирован в системе.
@apiUse CreateClientError

"""

"""
@api {put} /risar/api/integration/<int:api_version>/client/<external_system_id>/<external_client_id> Изменение пациента
@apiName PutClient
@apiGroup Client
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных пациента
Валидация JSON Scheme <a href="/mon-pregnancy-api/api-docs/client/data/client-change-scheme.json">client-change-scheme.json</a>.
JSON пример <a href="/mon-pregnancy-api/api-docs/client/data/client-change-example.json">client-change-example.json</a>.

@apiParam {Number} api_version Версия API от целое положительной число.1
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_client_id Код пациента во внешней учетной системе.

@apiUse CreateClientSuccess

@apiUse CreateClientError
"""