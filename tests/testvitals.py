class VitalsResource:
    def __init__(self):
        self.resources = [{
            "resourceType": "Observation",
            "id": "weight",
            "meta": {
                "profile": [
                    "http://fhir.org/guides/argonaut/StructureDefinition/argo-vitalsigns"
                ]
            },
            "text": {
                "status": "generated",
                "div": ""
            },
            "status": "final",
            "category": {
                "coding": [
                    {
                        "system": "http://hl7.org/fhir/observation-category",
                        "code": "vital-signs",
                        "display": "Vital Signs"
                    }
                ],
                "text": "Vital Signs"
            },
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "29463-7",
                        "display": "Body Weight"
                    }
                ],
                "text": "weight"
            },
            "subject": {
                "reference": "Patient/1",
                "display": "1"
            },
            "encounter": {
                "reference": "Encounter/"
            },
            "effectiveDateTime": "1999-07-02",
            "valueQuantity": {
                "value": 20.09414,
                "unit": "kg",
                "system": "http://unitsofmeasure.org",
                "code": "kg"
            }
        }, {
            "issued": "2018-01-01T21:39:08.000Z",
            "code": {
                "text": "O2 Source"
            },
            "effectiveDateTime": "2018-01-01T21:39:00.000Z",
            "status": "final",
            "encounter": {
                "reference": "Encounter/1"
            },
            "category": {
                "coding": [
                    {
                        "code": "vital-signs",
                        "display": "Vital Signs",
                        "system": "http://hl7.org/fhir/observation-category"
                    }
                ],
                "text": "Vital Signs"
            },
            "subject": {
                "reference": "Patient/1"
            },
            "meta": {
                "versionId": "1",
                "lastUpdated": "2018-01-01T21:41:08.000Z"
            },
            "resourceType": "Observation",
            "id": "1",
            "text": {
                "status": "generated",
                "div": ""
            },
            "valueCodeableConcept": {
                "text": "Room Air"
            }
        }]

    def get_resources(self):
        return self.resources
