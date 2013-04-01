{
  "targets": [
    {
      "target_name": "liblibuuid",
      "sources": [ "src/uuid.cc" ],
      "conditions": [
        ["OS=='linux'",{
          "link_settings":{
            "libraries": ["-luuid"]
          }
        }],
        ["OS=='mac'",{
          "link_settings":{
            "libraries": ["-uuid"]
          }
        }]
      ]
    }
  ]
}
