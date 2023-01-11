# DRF Validate Upload File

## Name
DRF handle Validate upload file

## Description
this util use for DRF handle Validate upload file

Also in your settings you should define these:
```
FILE_UPLOAD_MAX_MEMORY_SIZE = 10000
FILE_SUPPORTED_EXTENTION = []
FILE_SUPPORTED_TYPES = []
```

## Usage
For example in your views, you can proceed as blow:

```
this_file = request.FILES["file"]

validation_status = validate_upload_file(this_file)

if validation_status["code"] != 200:
    return Response(
        {"error": validation_status["message"]}, validation_status["code"]
    )
```
