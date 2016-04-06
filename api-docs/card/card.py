"""
@apiVersion 0.1.0
"""

"""
------------------------------------------------------------------------------------------
Current Success.
------------------------------------------------------------------------------------------
@apiDefine CreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного клиента.
@apiSuccessExample {json} Успешный ответ
{}
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
    "code": 400,
    "errors": [
      {
      }
    ],
    "name": "Невалидные данные",
    "traceback": [

    ]
  },
  "result": null
}
"""

"""
@api {get} /risar/api/integration/<int:api_version>/card/schema.json json-schema
@apiName CardSchema
@apiGroup Card
@apiVersion 0.1.0
@apiDescription Получение данных json-schema по медицинской карте

@apiParam {Number} api_version Версия API, целое положительной число

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {post} /risar/api/integration/<int:api_version>/card/ Регистрация медицинской карты
@apiName PostCard
@apiGroup Card
@apiVersion 0.1.0
@apiDescription Метод предназначен для регистрации медицинской карты и постановки на учет

@apiParam {Number} api_version Версия API, целое положительной число

@apiUse CreateSuccess

@apiUse CreateError

"""

"""
@api {put} /risar/api/integration/<int:api_version>/card/<card_id> Изменение медицинской карты
@apiName PutCard
@apiGroup Card
@apiVersion 0.1.0
@apiDescription Метод предназначен для изменения данных медицинской карты

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} card_id Код карты в системе БАРС.МР

@apiUse CreateSuccess

@apiUse CreateError
"""

"""
@api {delete} /risar/api/integration/<int:api_version>/card/<card_id> Удаление медицинской карты
@apiName DeleteCard
@apiGroup Card
@apiVersion 0.1.0
@apiDescription Метод asd sa предназначен для удаления данных медицинской карты.

@apiParam {Number} api_version Версия API от целое положительной число.
@apiParam {String} card_id Код карты в системе БАРС.МР

@apiUse CreateSuccess

@apiUse CreateError
"""