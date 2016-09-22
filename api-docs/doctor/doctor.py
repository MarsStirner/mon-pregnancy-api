"""
@apiVersion 0.1.0
"""


"""
@api {Result} /risar/api/integration/<api_version>/doctor/ Описание ошибок и успешных ответов
@apiName ErrorDoctor
@apiGroup rbDoctor
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiSuccess (Success 2xx) {json} 200 Данные врача
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
    "data": {
        "last_name": "Цой",
        "first_name": "Иван",
        "patr_name": "Леонидович",
        "sex": 2,
        "birth_date": "1989-11-28",
        "SNILS": "036789",
        "INN": "036789",
        "organization": "134",
        "speciality": "233232",
        "post": "036789",
        "login": "036789",
        "regional_code": "036789"
    }
}

@apiUse CreateError
"""


"""
@api {get} /risar/api/integration/<api_version>/doctor/<organization_code>/<doctor_code> Получение данных врача
@apiName GetDoctor
@apiGroup rbDoctor
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения данных врача из реестра сотрудников ЛПУ<br/>
Валидация JSON Schema <a href="/json-data/doctor/data/doctor-schema.json">doctor-schema.json</a><br/>
JSON пример успешный ответ: <a href="/json-data/doctor/data/doctor-success-example.json">doctor-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} organization_code ТФОМС-Код организации
@apiParam {Int} doctor_code Региональный код врача
"""


"""
@api {post} /risar/api/integration/<api_version>/doctor/ Регистрация врача
@apiName PostDoctor
@apiGroup rbDoctor
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных врача в реестре врачей<br/>
Валидация JSON Schema <a href="/json-data/doctor/data/doctor-schema.json">doctor-schema.json</a><br/>
JSON пример <a href="/json-data/doctor/data/doctor-example.json">doctor-example.json</a><br/>
JSON пример успешный ответ: <a href="/json-data/doctor/data/doctor-success-example.json">doctor-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число

@apiParamExample {json} Request-Example:
{
    "last_name": "Цой",
    "first_name": "Иван",
    "patr_name": "Леонидович",
    "sex": 2,
    "birth_date": "1989-11-28",
    "SNILS": "036789",
    "INN": "036789",
    "organization": "134",
    "speciality": "233232",
    "post": "036789",
    "login": "036789",
    "regional_code": "036789"
}
"""


"""
@api {put} /risar/api/integration/<api_version>/doctor/<organization_code>/<doctor_code> Изменение врача
@apiName PutDoctor
@apiGroup rbDoctor
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных врача<br/>
Валидация JSON Schema <a href="/json-data/doctor/data/doctor-schema.json">doctor-schema.json</a><br/>
JSON пример <a href="/json-data/doctor/data/doctor-example.json">doctor-example.json</a><br/>
JSON пример успешный ответ: <a href="/json-data/doctor/data/doctor-success-example.json">doctor-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} organization_code ТФОМС-Код организации
@apiParam {Int} doctor_code Региональный код врача
"""


"""
@api {delete} /risar/api/integration/<api_version>/doctor/<organization_code>/<doctor_code> Удаление врача
@apiName DeleteDoctor
@apiGroup rbDoctor
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных врача из реестра врачей

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} organization_code ТФОМС-Код организации
@apiParam {Int} doctor_code Региональный код врача
"""