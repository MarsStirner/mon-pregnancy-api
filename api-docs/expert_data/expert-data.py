"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine GetExpertDataSuccess
@apiSuccess (Success 2xx) {json} 200 Данные экспертных показателей пациентки.
@apiSuccessExample {json} Успешный ответ

{"meta":{
"code":"200", 
"result": { 
                  "risk_degree": "1",
                  "risk_diagnosis": [
                  {
                        "diagnosis_code": "O10.0",
                        "diagnosis_name":
 "Существовавшая ранее эссенциальная гипертензия, осложняющая беременность, роды и послеродовой период"
                  }
                  ],
                  "established_preeclampsia": "3",
                  "suspected_preeclampsia": "3",
                  "estimated_birth_date": "25-05-2015",
                  "risk_groups": ["5","6"],
                  "patology_groups": ["2"]
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
@apiError (Error 4xx) {json} 404 ошибка, запрашиваемый ресурс не найден или не найдена пациентка с соответствующим идентификатором
@apiError (Error 5xx) {json} 500 исключительная ситуация, ошибка: внутренняя ошибка сервера 


"""

"""
@api {get} /risar/api/integration//risar/api/integration/<int:api_version>/card/<card_id>/expert_data Передача экспертных показателей пациентки
@apiName GettExpertData
@apiGroup expert_data
@apiVersion 0.1.0
@apiDescription Метод предназначен для передачи экспертных показателей пациентки

Валидация JSON Scheme: <a href="/json-data/expert_data/data/expert-data-scheme.json">expert-data.json</a>.

JSON пример: <a href="/mon-pregnancy-api/expert_data/data/expert-data-example.json">expert-data-example.json</a>

@apiParam {Number} api_version Версия API от целое положительной число
@apiParam {String} card_id Код карты пациентки

@apiParamExample {json} Request-Example:
{
      "risk_degree": "1",
      "established_preeclampsia": "3",
      "suspected_preeclampsia": "3",
      "estimated_birth_date": "25-05-2015",
      "risk_groups": ["5","6"],
      "patology_groups": ["2"]
}

@apiUse GetExpertDataSuccess

"""

