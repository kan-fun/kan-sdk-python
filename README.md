# Install Kan SDK
```bash
pip install kan-sdk
```

# Quick Start
```python
import kan_sdk

# Get AccessKey and SecretKey from http://www.mlflow.org.cn/
AccessKey = 'XXXXXX'
SecretKey = 'XXXXXX'

kan = kan_sdk.Client(AccessKey, SecretKey)
kan.email(topic='topic', msg='msg')
```