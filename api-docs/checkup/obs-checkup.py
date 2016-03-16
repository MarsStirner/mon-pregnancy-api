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
@apiDefine CreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного клиента.
@apiSuccessExample {json} Успешный ответ
{
  "status":{
    "code": "200",
    "name": "ОК",
    "external_exam_obs_id": "123456"
    },
  "data": {
    //данные осмотра
  }
}
"""

"""
------------------------------------------------------------------------------------------
Current Errors.
------------------------------------------------------------------------------------------

@apiDefine CreateError
@apiVersion 0.1.0
@apiError (Error 5xx) {json} 500 исключительная ситуация, ошибка: внутренняя ошибка сервера
@apiError (Error 4xx) {json} 404 ошибка, запрашиваемый ресурс не найден

@apiErrorExample {json} Ошибка
{
  "meta": {
    "code": 406,
    "errors": [
      {
        "instance": {
          "insurance_document_series": "0944",
          "insurance_document_issuing_authority": "22001",
          "insurance_document_beg_date": "03-02-02",
          "insurance_document_number": "7837833"
        },
        "path": "insurance_documents/0",
        "error": "'insurance_document_type' is a required property"
      }
    ],
    "name": "Не валидные данные",
    "traceback": [

    ]
  },
  "result": null
}
"""

"""
@api {Result} /risar/api/integration/<api_version>/card/<external_system_id>/<external_card_id>/checkup/ Описание ошибок и успешных ответов.
@apiName ObsExamination
@apiGroup Obs-Examination
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных.

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {post} /risar/api/integration/<api_version>/card/<external_system_id>/<external_card_id>/checkup/obs/first/ Регистрация первичных осмотров акушеров-гинекологов
@apiName PostObsFirstExamination
@apiGroup Obs-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Регистрация данных первичного осмотра врача-акушера-гинеколога.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
"""

"""
@api {put} /risar/api/integration/<api_version>/card/<external_system_id>/<external_card_id>/checkup/obs/first/<external_exam_obs_id>/ Изменение первичных осмотров акушеров-гинекологов
@apiName PutObsFirstExamination
@apiGroup Obs-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Изменение данных первичного осмотра врача-акушера-гинеколога.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
@apiParam {String} external_exam_obs_id Код первичного осмотра врача-акушера-гинеколога во внешней учетной системе.
"""

"""
@api {delete} /risar/api/integration/<api_version>/card/<external_system_id>/<external_card_id>/checkup/obs/first/<external_exam_obs_id>/ Удаление первичных осмотров акушеров-гинекологов
@apiName DeleteObsFirstExamination
@apiGroup Obs-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Удаление данных первичного осмотра врача-акушера-гинеколога.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
@apiParam {String} external_exam_obs_id Код первичного осмотра врача-акушера-гинеколога во внешней учетной системе.
"""

############################## Second start ##############################

"""
@api {post} /risar/api/integration/<api_version>/card/<external_system_id>/<external_card_id>/checkup/obs/second/ Регистрация повторных осмотров акушеров-гинекологов
@apiName PostObsSecondExamination
@apiGroup Obs-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Регистрация данных повторного осмотра врача-акушера-гинеколога.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
"""

"""
@api {put} /risar/api/integration/<api_version>/card/<external_system_id>/<external_card_id>/checkup/obs/second/<external_exam_obs_id>/ Изменение повторных осмотров акушеров-гинекологов
@apiName PutObsSecondExamination
@apiGroup Obs-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Изменение данных повторного осмотра врача-акушера-гинеколога.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
@apiParam {String} external_exam_obs_id Код повторного осмотра врача-акушера-гинеколога во внешней учетной системе.
"""

"""
@api {delete} /risar/api/integration/<api_version>/card/<external_system_id>/<external_card_id>/checkup/obs/second/<external_exam_obs_id>/ Удаление повторных осмотров акушеров-гинекологов
@apiName DeleteObsSecondExamination
@apiGroup Obs-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Удаление данных повторного осмотра врача-акушера-гинеколога.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
@apiParam {String} external_exam_obs_id Код повторного осмотра врача-акушера-гинеколога во внешней учетной системе.
"""

############################## Second end ##############################


"""
@api {get} /risar/api/integration/<api_version>/card/<external_system_id>/<external_card_id>/checkup/obs/ Получение списка осмотров акушеров-гинекологов
@apiName GetObsExamination
@apiGroup Obs-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Получение списка первичных и повторных осмотров врача-акушера-гинеколога.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
"""
