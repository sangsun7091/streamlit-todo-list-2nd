# from dataclasses import dataclass
#
# @dataclass
# class Task:
#     name: str
#     is_done: bool = False

## change for idx -> task_ID '26.0911

import uuid

class Task:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())  # 고유 식별자 부여
        self.name = name
        self.is_done = False
        