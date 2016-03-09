'use strict';

let tv4 = require('tv4');

tv4.addSchema("/api-docs/examination/general", {
    "type": "object",
        "$schema": "http://json-schema.org/draft-04/schema",
        "id": "/api-docs/examination",
        "properties": {
        "date": {
            "type": "string",
            "id": "/api-docs/examination/general/date",
            "description": "Дата осмотра"
        },
        "growth": {
            "type": "number",
                "id": "/api-docs/examination/general/growth",
                "description": "Рост пациентки"
        },
        "weight": {
            "type": "number",
                "id": "/api-docs/examination/general/weight",
                "description": "Масса пациентки на осмотре"
        },
        "body_mass_index": {
            "type": "number",
                "id": "/api-docs/examination/general/body_mass_index",
                "description": "Индекс массы тела"
        },
        "WGR": {
            "type": "integer",
                "id": "/api-docs/examination/general/WGR",
                "description": "Массо-ростовой коэффициент (МРК)"
        }
    },
    "required": [
        "date",
        "growth",
        "weight"
    ]
});

var schema = {
    "type": "object",
    "$schema": "http://json-schema.org/draft-04/schema",
    "id": "/api-docs/examination",
    "properties": {
        "general": {
            "$ref": "/api-docs/examination/general",
            "id": "/api-docs/examination/general",
            "description": "Общие атрибуты осмотра"
        }
    }
};

var data1 = {
    "general": {
        "date": "12.02.2015",
        "growth": 170,
        "weight": 56,
        "body_mass_index": 19.4,
        "WGR": 33
    }
};

console.log("data 1: " + tv4.validate(data1, schema));
console.log("data 1: " + tv4.missing);
console.log("data 2 error: " + JSON.stringify(tv4.error, null, 4));