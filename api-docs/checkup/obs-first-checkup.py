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
@apiDefine ObsFirstExaminationCreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного клиента.
@apiSuccessExample {json} Успешный ответ
{
  "meta":{
    "code": "200",
    "name": "ОК"
  },
  "data": {
    "exam_obs_id": "123456",
    "general_info": {
      "date": "2011-11-11",
      "time": "18:00",
      "doctor": "Иванов И.И.",
      "height": 175,
      "weight": 70
    },
    "somatic_status": {
      "state": "udovletvoritel_noe",
      "subcutaneous_fat": "izbytocnorazvita",
      "tongue": "01",
      "complaints": "oteki",
      "skin": "suhaa",
      "lymph": "boleznennye",
      "breast": "nagrubanie",
      "heart_tones": "akzentIItona",
      "pulse": "defizitpul_sa",
      "nipples": "norma",
      "mouth": "sanirovana",
      "respiratory": "hripyotsutstvuut",
      "abdomen": "jivotnaprajennyj",
      "liver": "nepal_piruetsa",
      "urinoexcretory": "СindromПasternazkogo",
      "ad_right_high": 120,
      "ad_left_high": 120,
      "ad_right_low": 80,
      "ad_left_low": 80,
      "veins": "noma",
      "heart_rate": 80
    },
    "obstetric_status": {
      "uterus_state": "normal_nyjtonus",
      "dssp": 1,
      "dscr": 1,
      "dstr": 1,
      "cext": 1,
      "soloviev_index": 1
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
@apiName ObsFirstExamination
@apiGroup Obs-First-Examination
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных.

@apiUse ObsFirstExaminationCreateSuccess
"""

"""
@api {post} /risar/api/integration/<api_version>/card/<card_id>/checkup/obs/first/ Регистрация первичных осмотров акушеров-гинекологов
@apiName PostObsFirstExamination
@apiGroup Obs-First-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Регистрация данных первичного осмотра врача-акушера-гинеколога.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/firstcheckout/data/firstcheckout-all-scheme.json">firstcheckout-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/firstcheckout/data/firstcheckout-all-example.json">firstcheckout-all-example.json</a>.


@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
"""

"""
@api {put} /risar/api/integration/<api_version>/card/<card_id>/checkup/obs/first/<exam_obs_id>/ Изменение первичных осмотров акушеров-гинекологов
@apiName PutObsFirstExamination
@apiGroup Obs-First-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Изменение данных первичного осмотра врача-акушера-гинеколога.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/firstcheckout/data/firstcheckout-all-scheme.json">firstcheckout-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/firstcheckout/data/firstcheckout-all-example.json">firstcheckout-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} exam_obs_id Код первичного осмотра врача акушера-гинеколога.
"""

"""
@api {delete} /risar/api/integration/<api_version>/card/<card_id>/checkup/obs/first/<exam_obs_id>/ Удаление первичных осмотров акушеров-гинекологов
@apiName DeleteObsFirstExamination
@apiGroup Obs-First-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Удаление данных первичного осмотра врача-акушера-гинеколога.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} exam_obs_id Код первичного осмотра врача акушера-гинеколога.
"""