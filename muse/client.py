import webview

webview.create_window(
    title='MUSE Desktop App',
    url='http://plasma.onlix.me/',
    width=450,
    height=650
)
webview.start(debug=True)