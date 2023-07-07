import json
import yaml

class SignalWireML:

    def __init__(self, args=None):
        if args is None:
            args = {}
        self._content = {
            'version': args.get('version', '1.0.0')
        }
        self._voice = args.get('voice')
        self._applications = []

    def add_application(self, section, app, args=None):
        if args is None:
            args = {}
        self._applications.append({
            app: args
        })
        self._content.setdefault('sections', {}).setdefault(section, self._applications)

    def render_json(self):
        return json.dumps(self._content, indent=2)

    def render_yaml(self):
        return yaml.dump(self._content)

# Usage example:
swml = SignalWireML(args={'version': '1.0.0', 'voice': 'en-US-Neural2-J'})
swml.add_application("main", "answer")
swml.add_application("main", "play", {
    'urls': [
        "https://github.com/freeswitch/freeswitch-sounds/raw/master/en/us/callie/ivr/48000/ivr-welcome_to_freeswitch.wav"
    ]
})
swml.add_application("main", "hangup")

print(swml.render_json())
