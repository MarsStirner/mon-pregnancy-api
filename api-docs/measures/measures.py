"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine CreateResearchSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного исследования.
@apiSuccessExample {json} Успешный ответ

{"meta":{
"code":"200", 
"result": {
  "result_action_id": "123456",
  "external_id": "qwerty_012345",
  "event_measure_id": "235",
  "measure_type_code": "52",
  "realization_date": "2004-10-31",
  "lpu_code": "16787",
  "analysis_number": "105-У",
  "results": "11111111",
  "comment": "Результаты в пределах нормы",
  "doctor_code": "136"
  }
}
}
"""
"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine EditResearchSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного исследования.
@apiSuccessExample {json} Успешный ответ

{"meta":{
"code":"200", 
"result": {
  "result_action_id": "123456",
  "external_id": "qwerty_012345",
  "event_measure_id": "235",
  "measure_type_code": "52",
  "realization_date": "2004-10-31",
  "lpu_code": "16787",
  "analysis_number": "105-У",
  "results": "11111111",
  "comment": "Результаты в пределах нормы",
  "doctor_code": "136"
  }
}
}
"""
"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine CreateSpecialistsCheckupSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного осмотра врачом-специалистом.
@apiSuccessExample {json} Успешный ответ

{"meta":{
"code":"200", 
"result": {
  "result_action_id": "123456",
  "external_id": "qwerty_012345",
  "event_measure_id": "55",
  "measure_type_code": "52",
  "checkup_date": "2004-10-31",
  "lpu_code": "16787",
  "doctor_code": "136",
  "analysis_number": "105-У",
  "diagnosis": "036.5"
  }
}
}
"""
"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine EditSpecialistsCheckupSuccess
@apiSuccess (Success 2xx) {json} 200 Данные успешного сохранения изменений результатов осмотра.
@apiSuccessExample {json} Успешный ответ

{"meta":{
"code":"200", 
"result": { 
  "result_action_id": "123456",
  "external_id": "qwerty_012345",
  "event_measure_id": "55",
  "measure_type_code": "52",
  "checkup_date": "2004-10-31",
  "lpu_code": "16787",
  "doctor_code": "136",
  "analysis_number": "105-У",
  "diagnosis": "036.5"
  }
}
}
"""
"""
------------------------------------------------------------------------------------------
Current Errors.
------------------------------------------------------------------------------------------

@apiDefine CreateResearchError
@apiVersion 0.1.0
@apiError (Error 4xx) {json} 400 исключительная ситуация, ошибка валидации переданных данных
@apiError (Error 4xx) {json} 404 ошибка, запрашиваемый ресурс не найден
@apiError (Error 5xx) {json} 500 исключительная ситуация, ошибка: внутренняя ошибка сервера 


"""

"""
@api {post} /risar/api/integration/<int:api_version>/card/<card_id>/measures/research Регистрация результатов лабораторных и функциональных исследований
@apiName PostResearch
@apiGroup Measures
@apiVersion 0.1.0
@apiDescription Метод предназначен для добавления результатов функциональных и лабораторных исследований

Валидация JSON Scheme: <a href="/json-data/measures/data/research-scheme.json">research-scheme.json</a>.

JSON пример: <a href="/json-data/measures/data/research-example.json">research-example.json</a>

@apiParam {Number} api_version Версия API от целое положительной число
@apiParam {String} card_id Код карты пациентки

@apiParamExample {json} Request-Example:
{
  "external_id": "qwerty_012345",
  "measure_id": "7654321",
  "measure_type_code": "52",
  "realization_date": "2004-10-31",
  "lpu_code": "16787",
  "analysis_number": "105-У",
  "results": "11111111",
  "comment": "Результаты в пределах нормы",
  "doctor_code": "136"
}

@apiUse CreateResearchSuccess

"""

"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id>/measures/<result_action_id>/research Изменение результатов функциональных и лабораторных исследований
@apiName PutResearch
@apiGroup Measures
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных по результатам функциональных и лабораторных исследований
Валидация JSON Scheme <a href="/json-data/measures/data/research-scheme.json">research-scheme.json</a>.
JSON пример <a href="/json-data/measures/data/research-example.json">research-example.json</a>

@apiParam {Number} api_version Версия API от целое положительной число.1
@apiParam {String} card_id Код карты пациентки
@apiParam {String} result_action_id Код действия результатов мероприятия
@apiUse EditResearchSuccess

@apiParamExample {json} Request-Example:
{
  "measure_type_code": "52",
  "realization_date": "2004-10-31",
  "lpu_code": "16787",
  "analysis_number": "105-У",
  "results": "11111111",
  "comment": "Результаты в пределах нормы",
  "doctor_code": "136"
}
"""
"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id>/measures/<result_action_id>/specialists_checkup Изменение результатов осмотра пациентки врачом-специалистом
@apiName PutSpecialistsCheckup
@apiGroup Measures
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных по результатам осмотра пациентки врачом-специалистом
Валидация JSON Scheme: <a href="/json-data/measures/data/specialists_checkup-scheme.json">specialists_checkup-scheme.json</a>.
JSON пример: <a href="/json-data/measures/data/specialists_checkup-example.json">specialists_checkup-example.json</a>

@apiParam {Number} api_version Версия API от целое положительной число.1
@apiParam {String} card_id Код карты пациентки
@apiParam {String} result_action_id Код действия результатов мероприятия

@apiUse EditSpecialistsCheckupSuccess

@apiParamExample {json} Request-Example:
{
  "external_id": "qwerty_012345",
  "measure_id": "7654321",
  "measure_type_code": "52",
  "checkup_date": "2004-10-31",
  "lpu_code": "16787",
  "doctor_code": "136",
  "analysis_number": "105-У",
  "diagnosis": "036.5"
}
"""

"""
@api {post} /risar/api/integration/<int:api_version>/card/<card_id>/measures/specialists_checkup Регистрация результатов осмотра пациентки врачом-специалистом
@apiName PostSpecialistsCheckup
@apiGroup Measures
@apiVersion 0.1.0
@apiDescription Метод предназначен для добавления результатов осмотра пациентки врачом-специалистом
Валидация JSON Scheme: <a href="/json-data/measures/data/specialists_checkup-scheme.json">specialists_checkup-scheme.json</a>.
JSON пример: <a href="/json-data/measures/data/specialists_checkup-example.json">specialists_checkup-example.json</a>

@apiParam {Number} api_version Версия API от целое положительной число
@apiParam {String} card_id Код карты пациентки

@apiParamExample {json} Request-Example:
{
  "external_id": "qwerty_012345",
  "measure_id": "7654321",
  "measure_type_code": "52",
  "checkup_date": "2004-10-31",
  "lpu_code": "16787",
  "doctor_code": "136",
  "analysis_number": "105-У",
  "diagnosis": "036.5"
}

@apiUse CreateSpecialistsCheckupSuccess

"""