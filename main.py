from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI
import uvicorn


app = FastAPI()

data = {
    "email": "testuser@mail.co",
    "bio": "Test user",
}

data_with_age = {
    "email": "test@mail.co",
    "bio": None,
    "age": 29,
    # "gender": "male"
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=100)

    model_config = ConfigDict(extra='forbid')


class UserWithAgeSchema(UserSchema):
    age: int = Field(ge=0, le=125)


users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"success": True, "msg": "User has been added"}


@app.get("/users")
def get_users() -> list[UserSchema]:
    return users


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
