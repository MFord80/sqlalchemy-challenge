# Python application

# Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt


# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Station = Base.classes.station
Measurement = Base.classes.measurement

# Flask Setup
app = Flask(__name__)

########################

# Flask Routes

# Static Routes

@app.route("/")
def homepage():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/yyyy-mm-dd<br/>"
        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    recent_date = dt.date(2017, 8, 23)
    query_date = recent_date - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= query_date).all()
    session.close()
    prcp_data = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[date] = prcp
        prcp_data.append(prcp_dict)

    return jsonify(prcp_data)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station, Station.name).all()
    session.close()
    station_data = []
    for station, name in results:
        station_dict = {}
        station_dict['station'] = station
        station_dict['name'] = name
        station_data.append(station_dict)

    return jsonify(station_data)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    most_active_station = 'USC00519281'
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= query_date,\
        Measurement.station == most_active_station).all()
    session.close()
    tobs_data = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict[date] = tobs
        tobs_data.append(tobs_dict)

    return jsonify(tobs_data)


# Dynamic Routes

@app.route("/api/v1.0/<start>")
def temp_start(start):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs),\
        func.max(Measurement.tobs),\
        func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    session.close()
    temp_stats = []
    for min, max, avg in results:
        stats_dict = {}
        stats_dict["TMIN"] = min
        stats_dict["TMAX"] = max
        stats_dict["TAVG"] = round(avg, 3)
        temp_stats.append(stats_dict)

    return jsonify(temp_stats)

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start, end):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs),\
        func.max(Measurement.tobs),\
        func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start, Measurement.date <= end).all()
    session.close()
    temp_stats = []
    for min, max, avg in results:
        stats_dict = {}
        stats_dict["TMIN"] = min
        stats_dict["TMAX"] = max
        stats_dict["TAVG"] = round(avg, 3)
        temp_stats.append(stats_dict)

    return jsonify(temp_stats)


if __name__ == '__main__':
    app.run(debug=True)

