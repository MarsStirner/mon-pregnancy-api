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
@apiDefine HospitalizationCreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненной госпитализации.
@apiSuccessExample {json} Успешный ответ
{
    "meta":{
        "code": "200",
        "name": "ОК"
    },
    "data": {
        "hospitalization_id": "123456",
        "external_id": "qwerty_012345",
        "measure_id": "7654321",
        "date_in": "2011-11-01",
        "date_out": "2011-11-11",
        "hospital": "hospital_code_012345",
        "doctor": "doctor_code_012345",
        "pregnancy_week": 25,
        "diagnosis_in": "Q00.0",
        "diagnosis_out": "Q00.0"
    }
}
"""

"""
@api {post} /risar/api/integration/<api_version>/card/<card_id>/measures/hospitalization/ Регистрация госпитализации
@apiName PostHospitalization
@apiGroup Measures
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Регистрация данных госпитализации.</br>
Валидация JSON Scheme: <a href="/json-data/measures/data/hospitalization-all-scheme.json">hospitalization-all-scheme.json</a>.<br/>
JSON пример: <a href="/json-data/measures/data/hospitalization-all-example.json">hospitalization-all-example.json</a>.<br/>
JSON пример успешный ответ: <a href="/json-data/measures/data/hospitalization-all-success-example.json">hospitalization-all-success-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.



@apiParamExample {json} Request-Example:
{
    "external_id": "qwerty_012345",
    "measure_id": "7654321",
    "date_in": "2011-11-01",
    "date_out": "2011-11-11",
    "hospital": "hospital_code_012345",
    "doctor": "doctor_code_012345",
    "pregnancy_week": 25,
    "diagnosis_in": "Q00.0",
    "diagnosis_out": "Q00.0"
}


@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{
    "meta":{
        "code": "200",
        "name": "ОК"
    },
    "data": {
        "hospitalization_id": "123456",
        "external_id": "qwerty_012345",
        "measure_id": "7654321",
        "date_in": "2011-11-01",
        "date_out": "2011-11-11",
        "hospital": "hospital_code_012345",
        "doctor": "doctor_code_012345",
        "pregnancy_week": 25,
        "diagnosis_in": "Q00.0",
        "diagnosis_out": "Q00.0"
    }
}
"""

"""
@api {put} /risar/api/integration/<api_version>/card/<card_id>/measures/hospitalization/<hospitalization_id>/ Изменение госпитализации
@apiName PutHospitalization
@apiGroup Measures
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Изменение данных госпитализации.</br>
Валидация JSON Scheme: <a href="/json-data/measures/data/hospitalization-all-scheme.json">hospitalization-all-scheme.json</a>.<br/>
JSON пример: <a href="/json-data/measures/data/hospitalization-all-example.json">hospitalization-all-example.json</a>.<br/>
JSON пример успешный ответ: <a href="/json-data/measures/data/hospitalization-all-success-example.json">hospitalization-all-success-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} hospitalization_id Код госпитализации.
"""

"""
@api {delete} /risar/api/integration/<api_version>/card/<card_id>/measures/hospitalization/<hospitalization_id> Удаление госпитализации
@apiName DeleteHospitalization
@apiGroup Measures
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Удаление данных госпитализации.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} hospitalization_id Код госпитализации.
"""
