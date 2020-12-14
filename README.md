# allcountrycode

# allcountrycode

This repositry code helps to retrive country name when country code is given. 

##CLI DIR##
1. API data from https://www.travel-advisory.info/api  is stored in a file called data.json.
2. country_source_code.py helps to retrive the country name by reading data.json when we pass country code as cmd line argument.
3. Executiton of script takes singe country code as well as multiple country codes as the cmd line argument. For example:
```
python country_source_code.py  AE US IN ABCD
AE United Arab Emirates
US United States
IN India
ABCD Country Code Not Found in API JSON
```

## webapp ##
1.Used Flask, which is a python micro-framework to create web application serrvices.
2.So installed python module called flask and requests. These can be called as pre-requisties
3.Finally app.py in webapp/app/app.py dir helps to give webapp service to get country name when we pass country codes in the browser.
4.As part it also enabled another routes to check health status and status of the api as below
```
python app.py
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 409-049-278


In browser if you enter below url with /diag   it returns as follows:
 http://localhost:5000/diag
 {"code": 200, "status": "ok", "note": "The api works, we could fetch countries.", "cache": "cached", "count": 238}

/health gives health status of app
status: running active
```
5. /convert helps to give country name when we pass countries codes as below
```
http://localhost:5000/convert?cc=AE US IN ABCD
above url returns as below:

AE United Arab Emirates
US United States
IN India
ABCD Country Code Not Found in API JSON

```

## K8s DIR ##
1.Once my service is created, now we are ready to deploy in local k8s cluster.
2.To deploy in a cluster, we need to create a image from the above service by writing a dockerfile.
3.Dockerfile in webapp/Dockerfile directory create the image locally. Then we can push to dockerhub registries or ECR OR GCR.
4.In k8s DIR we have a file called allcountrycode.yaml which has k8s kind deployment/service/ingress. All this helps to deploy my app in local k8s cluster and I can access my allcountrycode service at sateeshallcountrycodes.com as above endpoints.

##  Monitoring ##
Deployed prometheus on the k8s cluster locally to monitor the endpoint of allcountrycode service.
As of part it applied prometheus-deployment.yaml, prometheus-service.yaml, rbac.yaml, prometheus.yml
promtheus.yaml here refers to config-map used by deployment yaml
rbac.yaml helps to grant some permissions to Prometheus to access pods, endpoints, and services running in your cluster
