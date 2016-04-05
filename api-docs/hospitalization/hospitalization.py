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
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/hospitalization/ Описание ошибок и успешных ответов.
@apiName Hospitalization
@apiGroup Hospitalization
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiUse HospitalizationCreateSuccess

@apiUse CreateError
"""

"""
@api {post} /risar/api/integration/<api_version>/card/<card_id>/hospitalization/ Регистрация госпитализации
@apiName PostHospitalization
@apiGroup Hospitalization
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Регистрация данных госпитализации.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/hospitalization/data/hospitalization-all-scheme.json">hospitalization-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/hospitalization/data/hospitalization-all-example.json">hospitalization-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
"""

"""
@api {put} /risar/api/integration/<api_version>/card/<card_id>/hospitalization/<hospitalization_id>/ Изменение госпитализации
@apiName PutHospitalization
@apiGroup Hospitalization
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Изменение данных госпитализации.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/hospitalization/data/hospitalization-all-scheme.json">hospitalization-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/hospitalization/data/hospitalization-all-example.json">hospitalization-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} hospitalization_id Код госпитализации.
"""

"""
@api {delete} /risar/api/integration/<api_version>/card/<card_id>/hospitalization/<hospitalization_id> Удаление госпитализации
@apiName DeleteHospitalization
@apiGroup Hospitalization
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Удаление данных госпитализации.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} hospitalization_id Код госпитализации.
"""
