Instructions for label studio deployment and pushing labeled data to dvc.

1. Create mydata directory: `mkdir mydata`
2. Deploy label-studio with `docker run -it -p 8080:8080 -v mydata:/label-studio/data heartexlabs/label-studio:latest`
3. Go to `localhost:8080`. Create new project with "Semantic segmentaton with masks" subtype. Add labels "Cloud" and "Cloud shadow".
4. Upload batch of images and label them.
5. Export resulting segmentation labels with "Brush labels as png" function to the folder exported_data.
6. Create minio bucket called ml-data
7. Install dvc: `pip install dvc[s3]`
8. Configure dvc and push segmentation masks
```
dvc init --subdir
dvc add exported_data/*.png
dvc remote add -d minio s3://ml-data
dvc remote modify minio endpointurl http://0.0.0.0:9000
export AWS_ACCESS_KEY_ID=minio
export AWS_SECRET_ACCESS_KEY=minio123
dvc push
```
9. With UI check that minio bucket ml-data contains pushed binary objects.
