import obspython as obs

def script_description():
	return "A simple Python script inside OBS Studio."

def script_load(settings):
	print("Python script has loaded successfully!")

# Example: trigger an action when the stream starts
def on_event(event):
	if event == obs.OBS_FRONTEND_EVENT_STREAMING_STARTED:
		print("Stream started!")

def script_load(settings):
	obs.obs_frontend_add_event_callback(on_event)