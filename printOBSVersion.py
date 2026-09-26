import obsws_python as obs

def printOBSVersion(actual=None, ho="localhost", po=4455, pa=None, ti=3):
	if actual == None:
		if pa == None:
			print("no client available")
		else:
			try:
				client = obs.ReqClient(host=ho, port=po, password=pa, timeout=ti)
			except:
				print(f"printOBSVersion: no client available with {pa} as password")
				return
	else:
		try:
			client = actual
		except:
			print(f"printOBSVersion: no client as given actual")
			return

	version_info = client.get_version()
	print(f"Connected to OBS version: {version_info.obs_version}")



if __name__ == "__main__":
	defaultPassword = "EK35AJBEoBhuJ91Z"
	printOBSVersion(pa=defaultPassword)