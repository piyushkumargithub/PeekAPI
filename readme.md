# PeekAPI

PeekAPI is a Postman-like tool built using Python and CustomTkinter. It provides a user-friendly interface to send and analyze HTTP requests with ease. PeekAPI is designed to handle various HTTP methods, view responses, and manage headers and request bodies effectively.

---

## 🚀 Features

- 🖥️ **Intuitive GUI:** Clean and simple interface with CustomTkinter.
- 🌐 **HTTP Methods:** Supports GET, POST, PUT, DELETE, PATCH requests.
- 📦 **Request Handling:** Automatic parsing of JSON headers and body.
- 🔍 **Response Viewer:** Displays status, headers, and formatted response body.
- ❌ **Error Handling:** Informs user of invalid URLs or request issues.

---

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- `pip` package manager

### 1. Clone the repository
```bash
git clone https://github.com/piyushkumargithub/peekapi.git
cd peekapi
```

### 2. Create a virtual environment
```bash
python -m venv envname
source envname/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🎯 Usage

```bash
python main.py
```

1. Enter the request URL.
2. Choose the HTTP method.
3. Optionally add headers and body.
4. Click **Send Request** and view the response below.

---

## 🧪 Example Request

- URL: `https://jsonplaceholder.typicode.com/posts/1`
- Method: `GET`
- Expected Response: JSON data with post details.

---

## 🌱 Future Enhancements

- 📋 **Request History:** Save and replay previous requests.
- 🧠 **Response Filters:** Format and search within responses.
- 🧬 **Additional Protocols:** Support for WebSocket and GraphQL.

---

## 🤝 Contributing
Feel free to fork this repository, make feature requests, or submit pull requests. Your contributions are welcome!

---

## 📄 License
This project is licensed under the MIT License.

