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
@apiDefine ObsSecondExaminationCreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного клиента.
@apiSuccessExample {json} Успешный ответ
{
  "meta":{
    "code": "200",
    "name": "ОК"
  },
  "data": {
    "exam_obs_id": "123456",
    "external_id": "qwerty_012345",
    "dynamic_monitoring": {
      "date": "2011-11-11",
      "hospital": "hospital_code_012345",
      "doctor": "doctor_code_012345",
      "ad_right_high": 120,
      "ad_left_high": 80,
      "ad_right_low": 80,
      "ad_left_low": 120,
      "weight": 70
    },
    "somatic_status": {
      "state": "udovletvoritel_noe",
      "complaints": ["oteki", "zrenie"]
    },
    "obstetric_status": {
      "uterus_state": "normal_nyjtonus"
    },
    "medical_report": {
      "pregnancy_week": 42,
      "next_visit_date": "2011-11-12",
      "pregnancy_continuation": true,
      "abortion_refusal": true,
      "diagnosis_osn": "Q00.0",
      "recommendations": "улыбаться",
      "notes": "мало улыбается"
    }
  }
}
"""

"""
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/checkup/ Описание ошибок и успешных ответов.
@apiName ObsSecondExamination
@apiGroup Obs-Second-Examination
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных.

@apiUse ObsSecondExaminationCreateSuccess
"""



"""
@api {post} /risar/api/integration/<api_version>/card/<card_id>/checkup/obs/second/ Регистрация повторных осмотров акушеров-гинекологов
@apiName PostObsSecondExamination
@apiGroup Obs-Second-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Регистрация данных повторного осмотра врача-акушера-гинеколога.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/checkup/data/secondcheckup-all-scheme.json">secondcheckup-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/checkup/data/secondcheckup-all-example.json">secondcheckup-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
"""

"""
@api {put} /risar/api/integration/<api_version>/card/<card_id>/checkup/obs/second/<exam_obs_id>/ Изменение повторных осмотров акушеров-гинекологов
@apiName PutObsSecondExamination
@apiGroup Obs-Second-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Изменение данных повторного осмотра врача-акушера-гинеколога.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/checkup/data/secondcheckup-all-scheme.json">secondcheckup-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/checkup/data/secondcheckup-all-example.json">secondcheckup-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} exam_obs_id Код повторного осмотра врача акушера-гинеколога.
"""

"""
@api {delete} /risar/api/integration/<api_version>/card/<card_id>/checkup/obs/second/<exam_obs_id>/ Удаление повторных осмотров акушеров-гинекологов
@apiName DeleteObsSecondExamination
@apiGroup Obs-Second-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Удаление данных повторного осмотра врача-акушера-гинеколога.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} exam_obs_id Код повторного осмотра врача акушера-гинеколога.
"""