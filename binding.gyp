{
  "targets": [
    {
      "target_name": "liblibuuid",
      "sources": [ "src/uuid.cc" ],
      "link_settings": {
        "libraries": ["-luuid"]
      },
      "conditions": [
        ["OS=='mac'",{
          "link_settings":{
            "libraries": ["-uuid"]
          }
        }]
      ]
    }
  ]
}
