import dagshub
dagshub.init(repo_owner='mh4070685', repo_name='MLOPS-Project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)