import telebot
from flask import Flask
import threading
import os

# إعدادات البوت
BOT_TOKEN = "ضع_توكن_البوت_هنا"
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# كود HTML الكامل للموقع مدمج مباشرة
WEBSITE_HTML = """
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>خدمة التحميل - حمّال محترف</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            background: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            text-align: center;
        }

        .header h1 {
            color: #1e3c72;
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .header p {
            color: #666;
            font-size: 1.2em;
        }

        .contact-info {
            background: #ffc107;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            display: inline-block;
        }

        .contact-info a {
            color: #000;
            text-decoration: none;
            font-size: 1.3em;
            font-weight: bold;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }

        .service-card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s;
        }

        .service-card:hover {
            transform: translateY(-5px);
        }

        .service-card h2 {
            color: #1e3c72;
            margin-bottom: 20px;
            font-size: 1.8em;
            border-bottom: 3px solid #ffc107;
            padding-bottom: 10px;
        }

        .price-table {
            width: 100%;
            margin-top: 15px;
        }

        .price-row {
            display: flex;
            justify-content: space-between;
            padding: 15px;
            margin-bottom: 10px;
            background: #f8f9fa;
            border-radius: 8px;
            transition: all 0.3s;
        }

        .price-row:hover {
            background: #e9ecef;
            transform: scale(1.02);
        }

        .floor {
            font-weight: bold;
            color: #1e3c72;
        }

        .price {
            color: #28a745;
            font-weight: bold;
            font-size: 1.2em;
        }

        .booking-section {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .booking-section h2 {
            color: #1e3c72;
            margin-bottom: 25px;
            font-size: 2em;
            text-align: center;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
            font-size: 1.1em;
        }

        input, select, textarea {
            width: 100%;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1em;
            transition: border-color 0.3s;
            font-family: inherit;
        }

        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: #1e3c72;
        }

        .quantity-control {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .quantity-btn {
            width: 50px;
            height: 50px;
            border: none;
            background: #1e3c72;
            color: white;
            font-size: 1.5em;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .quantity-btn:hover {
            background: #2a5298;
            transform: scale(1.1);
        }

        .quantity-display {
            font-size: 1.5em;
            font-weight: bold;
            color: #1e3c72;
            min-width: 60px;
            text-align: center;
        }

        .calculate-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.3em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 20px;
        }

        .calculate-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(40, 167, 69, 0.4);
        }

        .submit-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #ffc107 0%, #ff9800 100%);
            color: #000;
            border: none;
            border-radius: 8px;
            font-size: 1.3em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 10px;
        }

        .submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 193, 7, 0.4);
        }

        .total-price {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
            font-size: 1.5em;
            display: none;
        }

        .total-price.show {
            display: block;
            animation: slideIn 0.5s;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            justify-content: center;
            align-items: center;
        }

        .modal.show {
            display: flex;
        }

        .modal-content {
            background: white;
            padding: 40px;
            border-radius: 15px;
            max-width: 500px;
            width: 90%;
            text-align: center;
            animation: zoomIn 0.3s;
        }

        @keyframes zoomIn {
            from {
                transform: scale(0.8);
                opacity: 0;
            }
            to {
                transform: scale(1);
                opacity: 1;
            }
        }

        .modal-content h3 {
            color: #28a745;
            font-size: 2em;
            margin-bottom: 20px;
        }

        .modal-content p {
            font-size: 1.2em;
            margin: 15px 0;
            color: #333;
        }

        .phone-number {
            background: #ffc107;
            padding: 20px;
            border-radius: 10px;
            font-size: 2em;
            font-weight: bold;
            margin: 20px 0;
            direction: ltr;
        }

        .close-btn {
            background: #dc3545;
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 8px;
            font-size: 1.1em;
            cursor: pointer;
            margin-top: 20px;
        }

        .close-btn:hover {
            background: #c82333;
        }

        .icon {
            font-size: 3em;
            margin-bottom: 15px;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 1.8em;
            }
            
            .services-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="icon">🏗️</div>
            <h1>خدمة التحميل المحترفة</h1>
            <p>نوفر خدمة تحميل الرمل والقرافي والورد بأسعار تنافسية</p>
            <div class="contact-info">
                📞 للحجز والاستفسار: <a href="tel:0000000000">0000000000</a>
            </div>
        </div>

        <div class="services-grid">
            <div class="service-card">
                <h2>🪨 الرملة البيضاء</h2>
                <div class="price-table">
                    <div class="price-row">
                        <span class="floor">الطابق الأول</span>
                        <span class="price">250 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الثاني</span>
                        <span class="price">300 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الثالث</span>
                        <span class="price">350 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الرابع</span>
                        <span class="price">400 دج</span>
                    </div>
                </div>
            </div>

            <div class="service-card">
                <h2>🟤 الرملة الحمراء</h2>
                <div class="price-table">
                    <div class="price-row">
                        <span class="floor">الطابق الأول</span>
                        <span class="price">250 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الثاني</span>
                        <span class="price">300 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الثالث</span>
                        <span class="price">350 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الرابع</span>
                        <span class="price">400 دج</span>
                    </div>
                </div>
            </div>

            <div class="service-card">
                <h2>⚫ القرافي</h2>
                <div class="price-table">
                    <div class="price-row">
                        <span class="floor">الطابق الأول</span>
                        <span class="price">250 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الثاني</span>
                        <span class="price">300 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الثالث</span>
                        <span class="price">350 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الرابع</span>
                        <span class="price">400 دج</span>
                    </div>
                </div>
            </div>

            <div class="service-card">
                <h2>🪣 الورد (الماء)</h2>
                <div class="price-table">
                    <div class="price-row">
                        <span class="floor">الطابق الأول</span>
                        <span class="price">5 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الثاني</span>
                        <span class="price">10 دج</span>
                    </div>
                    <div class="price-row">
                        <span class="floor">الطابق الثالث</span>
                        <span class="price">15 دج</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="booking-section">
            <h2>📋 احسب التكلفة واحجز الآن</h2>
            
            <form id="bookingForm">
                <div class="form-group">
                    <label>نوع المادة *</label>
                    <select id="materialType" required>
                        <option value="">اختر المادة...</option>
                        <option value="white-sand">الرملة البيضاء</option>
                        <option value="red-sand">الرملة الحمراء</option>
                        <option value="gravel">القرافي</option>
                        <option value="water">الورد (الماء)</option>
                    </select>
                </div>

                <div class="form-group">
                    <label>الطابق *</label>
                    <select id="floor" required>
                        <option value="">اختر الطابق...</option>
                        <option value="1">الطابق الأول</option>
                        <option value="2">الطابق الثاني</option>
                        <option value="3">الطابق الثالث</option>
                        <option value="4">الطابق الرابع</option>
                    </select>
                </div>

                <div class="form-group">
                    <label>الكمية (بالحمولة)</label>
                    <div class="quantity-control">
                        <button type="button" class="quantity-btn" onclick="changeQuantity(-1)">-</button>
                        <span class="quantity-display" id="quantityDisplay">1</span>
                        <button type="button" class="quantity-btn" onclick="changeQuantity(1)">+</button>
                    </div>
                </div>

                <button type="button" class="calculate-btn" onclick="calculatePrice()">💰 احسب التكلفة</button>

                <div class="total-price" id="totalPrice">
                    <div>التكلفة الإجمالية</div>
                    <div style="font-size: 2em; margin-top: 10px;" id="priceAmount">0 دج</div>
                </div>

                <div class="form-group" style="margin-top: 30px;">
                    <label>الاسم *</label>
                    <input type="text" id="customerName" required placeholder="أدخل اسمك الكامل">
                </div>

                <div class="form-group">
                    <label>رقم الهاتف *</label>
                    <input type="tel" id="customerPhone" required placeholder="0555123456">
                </div>

                <div class="form-group">
                    <label>العنوان *</label>
                    <textarea id="address" rows="3" required placeholder="أدخل العنوان بالتفصيل..."></textarea>
                </div>

                <div class="form-group">
                    <label>ملاحظات إضافية</label>
                    <textarea id="notes" rows="2" placeholder="أي ملاحظات أو طلبات خاصة..."></textarea>
                </div>

                <button type="submit" class="submit-btn">📞 أكمل الحجز واتصل بنا</button>
            </form>
        </div>
    </div>

    <div class="modal" id="confirmModal">
        <div class="modal-content">
            <div class="icon">✅</div>
            <h3>تم تسجيل طلبك بنجاح!</h3>
            <p>شكراً لك على اختيار خدماتنا</p>
            <p style="margin-top: 20px; font-weight: bold;">يرجى الاتصال بنا لتأكيد الحجز:</p>
            <div class="phone-number">
                <a href="tel:0000000000" style="color: #000; text-decoration: none;">0000000000</a>
            </div>
            <p style="color: #666; font-size: 1em;">سنكون في خدمتك من 7 صباحاً إلى 7 مساءً</p>
            <button class="close-btn" onclick="closeModal()">إغلاق</button>
        </div>
    </div>

    <script>
        let quantity = 1;
        let currentPrice = 0;

        const prices = {
            'white-sand': { 1: 250, 2: 300, 3: 350, 4: 400 },
            'red-sand': { 1: 250, 2: 300, 3: 350, 4: 400 },
            'gravel': { 1: 250, 2: 300, 3: 350, 4: 400 },
            'water': { 1: 5, 2: 10, 3: 15 }
        };

        function changeQuantity(change) {
            quantity = Math.max(1, quantity + change);
            document.getElementById('quantityDisplay').textContent = quantity;
            
            if (currentPrice > 0) {
                calculatePrice();
            }
        }

        function calculatePrice() {
            const material = document.getElementById('materialType').value;
            const floor = parseInt(document.getElementById('floor').value);

            if (!material || !floor) {
                alert('⚠️ يرجى اختيار نوع المادة والطابق أولاً');
                return;
            }

            if (material === 'water' && floor > 3) {
                alert('⚠️ خدمة الورد متوفرة حتى الطابق الثالث فقط');
                document.getElementById('floor').value = '';
                return;
            }

            const unitPrice = prices[material][floor];
            const totalPrice = unitPrice * quantity;
            currentPrice = totalPrice;

            document.getElementById('priceAmount').textContent = totalPrice.toLocaleString() + ' دج';
            document.getElementById('totalPrice').classList.add('show');
        }

        document.getElementById('materialType').addEventListener('change', function() {
            const material = this.value;
            const floorSelect = document.getElementById('floor');
            
            if (material === 'water') {
                floorSelect.innerHTML = `
                    <option value="">اختر الطابق...</option>
                    <option value="1">الطابق الأول</option>
                    <option value="2">الطابق الثاني</option>
                    <option value="3">الطابق الثالث</option>
                `;
            } else {
                floorSelect.innerHTML = `
                    <option value="">اختر الطابق...</option>
                    <option value="1">الطابق الأول</option>
                    <option value="2">الطابق الثاني</option>
                    <option value="3">الطابق الثالث</option>
                    <option value="4">الطابق الرابع</option>
                `;
            }
            
            document.getElementById('totalPrice').classList.remove('show');
            currentPrice = 0;
        });

        document.getElementById('bookingForm').addEventListener('submit', function(e) {
            e.preventDefault();

            if (currentPrice === 0) {
                alert('⚠️ يرجى حساب التكلفة أولاً');
                return;
            }

            const bookingData = {
                material: document.getElementById('materialType').options[document.getElementById('materialType').selectedIndex].text,
                floor: document.getElementById('floor').value,
                quantity: quantity,
                totalPrice: currentPrice,
                name: document.getElementById('customerName').value,
                phone: document.getElementById('customerPhone').value,
                address: document.getElementById('address').value,
                notes: document.getElementById('notes').value,
                date: new Date().toLocaleString('ar-DZ')
            };

            let bookings = JSON.parse(localStorage.getItem('bookings') || '[]');
            bookings.push(bookingData);
            localStorage.setItem('bookings', JSON.stringify(bookings));

            document.getElementById('confirmModal').classList.add('show');
        });

        function closeModal() {
            document.getElementById('confirmModal').classList.remove('show');
            document.getElementById('bookingForm').reset();
            quantity = 1;
            document.getElementById('quantityDisplay').textContent = '1';
            document.getElementById('totalPrice').classList.remove('show');
            currentPrice = 0;
        }
    </script>
</body>
</html>
"""

# استضافة الموقع
@app.route('/')
def home():
    return WEBSITE_HTML

# تشغيل Flask في خيط منفصل
def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)

threading.Thread(target=run_flask, daemon=True).start()

# ====== أوامر البوت ======

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('🌐 افتح الموقع', '📞 رقم الهاتف')
    markup.add('ℹ️ معلومات', '📋 الأسعار')
    
    bot.send_message(
        message.chat.id,
        """
🏗️ مرحباً بك في خدمة التحميل المحترفة!

نوفر خدمات:
- الرملة البيضاء والحمراء
- القرافي
- الورد (الماء)

اختر من القائمة أدناه:
        """,
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == '🌐 افتح الموقع')
def open_website(message):
    markup = telebot.types.InlineKeyboardMarkup()
    # غيّر هذا الرابط بعد النشر على Railway أو Render
    btn = telebot.types.InlineKeyboardButton(
        "🌐 افتح الموقع", 
        url="https://your-app-name.railway.app"
    )
    markup.add(btn)
    
    bot.send_message(
        message.chat.id,
        "اضغط على الزر لفتح موقع الحجز:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == '📞 رقم الهاتف')
def send_phone(message):
    bot.send_message(
        message.chat.id,
        """
📞 للحجز والاستفسار:
0000000000

🕐 أوقات العمل:
من 7 صباحاً إلى 7 مساءً
        """
    )

@bot.message_handler(func=lambda message: message.text == '📋 الأسعار')
def send_prices(message):
    bot.send_message(
        message.chat.id,
        """
💰 أسعارنا:

🪨 الرملة (البيضاء/الحمراء) والقرافي:
- الطابق الأول: 250 دج
- الطابق الثاني: 300 دج
- الطابق الثالث: 350 دج
- الطابق الرابع: 400 دج

🪣 الورد (الماء):
- الطابق الأول: 5 دج
- الطابق الثاني: 10 دج
- الطابق الثالث: 15 دج

📌 السعر للحمولة الواحدة
        """
    )

@bot.message_handler(func=lambda message: message.text == 'ℹ️ معلومات')
def send_info(message):
    bot.send_message(
        message.chat.id,
        """
ℹ️ عن خدمتنا:

✅ خدمة تحميل احترافية
✅ أسعار منافسة
✅ عمال محترفون
✅ خدمة سريعة
✅ تغطية جميع المناطق

📞 للحجز: 0000000000
        """
    )

# تشغيل البوت
print("✅ البوت والموقع يعملان الآن...")
print("🌐 الموقع متاح على: http://localhost:8080")
bot.infinity_polling()
