#!/bin/bash
grep 'typeName = "' chat.js | while read -r line; do
  class=$(echo "$line" | grep -oP 'class \K\w+')
  type=$(echo "$line" | grep -oP '"exa\.\K[^"]+')
  
  if [[ "$type" == *"Context"* ]]; then
    echo "Core Context: $class → $type"
  elif [[ "$type" =~ File|Directory|Repo ]]; then
    echo "File/Repo: $class → $type" 
  elif [[ "$type" =~ Knowledge|Document|Slack|Jira ]]; then
    echo "Knowledge Base: $class → $type"
  else
    echo "Other: $class → $type"
  fi
done > class-categories.txt