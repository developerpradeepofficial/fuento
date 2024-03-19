#!/bin/bash

API_KEY_SECRET="pradeep"
FLUENTO_URL="http://localhost:3000/api/v1/meeting"

curl $FLUENTO_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --request POST