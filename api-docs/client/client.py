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
    "registration_address": {
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

        "medicine_intolerance_power": 4,
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
@apiError (Error 4xx) {json} 400 исключительная ситуация, ошибка валидации переданных данных
@apiError (Error 4xx) {json} 404 ошибка, запрашиваемый ресурс не найден
@apiError (Error 4xx) {json} 409 ошибка, попытка создания дублирующей записи
@apiError (Error 5xx) {json} 500 исключительная ситуация, ошибка: внутренняя ошибка сервера

@apiErrorExample {json} Ошибка
{
  "meta": {
    "code": 400,
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
    "name": "Невалидные данные",
    "traceback": [

    ]
  },
  "result": null
}
"""

"""
@api {post} /risar/api/integration/<int:api_version>/client/ Регистрация пациента
@apiName PostClient
@apiGroup Client
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации пациента<br/>
Валидация JSON Scheme <a href="/json-data/client/data/client-scheme.json">client-scheme.json</a><br/>
JSON пример запроса <a href="/json-data/client/data/client-register-example.json">client-register-example.json</a><br/>
JSON пример ответа <a href="/json-data/client/data/client-all-response-successful-example.json">client-all-response-successful-example.json</a>

@apiParam {Number} api_version Версия API, целое положительное число

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
    "registration_address": {
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
           "medicine_intolerance_power": 4,
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
@api {put} /risar/api/integration/<int:api_version>/client/<int:client_id> Изменение пациента
@apiName PutClient
@apiGroup Client
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных пациента<br/>
Валидация JSON Scheme <a href="/json-data/client/data/client-scheme.json">client-scheme.json</a><br/>
JSON пример запроса <a href="/json-data/client/data/client-change-example.json">client-change-example.json</a><br/>
JSON пример ответа <a href="/json-data/client/data/client-all-response-successful-example.json">client-all-response-successful-example.json</a>

@apiParam {Number} api_version Версия API, целое положительное число
@apiParam {String} client_id Код пациента

@apiUse CreateClientSuccess

@apiUse CreateClientError
"""