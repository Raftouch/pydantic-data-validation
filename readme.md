#### Create a virtual environment

```bash
python -m venv venv
```

#### Activate it

Windows

```bash
venv\Scripts\activate
```

MacOS / Linux

```bash
source venv/bin/activate
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Start project

```bash
python main.py
```

#### Check data in terminal

```bash
print(repr(UserSchema(**data)))
```
