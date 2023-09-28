from google.cloud import tasks_v2
from google.protobuf import timestamp_pb2


def weather_task():
    client = tasks_v2.CloudTasksClient()
    parent = client.queue_path("project-id", "location", "queue-name")

    task = {
        "app_engine_http_request": {
            "http_method": tasks_v2.HttpMethod.POST,
            "relative_uri": "/fetch-weather-data",
        },
        "schedule_time": timestamp_pb2.Timestamp(seconds=300),  # 5 min for example
    }

    response = client.create_task(parent=parent, task=task)
