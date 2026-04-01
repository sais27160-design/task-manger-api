from pydantic import BaseModel

class TaskResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    done: bool
    
    
# gcloud run deploy project-api --source . --region europe-southwest1 --allow-unauthenticated --add-cloudsql-instances project-3f3a8251-9f09-4e75-946:europe-southwest1:free-trial-first-project --set-env-vars DB_USER=Sai_Sai,DB_PASSWORD=saisai123,DB_NAME=tasks,CLOUD_SQL_CONNECTION_NAME=project-3f3a8251-9f09-4e75-946:europe-southwest1:free-trial-first-project