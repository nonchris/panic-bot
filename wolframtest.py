import wolframalpha

#login to api
app_id = 'W2H5XW-HGP7R53JA6'
client = wolframalpha.Client(app_id)

#question
res = client.query('1*2')

for pod in res.pods:
    for sub in pod.subpods:
        print(sub)