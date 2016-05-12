"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine ErrandListSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{
    "meta":{
        "code": "200",
        "name": "ОК"
    },
    "data": [
        {
            "errand_id": "012345",
            "hospital": "hospital_code_0123456",
            "doctor": "doctor_code_0123456",
            "date": "2011-11-11",
            "comment": "требуется выполнить поручение",
            "execution_hospital": "hospital_code_0123457",
            "execution_doctor": "doctor_code_0123457",
            "status": "executed",
            "execution_date": "2011-11-11",
            "execution_comment": "комментарий"
        },
        {
            "errand_id": "543210",
            "hospital": "hospital_code_0123456",
            "doctor": "doctor_code_0123456",
            "date": "2011-11-11",
            "comment": "требуется выполнить поручение",
            "execution_hospital": "hospital_code_0123457",
            "execution_doctor": "doctor_code_0123457",
            "status": "waiting"
        }
    ]
}
"""


"""
@api {get} /risar/api/integration/<int:api_version>/card/<card_id>/errands/ Получение списка поручений
@apiName GetErrandList
@apiGroup Errands
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения списка поручений<br/>
Валидация JSON Schema <a href="/json-data/errand/data/errand-list-schema.json">errand-list-schema.json</a><br/>
JSON пример <a href="/json-data/errand/data/errand-list-success-example.json">errand-list-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.

@apiUse ErrandListSuccess
"""