import speedtest as st
"""
    upspeed : speed at which data sent from our device to internet used for uploading files and sending emails 
    download speed : viceversa  useful for Streaming videos and Browsing websites.
    ping : time taken to travel small data packet to travel to a server and back. lesser the time more the faster
            the connection
    Mbps(mega bits per second) : internet speed measured in bits per sec (bps)  
    """
def SpeedTest():
    test = st.Speedtest()
    download = test.download()
    download_speed = round(download/10**6,2)
    upload = test.upload()
    up_speed = round(upload/10**6,2)
    ping = test.results.ping
    print(f"upspeed is {up_speed}\n download speed is {download_speed}")
    print(f"ping status {ping}")
SpeedTest()

