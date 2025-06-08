# URL Shortener 🔗

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight web application built with Streamlit that converts long URLs into short, shareable links using TinyURL service.

## Features ✨

- 🌐 Web-based interface (no installation needed)
- ⚡ Instant URL shortening
- 🔒 Automatic URL validation
- 📋 Copy shortened URL with one click
- 🚫 Error handling for invalid URLs

## Requirements 📋

- Python 3.7+
- `streamlit` package
- `pyshorteners` package

## Installation ⚙️

```bash
# Clone the repository
git clone https://github.com/RevanthGangaput/URL_Shortener.git
cd URL_Shortener

# Install dependencies
pip install streamlit pyshorteners
```

## Usage 🚀

1. Run the application:
```bash
streamlit run urlshortener.py
```

2. In the web interface:
   - Paste your long URL in the input box
   - Click "Submit" button
   - Copy your shortened URL from the output

## Supported URL Formats ✔️
- `http://example.com`
- `https://example.com`
- `http://www.example.com/path?query=string`

## How It Works ⚙️
The application uses:
- `pyshorteners` library with TinyURL backend
- Streamlit for web interface
- Basic URL validation before processing


## Contributing 🤝
Contributions are welcome! Please:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License 📄
MIT License - see [LICENSE](LICENSE) file for details

## Notes 📝
- Requires internet connection to shorten URLs
- Uses TinyURL service which has its own terms of service
- For production use, consider adding rate limiting
