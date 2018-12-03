# Wolfram Alpha Short Answers as a microservice

## Installation and Build
```

npm install -g omg
omg build

```


## Usage

```

omg exec wolfram -a query= <your_query> -e APP_ID = <wolfram_app_id>

```

### OR

```

omg exec wolfram -a query= <your_query> -a units = <metrics/imperial> -e APP_ID = <wolfram_app_id>

```

"units" argument is not required, the default is based on your location.