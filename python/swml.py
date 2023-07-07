{
  "version": "1.0.0",
  "ai_prompt": {
    "temperature": "0.9",
    "top_p": "1.0",
    "text": "Your name is Olivia, You are able to lookup weather and time for various locations."
  },
  "ai_post_prompt": {
    "text": "Summarize the conversation"
  },
  "ai_hints": [
    "jokes",
    "weather",
    "time"
  ],
  "ai_post_prompt_url": {
    "post_prompt_url": "$ENV{post_prompt_url}"
  },
  "ai_swaig_defaults": {
    "web_hook_url": "$ENV{web_hook_url}"
  },
  "ai_include": [
    {
      "url": "https://replace-this-with-yours.herokuapp.com/swaig.cgi",
      "auth_user": "user",
      "auth_password": "pass",
      "functions": [
        "get_joke",
        "get_weather",
        "get_time"
      ]
    }
  ],
  "ai_swaig_functions": [
    {
      "function": "get_weather",
      "purpose": "use when inquired about weather anywhere across the globe",
      "argument": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "the location to check the weather in"
          }
        }
      }
    },
    {
      "function": "get_time",
      "purpose": "To determine what the current time is in a provided location.",
      "argument": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The location or name of the city to get the time from."
          }
        }
      }
    }
  ],
  "ai_native_functions": [
    "wait_seconds",
    "check_time"
  ],
  "ai_applications": [
    "main"
  ]
}
