from __future__ import absolute_import
from celery.schedules import crontab

broker_url = f'redis://127.0.0.1:6379/3'
accept_content = ['json']
# 时区设置
timezone = 'Asia/Shanghai'
# celery默认开启自己的日志
# False表示不关闭
worker_hijack_root_logger = False
# 存储结果过期时间，过期后自动删除
# 单位为秒
result_expires = 60 * 60 * 24 * 10

# 设置默认不存结果
# task_ignore_result = True
# 使用celery event机制，监听task执行成功时会发出的 task-succeeded 事件。
task_send_sent_event = False  # 如果启用，将为每个任务发送一个任务发送事件，这样就可以在任务被工作者消耗之前对其进行跟踪。

# 解决  max number of clients reached
broker_pool_limit = 100
redis_max_connections = 1000

# Add tasks here
imports = (
    'tasks',
)

# beat_schedule = {
#     'sub': {
#         'task': 'tasks.sub',
#         # 'schedule': timedelta(seconds=3),
#         # 每周一早八点
#         # 'schedule': crontab(hour=8, day_of_week=1),
#         'args': (300, 150),
#     }
# }
