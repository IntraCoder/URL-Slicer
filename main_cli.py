print("------------------------ URL Slicer ------------------------")

url = input("\n>>> Enter URL : ").strip()

if not url:
    print("[-] Please Enter a URL")

else:

    if "http" in url:
        security = url.split("/")[0]
        slice_url = url.split("/")[2]
    else:
        slice_url = url.split("/")[0]

    print("[+] Sliced URL :", slice_url)
