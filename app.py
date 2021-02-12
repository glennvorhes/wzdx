from flask import Flask, render_template, url_for
from db import get_oracle_connection, get_oracle_engine, get_oracle_session
from flask import jsonify
import models as m
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', endPoints=[url_for('api1'), url_for('api2')])


@app.route('/api1')
def api1():
    sess = get_oracle_session()

    f = sess.query(m.Facility).first()
    assert isinstance(f, m.Facility)

    j = json.loads(f.geojson)

    j['closureId'] = f.closureid
    j['facilityId'] = f.facilityid
    j['recordNum'] = f.recordnum
    j['laneDetails'] = f.lanedetails
    j['duration'] = f.duration
    j['startDate'] = f.startdate.strftime("%Y/%m/%d")
    j['endDate'] = f.enddate.strftime("%Y/%m/%d")

    return jsonify(j)


@app.route('/api2')
def api2():
    return jsonify({"v": 1})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8085)


