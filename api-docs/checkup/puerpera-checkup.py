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
@apiDefine PuerperaExaminationCreateSuccess
@apiSuccess (Success 2xx) {json} 200 Данные сохраненного осмотра.
@apiSuccessExample {json} Успешный ответ
{
  "meta":{
    "code": "200",
    "name": "ОК"
  },
  "data": {
    "exam_puerpera_id": "123456",
    "date": "2011-11-12",
    "time": "18:00",
    "date_of_childbirth": "2011-11-11",
    "hospital": "ЛПУ",
    "doctor": "Иванов И.И.",
    "time_since_childbirth": 1,
    "state": "srednejtajesti",
    "ad_right_high": 120,
    "ad_left_high": 120,
    "ad_right_low": 80,
    "ad_left_low": 80,
    "veins": "noma",
    "diagnosis": "Q00.0",
    "contraception_recommendations": "01",
    "recommendations": "апельсиновый сок 3 р.д. натощак"
  }
}
"""

"""
@api {Result} /risar/api/integration/<api_version>/card/<card_id>/checkup/ Описание ошибок и успешных ответов.
@apiName PuerPeraExamination
@apiGroup PuerPera-Examination
@apiVersion 0.1.0
@apiDescription Описание ошибок и успешных ответов.

@apiUse PuerperaExaminationCreateSuccess
"""

"""
@api {post} /risar/api/integration/<api_version>/card/<card_id>/checkup/puerpera/ Регистрация осмотров родильницы
@apiName PostPuerPeraExamination
@apiGroup PuerPera-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Регистрация данных осмотра родильницы.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/checkup/data/puerperacheckup-all-scheme.json">puerperacheckup-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/checkup/data/puerperacheckup-all-example.json">puerperacheckup-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
"""

"""
@api {put} /risar/api/integration/<api_version>/card/<card_id>/checkup/puerpera/<exam_puerpera_id>/ Изменение осмотров родильницы
@apiName PutPuerPeraExamination
@apiGroup PuerPera-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Изменение данных осмотра родильницы.</br>
Валидация JSON Scheme: <a href="/mon-pregnancy-api/api-docs/checkup/data/puerperacheckup-all-scheme.json">puerperacheckup-all-scheme.json</a>.<br/>
JSON пример: <a href="/mon-pregnancy-api/api-docs/checkup/data/puerperacheckup-all-example.json">puerperacheckup-all-example.json</a>.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} exam_puerpera_id Код осмотра родильницы.
"""

"""
@api {delete} /risar/api/integration/<api_version>/card/<card_id>/checkup/puerpera/<exam_puerpera_id> Удаление осмотров родильницы
@apiName DeletePuerPeraExamination
@apiGroup PuerPera-Examination
@apiVersion 0.1.0
@apiPermission auth
@apiDescription Удаление данных осмотра родильницы.

@apiParam {Number} api_version Версия API, целое положительной число
@apiParam {Int} card_id Код карты пациента.
@apiParam {Int} exam_puerpera_id Код осмотра родильницы.
"""
