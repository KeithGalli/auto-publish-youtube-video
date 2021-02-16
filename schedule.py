import boto3

def get_schedule_speed(subscribers):
    schedule_speed = check_schedule_expression()
    subscribers_remaining = 1000 - subscribers 
    if subscribers_remaining < 25:
        schedule_speed = "rate(5 minutes)"
    elif subscribers_remaining < 200:
        schedule_speed = "rate(30 minutes)"
    elif subscribers_remaining < 400:
        schedule_speed = "rate(2 hours)"
    return schedule_speed
    
def check_schedule_expression():
    client = boto3.client('events')
    response = client.list_rules()
    schedule = response['Rules'][0]['ScheduleExpression']
    return schedule
    
def update_schedule_expression(subscribers):
    schedule_speed = get_schedule_speed(subscribers)
    client = boto3.client('events')
    response = client.put_rule(
        Name='publish-video-rule',
        ScheduleExpression=schedule_speed,
    )
    return response
    
def turn_off_function():
    client = boto3.client('events')
    response = client.put_rule(
        Name='publish-video-rule',
        ScheduleExpression=check_schedule_expression(),
        State='DISABLED',
    )
    return response