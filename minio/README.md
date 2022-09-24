Commands for minio deployment and testing.

Create cluster:

`kind create cluster --name ml-in-production-course-week-2`

Create minio deployment:

```
cd minio
kubectl create -f minio-standalone.yaml
```

Use `k9s` to check if deployment is running.

Port forward API and UI:

```
kubectl port-forward svc/minio-api 9000:9000
kubectl port-forward svc/minio-ui 9001:9001
```


Login to UI by the link `localhost:9001` with credentials and create bucket called models.

Run `python sample_train.py` (it runs dummy training and saves the model to the bucket).

Check if the file `dummy_model` is in the bucket (with UI).

Check tests pass: `pytest minio_tests.py`
