import os
from src.turn_alerts.alerts import AlertAPI # type: ignore

from src.turn_alerts.schemas.create_alerts import CreateAlertPayload # type: ignore
from src.turn_alerts.schemas.types import AlertTypeEnum, ObjectTypeEnum # type: ignore

token = os.environ.get("TOKEN")
host = os.environ.get("HOST")
if not (host and token):
    raise Exception("No host or token set")
alert = AlertAPI(token=token, host=host)

alert_data: CreateAlertPayload = {
    "title": "Testing alert",
    "body": "Prueba de alerta",
    "type": AlertTypeEnum.IMPORT_START_PROCESSING,
    "object": {
        "object_type": ObjectTypeEnum.advise_job,
        "id": "b34eba69-f1cd-49ec-813a-b88a268198f5",
    },
    "partner_id": 1,
    "team_member_id": 1,
    "tags": [],
}

response_alert = alert.create(alert_data)
print(response_alert)
