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
@apiDefine DefectCreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного дефектуры.
@apiSuccessExample {json} Успешный ответ
{
    "meta":{
        "code": "200",
        "name": "ОК"
    },
    "data": {
        "defect_id": "123456",
        "external_id": "qwerty_012345",
        "referral_hospital": "hospital_code_012345",
        "referral_doctor": "doctor_code_012345",
        "referral_date": "2011-11-11",
        "delivered": "транспортом",
        "diagnosis_referral": "Q00.0",
        "diagnosis_opc": "Q00.0",
        "defect_organize": "бизнес-процессы приуныли",
        "recommend_organize": "не унывать",
        "hospital": "hospital_code_54321",
        "doctor": "doctor_code_54321",
        "doctor_department_chief": "doctor_code_54322",
        "doctor_chief_deputy": "doctor_code_54323"
    }
}
"""

"""
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/defect/ Описание ошибок и успешных ответов.
@apiName Defect
@apiGroup Defect
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiUse DefectCreateSuccess

@apiUse CreateError
"""

"""
@api {post} /risar/api/integration/<api_version>/card/<card_id>/defect/ Регистрация дефектуры
@apiName PostDefect
@apiGroup Defect
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Регистрация данных дефектуры.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/defect/data/defect-all-scheme.json">defect-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/defect/data/defect-all-example.json">defect-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
"""

"""
@api {put} /risar/api/integration/<api_version>/card/<card_id>/defect/<defect_id>/ Изменение дефектуры
@apiName PutDefect
@apiGroup Defect
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Изменение данных дефектуры.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/defect/data/defect-all-scheme.json">defect-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/defect/data/defect-all-example.json">defect-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} defect_id Код дефектуры.
"""

"""
@api {delete} /risar/api/integration/<api_version>/card/<card_id>/defect/<defect_id> Удаление дефектуры
@apiName DeleteDefect
@apiGroup Defect
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Удаление данных дефектуры.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} defect_id Код дефектуры.
"""
