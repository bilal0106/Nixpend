from flask import Flask, request, send_file
import io
import qrcode

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(str(data))
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    pdf = io.BytesIO()
    img.save(pdf, "PDF")
    pdf.seek(0)
    return send_file(pdf, attachment_filename="data.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
