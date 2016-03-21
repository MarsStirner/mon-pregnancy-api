"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine EpicrisisCreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{
  "status":{
    "code": "200",
    "name": "ОК"
  },
  "data": {
    "general_info": {
      "admission_date": "2011-11-11",
      "pregnancy_duration": 42,
      "delivery_date": "2011-11-11",
      "delivery_time": "18:00",
      "maternity_hospital": "",
      "diagnosis_osn": "Q11.1",
      "diagnosis_sop": [
        "Q00.0", "Q00.1"
      ],
      "diagnosis_osl": [
        "Q11.1"
      ],
      "pregnancy_speciality": "Нормальненько",
      "postnatal_speciality": "Нормальненько",
      "help": "Консультация",
      "pregnancy_final": "rodami",
      "maternity_hospital_doctor": "",
      "curation_hospital": ""
    },
    "mother_death": {
      "death": false
    },
    "complications": {
      "delivery_waters": "rannie",
      "weakness": "pervicnaa",
      "meconium_color": false,
      "pathological_preliminary_period": false,
      "abnormalities_of_labor": false,
      "chorioamnionitis": false,
      "perineal_tear": "0",
      "eclampsia": "net",
      "afterbirth": "plencataaplazenta",
      "anemia": "",
      "infections_during_delivery": "",
      "infections_after_delivery": ""
    },
    "manipulations": {
      "caul": false,
      "calfbed": false,
      "perineotomy": "",
      "secundines": false,
      "other_manipulations": ""
    },
    "operations": {
      "obstetrical_forceps": "vyhodnye",
      "vacuum_extraction": false,
      "indication": "kombinirovannye",
      "specialities": "planovoe",
      "anesthetization": "01",
      "hysterectomy": "boleedvuhsutokposlerodov",
      "complications": [
        "Q33.3"
      ],
      "embryotomy": false
    },
    "kids": [
      {
        "alive": true,
        "sex": 1,
        "weight": 3000,
        "length": 50,
        "date": "2001-11-11",
        "maturity_rate": "donosennyj",
        "apgar_score_1": 0,
        "apgar_score_5": 0,
        "apgar_score_10": 0,
        "death_date": "0000-00-00",
        "death_time": "00:00",
        "death_reason": ""
      }
    ],
    "epicrisis": {
      "hospital_chief_doctor": "",
      "hospital_doctor": "",
      "date_close": "2011-11-11"
    }
  }
}
"""


"""
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/checkup/ Описание ошибок и успешных ответов.
@apiName Epicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiUse EpicrisisCreateSuccess

@apiUse CreateError
"""


"""
@api {post} /risar/api/integration/<int:api_version>/card/<card_id>/epicrisis/ Регистрация эпикриза
@apiName PostEpicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных эпикриза случая беременности.<br/>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/epicrisis/data/epicrisis-all-scheme.json">epicrisis-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/epicrisis/data/epicrisis-all-example.json">epicrisis-all-example.json</a>.


@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты пациента во внешней учетной системе.

@apiParamExample {json} Request-Example:
{
  "general_info": {
    "admission_date": "2011-11-11",
    "pregnancy_duration": 42,
    "delivery_date": "2011-11-11",
    "delivery_time": "18:00",
    "maternity_hospital": "",
    "diagnosis_osn": "Q11.1",
    "diagnosis_sop": [
      "Q00.0", "Q00.1"
    ],
    "diagnosis_osl": [
      "Q11.1"
    ],
    "pregnancy_speciality": "Нормальненько",
    "postnatal_speciality": "Нормальненько",
    "help": "Консультация",
    "pregnancy_final": "rodami",
    "maternity_hospital_doctor": "",
    "curation_hospital": ""
  },
  "mother_death": {
    "death": false
  },
  "complications": {
    "delivery_waters": "rannie",
    "weakness": "pervicnaa",
    "meconium_color": false,
    "pathological_preliminary_period": false,
    "abnormalities_of_labor": false,
    "chorioamnionitis": false,
    "perineal_tear": "0",
    "eclampsia": "net",
    "afterbirth": "plencataaplazenta",
    "anemia": "",
    "infections_during_delivery": "",
    "infections_after_delivery": ""
  },
  "manipulations": {
    "caul": false,
    "calfbed": false,
    "perineotomy": "",
    "secundines": false,
    "other_manipulations": ""
  },
  "operations": {
    "obstetrical_forceps": "vyhodnye",
    "vacuum_extraction": false,
    "indication": "kombinirovannye",
    "specialities": "planovoe",
    "anesthetization": "01",
    "hysterectomy": "boleedvuhsutokposlerodov",
    "complications": [
      "Q33.3"
    ],
    "embryotomy": false
  },
  "kids": [
    {
      "alive": true,
      "sex": 1,
      "weight": 3000,
      "length": 50,
      "date": "2001-11-11",
      "maturity_rate": "donosennyj",
      "apgar_score_1": 0,
      "apgar_score_5": 0,
      "apgar_score_10": 0,
      "death_date": "0000-00-00",
      "death_time": "00:00",
      "death_reason": ""
    }
  ],
  "epicrisis": {
    "hospital_chief_doctor": "",
    "hospital_doctor": "",
    "date_close": "2011-11-11"
  }
}
"""


"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id>/epicrisis/ Изменение эпикриза
@apiName PutEpicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных эпикриза случая беременности.<br/>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/epicrisis/data/epicrisis-all-scheme.json">epicrisis-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/epicrisis/data/epicrisis-all-example.json">epicrisis-all-example.json</a>.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<card_id>/epicrisis/ Удаление эпикриза
@apiName DeleteEpicrisis
@apiGroup Epicrisis
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных данных эпикриза случая беременности.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе
"""