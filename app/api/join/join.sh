#!/bin/bash

API_KEY_SECRET="pradeep"
FLUENTO_URL="http://localhost:3000/api/v1/join"

curl $FLUENTO_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --data '{"room":"test","name":"Pradeep","audio":"true","video":"true","screen":"false","hide":"false","notify":"true","token":{"username":"username","password":"password","presenter":"true", "expire":"1h"}}' \
    --request POST