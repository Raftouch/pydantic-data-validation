from pydantic import BaseModel, Field, EmailStr, ConfigDict

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


print(repr(UserSchema(**data)))
print(repr(UserWithAgeSchema(**data_with_age)))
