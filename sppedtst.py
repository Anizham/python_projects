from speedtest import Speedtest
st= Speedtest()
print("Download Speed in bps",st.download())
print("Upload Speed in bps",st.upload())
