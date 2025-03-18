from cloudevents.http import from_http
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_event():
    # Parse CloudEvent from HTTP request
    event = from_http(request.headers, request.get_data())

    event_id = event.get("id")  # Use the 'get' method to retrieve attributes
    event_type = event.get("type")
    event_source = event.get("source")
    event_time = event.get("time")
    event_data = event.data  # The 'data' is the payload sent with the CloudEvent

    #Get VM name and namespace
    event_metadata = event_data.get("metadata")
    vm_name      = event_metadata.get("name")
    vm_namespace = event_metadata.get("namespace")

    # Print the event attributes (you can also process these as needed)
    print("Event ID:", event_id)
    print("Event Type:", event_type)
    print("Event Source:", event_source)
    print("Event Time:", event_time)

    print("VM Name:", vm_name)
    print("VM Namespace:", vm_namespace)

    #Get VM Phase and status
    event_status = event_data.get("status")
    if event_status is not None:
        vm_phase           = event_status.get("phase")
        vm_printableStatus = event_status.get("printableStatus")
        print("VM Phase:", vm_phase)
        print("VM Status:", vm_printableStatus)

    print("Event Data:")
    print(json.dumps(event_data, indent=4))

    print("----\n\n")

    return "CloudEvent received and printed", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

