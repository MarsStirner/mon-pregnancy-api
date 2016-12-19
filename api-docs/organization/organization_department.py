"""
@apiVersion 0.1.0
"""


"""
@api {Result} /risar/api/integration/<api_version>/organization_department Описание ошибок и успешных ответов
@apiName ErrorOrganizationDepartment
@apiGroup rbOrganizationDepartment
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiSuccess (Success 2xx) {json} 200 Данные подразделения
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
    "data": {
        "organisation_id": "organisation_code_123",
        "regionalCode": "department_code_123",
        "TFOMSCode": "123456",
        "name": "Подразделение ЛПУ",
        "address": "г.Москва, ул.Пушкина, д.1"
    }
}

@apiUse CreateError
"""


"""
@api {post} /risar/api/integration/<api_version>/organization_department Регистрация подразделения
@apiName PostOrganizationDepartment
@apiGroup rbOrganizationDepartment
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации подразделения<br/>
Валидация JSON Schema <a href="/json-data/organization/data/organization_department-schema.json">organization_department-schema.json</a><br/>
JSON пример <a href="/json-data/organization/data/organization_department-example.json">organization_department-example.json</a><br/>
JSON пример успешный ответ: <a href="/json-data/organization/data/organization_department-success-example.json">organization_department-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число

@apiParamExample {json} Request-Example:
{
    "organisation_id": "organisation_code_123",
    "regionalCode": "department_code_123",
    "TFOMSCode": "123456",
    "name": "Подразделение ЛПУ",
    "address": "г.Москва, ул.Пушкина, д.1"
}
"""


"""
@api {put} /risar/api/integration/<api_version>/organization_department/<department_id> Изменение подразделения
@apiName PutOrganizationDepartment
@apiGroup rbOrganizationDepartment
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных подразделения<br/>
Валидация JSON Schema <a href="/json-data/organization/data/organization_department-schema.json">organization_department-schema.json</a><br/>
JSON пример <a href="/json-data/organization/data/organization_department-example.json">organization_department-example.json</a><br/>
JSON пример успешный ответ: <a href="/json-data/organization/data/organization_department-success-example.json">organization_department-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} department_id Идентификатор подразделения
"""


"""
@api {delete} /risar/api/integration/<api_version>/organization_department/<department_id> Удаление подразделения
@apiName DeleteOrganizationDepartment
@apiGroup rbOrganizationDepartment
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных подразделения

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} department_id Идентификатор подразделения
"""