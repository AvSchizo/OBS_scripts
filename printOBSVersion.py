import obsws_python as obs
from sys import argv

def printOBSVersion(actual=None, ho="localhost", po=4455, pa=None, ti=3):

	if actual == None:

		if pa == None:
			found = None
			for arg in argv:
				if arg.split("=")[0] == "pa":
					wat = arg.split("=")[1]
					found = True
					break
			if found == None:
				print("printOBSVersion: no password given")
				return
		else:
			wat = pa

		try:
			client = obs.ReqClient(host=ho, port=po, password=wat, timeout=ti)
		except:
			print(f"printOBSVersion: no client available with {wat} as password")
			return
		
	else:
		client = actual


	version_info = client.get_version()
	print(f"Connected to OBS version: {version_info.obs_version}")



if __name__ == "__main__":
	defaultPassword = "EK35AJBEoBhuJ91Z"
	printOBSVersion(pa=defaultPassword)