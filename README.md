[![English](https://img.shields.io/badge/English-blue.svg)](README.md)
[![Português](https://img.shields.io/badge/Português-green.svg)](README.ptbr.md)

![Project Status](https://img.shields.io/badge/status-WIP-blue)

🚧 This project is still under development and may change frequently. It contains bugs. It is intended for learning and experimentation purposes only.

💬 Feedback and contributions are always welcome! Feel free to open issues, fork the project, submit pull requests, etc. All help is appreciated! 

---

# Infrapulse 

**Infrapulse** is a collection of Python scripts that interact with AWS services using [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), AWS's official Python SDK. The application features a Text User Interface (TUI) built with [Textual](https://textual.textualize.io/), providing an interactive terminal-based dashboard for AWS resource management. This is a study project with the purpose of learning and experimenting with AWS resource management via API calls, as well as diving deeper into Python programming.

### Features

- Simple AWS resource management with Python scripts
- Terminal-based user interface built with [Textual](https://textual.textualize.io/)
- Leverages `boto3` to interact with AWS services
- Helps in understanding AWS automation and scripting

### Prerequisites

- Python 3.x installed
- AWS credentials configured (`aws configure` or via IAM roles)
- (Optional) [LocalStack](https://docs.localstack.cloud/getting-started/) for testing AWS APIs locally

### Usage

1. Clone this repository:

```
git clone https://github.com/juanplagos/infrapulse.git  
cd infrapulse
```

2. Install dependencies:

```
pip install -r requirements.txt
```
3. Run:

```python
python app.py
```

---