
import sys
sys.path.append('/users/adams/deployment/lib/site-packages')

from flask import Flask, request, jsonify, render_template

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())
