import obsws_python as obs

client = obs.ReqClient(host='localhost', port=4455, password='EK35AJBEoBhuJ91Z', timeout=3)

version_info = client.get_version()
print(f"Connected to OBS version: {version_info.obs_version}")