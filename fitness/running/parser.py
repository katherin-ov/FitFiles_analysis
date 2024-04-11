from typing import Any
from filehash import FileHash

import fitdecode

from running.models import Result, UploadFiles


def get_dataframes(fname: str) -> dict[str, Any | None]:
    workout_type = None
    average_heart_rate = None
    distance = None
    average_speed = None
    calories = None
    with fitdecode.FitReader(fname) as fit_file:
        for frame in fit_file:
            if isinstance(frame, fitdecode.records.FitDataMessage):
                if frame.name == 'lap':
                    for field in frame:
                        if field.name == 'sport':
                            workout_type = field.value
                        elif field.name == 'total_calories':
                            calories = field.value
                        elif field.name == 'avg_heart_rate':
                            average_heart_rate = field.value
                        elif field.name == 'total_distance':
                            distance = field.value
                        elif field.name == 'timestamp':
                            timestamp = field.value
                if frame.name == 'session':
                    for field in frame.fields:
                        if field.name == 'avg_speed':
                            average_speed = field.value

    return {
        'workout_type': workout_type,
        'average_heart_rate': average_heart_rate,
        'distance': distance,
        'average_speed': average_speed,
        'total_calories': calories,
        'timestamp': timestamp,
    }


def parse(fname):
    md5hasher = FileHash('md5')
    file_name = "media/"+str(fname)
    file_hash = md5hasher.hash_file(file_name)
    q = Result.objects.filter(file_hash=file_hash)
    if q.values('file_hash'):
        pass
    else:
        fit_data = get_dataframes(fname)
        upload_file_obj = UploadFiles.objects.create(file=fname)
        Result.objects.create(
            fit_file=upload_file_obj,
            sport=fit_data['workout_type'],
            avg_speed=fit_data['average_speed'],
            total_calories=fit_data['total_calories'],
            distance=fit_data['distance'],
            avg_heart_rate=fit_data['average_heart_rate'],
            timestamp=fit_data['timestamp'],
            file_hash=file_hash
        )
    return file_hash
