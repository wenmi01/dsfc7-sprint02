mkdir -p ~/.streamlit/

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml

echo "

" >> ~/.streamlit/config.toml

# echo '[theme]
# base = "dark"
# primaryColor = "Teal"
# backgroundColor = "Silver"
# secondaryBackgroundColor = "Carmine"
# textColor = "Black"
# font = "sans serif"
# ' >> ~/.streamlit/config.toml

# echo "[server]
# headless = true
# port = $PORT
# enableCORS = false
# [theme]
# base = 'dark'
# primaryColor = '#d33682'
# backgroundColor = '#008080'
# secondaryBackgroundColor = '#00000'
# textColor = '#fafafa'
# font = 'sans serif'
# " > ~/.streamlit/config.toml
