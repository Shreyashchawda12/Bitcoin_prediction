from flask import Flask,request,render_template,jsonify
from src.pipeline.predict_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            Open=float(request.form.get('Open')),
            High=float(request.form.get('High')),
            Low=float(request.form.get('Low')),
            Close=float(request.form.get('Close')),
            Volume=float(request.form.get('Volume')),
            Market_Cap=float(request.form.get('Market_Cap')),
            Tomorrow = float(request.form.get('Tomorrow')),
            
           
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        def final_result(pred):
            if pred==1:
                result='Bitcoin price will go up'
            else:
                result = 'Bitcoin price will go down'
            return result
        
        final_results = final_result(pred)
            

        return render_template('results.html',final_results = final_result(pred))






if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
