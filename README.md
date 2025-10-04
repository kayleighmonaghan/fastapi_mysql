# Eat with the Seasons API
## Local startup
Open Terminal in the project directory.
Enter `py -m uvicorn main:app --reload`
`ctrl+click` the path in the output and add `/docs` to the end: `127.0.0.1:8000/docs` 

Required installations found in `requirements.txt`

## Hosting with ngrok
in terminal / powershell: `ngrok http http://127.0.0.1:8000`
this will begin hosting the api with a placeholder URL.

### Once a domain is secured. Update ngrok config.
in terminal / powershell: 
`ngrok http $PORT_NUMBER --url $YOUR_DOMAIN`
then:
`ngrok config edit`
paste at bottom of config.yml:
```endpoints:
  - name: cli-quickstart
    url: $YOUR_DOMAIN
    traffic_policy:
      on_http_request:
        - actions:
          - type: oauth
            config:
              provider: google
    upstream:
      url: 8080
      protocol: http1

ngrok paid plan is required at this point.