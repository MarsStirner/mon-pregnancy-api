"""
@apiVersion 0.1.0
"""


"""
@api {Result} /risar/api/integration/<api_version>/organization Описание ошибок и успешных ответов
@apiName ErrorOrganization
@apiGroup rbOrganization
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiSuccess (Success 2xx) {json} 200 Данные организации
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
    "data": {
        "full_name": "Саратовский областной перинатальный центр",
        "short_name": "Саратовский ОПЦ",
        "infis_code": "16787",
        "address": "Саратов, Ленина 11",
        "area": "77123456789",
        "phone": "+7987200000",
        "LPU_id":"012345",
        "TFOMSCode": "036789",
        "Department_TFOMSCode":"54321",
        "INN": "036789",
        "KPP": "036789",
        "OGRN": "036789",
        "OKATO": "036789",
        "is_LPU": 1,
        "is_stationary": 0,
        "is_insurer" : 0
    }
}

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<api_version>/organization/<organization_id> Получение данных организации
@apiName GetOrganization
@apiGroup rbOrganization
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения данных организации из реестра организаций<br/>
Валидация JSON Schema <a href="/json-data/organization/data/organization-schema.json">organization-schema.json</a><br/>
JSON пример <a href="/json-data/organization/data/organization-success-example.json">organization-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} organization_id ТФОМС-Код организации
"""


"""
@api {post} /risar/api/integration/<api_version>/organization Регистрация организации
@apiName PostOrganization
@apiGroup rbOrganization
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных организации в реестре врачей<br/>
Валидация JSON Schema <a href="/json-data/organization/data/organization-schema.json">organization-schema.json</a><br/>
JSON пример <a href="/json-data/organization/data/organization-example.json">organization-example.json</a><br/>
JSON пример успешный ответ: <a href="/json-data/organization/data/organization-success-example.json">organization-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число

@apiParamExample {json} Request-Example:
{
    "full_name": "Саратовский областной перинатальный центр",
    "short_name": "Саратовский ОПЦ",
    "infis_code": "16787",
    "address": "Саратов, Ленина 11",
    "area": "77123456789",
    "phone": "+7987200000",
    "LPU_id":"012345",
    "TFOMSCode": "036789",
    "Department_TFOMSCode":"54321",
    "INN": "036789",
    "KPP": "036789",
    "OGRN": "036789",
    "OKATO": "036789",
    "is_LPU": 1,
    "is_stationary": 0,
    "is_insurer" : 0
}
"""


"""
@api {put} /risar/api/integration/<api_version>/organization/<organization_id> Изменение организации
@apiName PutOrganization
@apiGroup rbOrganization
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных организации<br/>
Валидация JSON Schema <a href="/json-data/organization/data/organization-schema.json">organization-schema.json</a><br/>
JSON пример <a href="/json-data/organization/data/organization-example.json">organization-example.json</a><br/>
JSON пример успешный ответ: <a href="/json-data/organization/data/organization-success-example.json">organization-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} organization_id ТФОМС-Код организации
"""


"""
@api {delete} /risar/api/integration/<api_version>/organization/<organization_id> Удаление организации
@apiName DeleteOrganization
@apiGroup rbOrganization
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных организации из реестра организаций

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} organization_id ТФОМС-Код организации
"""