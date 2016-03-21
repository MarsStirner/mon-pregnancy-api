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
@apiDefine GetListSuccess
@apiSuccess (Success 2xx) {json} 200 Список осмотров пациентки.
@apiSuccessExample {json} Успешный ответ
{
  "status":{
    "code": "200",
    "name": "ОК"
    },
  "data": {
  // ???
  }
}

"""

"""
------------------------------------------------------------------------------------------
Current Errors.
------------------------------------------------------------------------------------------
@apiDefine GetListError
@apiVersion 0.1.0
@apiError (Error 5xx) {json} 500 исключительная ситуация, ошибка: внутренняя ошибка сервера
@apiError (Error 4xx) {json} 404 ошибка, запрашиваемый ресурс не найден
"""

"""
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/checkup/ Описание ошибок и успешных ответов
@apiName Examination
@apiGroup Examination
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiUse GetListSuccess

@apiUse GetListError
"""


"""
@api {get} /risar/api/integration/<api_version>/card/<card_id>/checkup/ Получение списка осмотров беременной
@apiName GetExamination
@apiGroup Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Получение списка первичных и повторных осмотров врача акушера-гинеколога, специалиста ПЦ.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} external_system_id Код внешней системы.
@apiParam {String} external_card_id Код карты во внешней учетной системе.
"""
