"""
@apiVersion 0.1.0
"""


"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine Ticket25Success
@apiSuccess (Success 2xx) {json} 200 Данные талона посещения
@apiSuccessExample {json} Успешный ответ
{
    "meta": {
        "code": "200",
        "name": "OK"
    },
    "data":{
        "hospital": "hospital_code_012345",
        "date_open": "2011-11-11",
        "date_close": "2011-11-11",
        "medical_care": "1",
        "finished_treatment": "1",
        "initial_treatment": "1",
        "treatment_result": "1",
        "payment": "1",
        "preliminary_diagnosis": "Q00.0",
        "medical_services": [
            "medical_service_code_012345"
        ],
        "diagnosis": "Q00.0",
        "disease_character": "1",
        "sick_leave": [{
            "sick_leave_type": "1",
            "sick_leave_reason": "1",
            "sick_leave_date_open": "2011-11-11",
            "sick_leave_date_close": "2011-11-11"
        }],
        "doctor": "doctor_code_012345"
    }
}

"""

"""
@api {get} /risar/api/integration/<api_version>/card/<card_id>/checkup/obs/first/<exam_obs_id>/ticket25 Получение данных талона посещения
@apiName GetObsFirstExaminationTicket25
@apiGroup Obs-First-Examination
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения данных талона посещения<br/>
Валидация JSON Schema <a href="/json-data/ticket25/data/ticket25-schema.json">ticket25-schema.json</a><br/>
JSON пример <a href="/json-data/ticket25/data/ticket25-success-example.json">ticket25-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} exam_obs_id Код первичного осмотра врача акушера-гинеколога

@apiUse Ticket25Success
"""


"""
@api {get} /risar/api/integration/<api_version>/card/<card_id>/checkup/obs/second/<exam_obs_id>/ticket25 Получение данных талона посещения
@apiName GetObsSecondExaminationTicket25
@apiGroup Obs-Second-Examination
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения данных талона посещения<br/>
Валидация JSON Schema <a href="/json-data/ticket25/data/ticket25-schema.json">ticket25-schema.json</a><br/>
JSON пример <a href="/json-data/ticket25/data/ticket25-success-example.json">ticket25-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} exam_obs_id Код повторного осмотра врача акушера-гинеколога

@apiUse Ticket25Success
"""

"""
@api {get} /risar/api/integration/<api_version>/card/<card_id>/checkup/pc/<exam_pc_id>/ticket25 Получение данных талона посещения
@apiName GetPCExaminationTicket25
@apiGroup PC-Examination
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения данных талона посещения<br/>
Валидация JSON Schema <a href="/json-data/ticket25/data/ticket25-schema.json">ticket25-schema.json</a><br/>
JSON пример <a href="/json-data/ticket25/data/ticket25-success-example.json">ticket25-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} exam_pc_id Код осмотра специалиста перинатального центра

@apiUse Ticket25Success
"""

"""
@api {get} /risar/api/integration/<api_version>/card/<card_id>/checkup/puerpera/<exam_puerpera_id>/ticket25 Получение данных талона посещения
@apiName GetPuerperaExaminationTicket25
@apiGroup PuerPera-Examination
@apiVersion 0.1.0
@apiDescription Метод предназначен для получения данных талона посещения<br/>
Валидация JSON Schema <a href="/json-data/ticket25/data/ticket25-schema.json">ticket25-schema.json</a><br/>
JSON пример <a href="/json-data/ticket25/data/ticket25-success-example.json">ticket25-success-example.json</a>

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} exam_puerpera_id Код осмотра родильницы

@apiUse Ticket25Success
"""


