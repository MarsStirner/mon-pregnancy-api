"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine ChildbirthCreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сущности.
@apiSuccessExample {json} Успешный ответ
{
  "meta":{
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
      "perineal_tear": "01",
      "eclampsia": "net",
      "afterbirth": "plencataaplazenta",
      "anemia": false,
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
        "time": "18:00",
        "maturity_rate": "donosennyj",
        "apgar_score_1": 0,
        "apgar_score_5": 0,
        "apgar_score_10": 0,
        "death_date": "0000-00-00",
        "death_time": "00:00",
        "death_reason": ""
      }
    ]
  }
}
"""


"""
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/childbirth/ Описание ошибок и успешных ответов.
@apiName Childbirth
@apiGroup Childbirth
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiUse ChildbirthCreateSuccess

@apiUse CreateError
"""


"""
@api {post} /risar/api/integration/<int:api_version>/card/<card_id>/childbirth/ Регистрация данных родоразрешения
@apiName PostChildbirth
@apiGroup Childbirth
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации данных родоразрешения случая беременности.<br/>
Валидация JSON Scheme: <a href="/json-data/epicrisis/data/childbirth-all-scheme.json">childbirth-all-scheme.json</a>.<br/>
JSON пример: <a href="/json-data/epicrisis/data/childbirth-all-example.json">childbirth-all-example.json</a>.


@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.

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
    "perineal_tear": "01",
    "eclampsia": "net",
    "afterbirth": "plencataaplazenta",
    "anemia": false,
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
      "time": "18:00",
      "maturity_rate": "donosennyj",
      "apgar_score_1": 0,
      "apgar_score_5": 0,
      "apgar_score_10": 0,
      "death_date": "0000-00-00",
      "death_time": "00:00",
      "death_reason": ""
    }
  ],
  "childbirth": {
    "hospital_chief_doctor": "",
    "hospital_doctor": "",
    "date_close": "2011-11-11"
  }
}
"""


"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id>/childbirth/ Изменение данных родоразрешения
@apiName PutChildbirth
@apiGroup Childbirth
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных родоразрешения случая беременности.<br/>
Валидация JSON Scheme: <a href="/json-data/epicrisis/data/childbirth-all-scheme.json">childbirth-all-scheme.json</a>.<br/>
JSON пример: <a href="/json-data/epicrisis/data/childbirth-all-example.json">childbirth-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<card_id>/childbirth/ Удаление данных родоразрешения
@apiName DeleteChildbirth
@apiGroup Childbirth
@apiVersion 0.1.0
@apiDescription Метод предназначен для удаления данных родоразрешения случая беременности.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
"""