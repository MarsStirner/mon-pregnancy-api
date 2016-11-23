"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine EpicrisisCreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{
  "meta":{
    "code": "200",
    "name": "ОК"
  },
  "data": {
    "epicrisis": {
      "hospital_chief_doctor": "",
      "hospital_doctor": "",
      "date_close": "2011-11-11"
    }
  }
}
"""


"""
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/checkup/ Описание ошибок и успешных ответов.
@apiName Epicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiUse EpicrisisCreateSuccess

@apiUse CreateError
"""


"""
@api {post} /risar/api/integration/<int:api_version>/card/<card_id>/epicrisis/ Завершение случая беременности
@apiName PostEpicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных завершения случая беременности.<br/>
Валидация JSON Scheme: <a href="/json-data/epicrisis/data/epicrisis-all-scheme.json">epicrisis-all-scheme.json</a>.<br/>
JSON пример: <a href="/json-data/epicrisis/data/epicrisis-all-example.json">epicrisis-all-example.json</a>.


@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.

@apiParamExample {json} Request-Example:
{
  "epicrisis": {
    "hospital_chief_doctor": "",
    "hospital_doctor": "",
    "date_close": "2011-11-11"
  }
}
"""


"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id>/epicrisis/ Изменение данных завершения случая беременности
@apiName PutEpicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных завершения случая беременности.<br/>
Валидация JSON Scheme: <a href="/json-data/epicrisis/data/epicrisis-all-scheme.json">epicrisis-all-scheme.json</a>.<br/>
JSON пример: <a href="/json-data/epicrisis/data/epicrisis-all-example.json">epicrisis-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<card_id>/epicrisis/ Удаление данных завершения случая беременности
@apiName DeleteEpicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных данных завершения случая беременности.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
"""