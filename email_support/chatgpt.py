################################################################################
### Step 1
################################################################################


import os
import openai

def init_api():
     with open(".env") as env:
         for line in env:
             key, value = line.strip().split("=")
             os.environ[key] = value

     openai.api_key = os.environ.get("API_KEY")
     openai.organization = os.environ.get("ORG_ID")

init_api()

products = """
{
    "TechPro Ultrabook": {
        "name": "TechPro Ultrabook",
        "category": "Computers and Laptops",
        "brand": "TechPro",
        "model_number": "TP-UB100",
        "warranty": "1 year",
        "rating": 4.5,
        "features": ["13.3-inch display", "8GB RAM", 
                  "256GB SSD", "Intel Core i5 processor"],
        "description": "A sleek and lightweight ultrabook 
                  for everyday use.",
        "price": 799.99
    },
    "BlueWave Gaming Laptop": {
        "name": "BlueWave Gaming Laptop",
        "category": "Computers and Laptops",
        "brand": "BlueWave",
        "model_number": "BW-GL200",
        "warranty": "2 years",
        "rating": 4.7,
        "features": ["15.6-inch display", "16GB RAM", 
                  "512GB SSD", "NVIDIA GeForce RTX 3060"],
        "description": "A high-performance gaming laptop for 
                  an immersive experience.",
        "price": 1199.99
    },
    "PowerLite Convertible": {
        "name": "PowerLite Convertible",
        "category": "Computers and Laptops",
        "brand": "PowerLite",
        "model_number": "PL-CV300",
        "warranty": "1 year",
        "rating": 4.3,
        "features": ["14-inch touchscreen", "8GB RAM", 
                  "256GB SSD", "360-degree hinge"],
        "description": "A versatile convertible laptop with 
                  a responsive touchscreen.",
        "price": 699.99
    },
    "TechPro Desktop": {
        "name": "TechPro Desktop",
        "category": "Computers and Laptops",
        "brand": "TechPro",
        "model_number": "TP-DT500",
        "warranty": "1 year",
        "rating": 4.4,
        "features": ["Intel Core i7 processor", "16GB RAM", 
                  "1TB HDD", "NVIDIA GeForce GTX 1660"],
        "description": "A powerful desktop computer for work 
                  and play.",
        "price": 999.99
    },
    "BlueWave Chromebook": {
        "name": "BlueWave Chromebook",
        "category": "Computers and Laptops",
        "brand": "BlueWave",
        "model_number": "BW-CB100",
        "warranty": "1 year",
        "rating": 4.1,
        "features": ["11.6-inch display", "4GB RAM", 
                  "32GB eMMC", 
                  "Chrome OS"],
        "description": "A compact and affordable Chromebook 
                  for everyday tasks.",
        "price": 249.99
    },
    "SmartX ProPhone": {
        "name": "SmartX ProPhone",
        "category": "Smartphones and Accessories",
        "brand": "SmartX",
        "model_number": "SX-PP10",
        "warranty": "1 year",
        "rating": 4.6,
        "features": ["6.1-inch display", "128GB storage", 
                  "12MP dual camera", "5G"],
        "description": "A powerful smartphone with advanced 
                  camera features.",
        "price": 899.99
    },
    "MobiTech PowerCase": {
        "name": "MobiTech PowerCase",
        "category": "Smartphones and Accessories",
        "brand": "MobiTech",
        "model_number": "MT-PC20",
        "warranty": "1 year",
        "rating": 4.3,
        "features": 
             ["5000mAh battery", "Wireless charging", 
             "Compatible with SmartX ProPhone"],
        "description": 
             "A protective case with built-in battery 
             for extended usage.",
        "price": 59.99
    },
    "SmartX MiniPhone": {
        "name": "SmartX MiniPhone",
        "category": "Smartphones and Accessories",
        "brand": "SmartX",
        "model_number": "SX-MP5",
        "warranty": "1 year",
        "rating": 4.2,
        "features": ["4.7-inch display", "64GB storage", 
                  "8MP camera", "4G"],
        "description": "A compact and affordable smartphone 
                  for basic tasks.",
        "price": 399.99
    },
    "MobiTech Wireless Charger": {
        "name": "MobiTech Wireless Charger",
        "category": "Smartphones and Accessories",
        "brand": "MobiTech",
        "model_number": "MT-WC10",
        "warranty": "1 year",
        "rating": 4.5,
        "features": ["10W fast charging", "Qi-compatible", 
                  "LED indicator", "Compact design"],
        "description": "A convenient wireless charger for 
                  a clutter-free workspace.",
        "price": 29.99
    },
    "SmartX EarBuds": {
        "name": "SmartX EarBuds",
        "category": "Smartphones and Accessories",
        "brand": "SmartX",
        "model_number": "SX-EB20",
        "warranty": "1 year",
        "rating": 4.4,
        "features": ["True wireless", "Bluetooth 5.0", 
                  "Touch controls", "24-hour battery life"],
        "description": "Experience true wireless freedom with 
                  these comfortable earbuds.",
        "price": 99.99
    },

    "CineView 4K TV": {
        "name": "CineView 4K TV",
        "category": "Televisions and Home Theater Systems",
        "brand": "CineView",
        "model_number": "CV-4K55",
        "warranty": "2 years",
        "rating": 4.8,
        "features": ["55-inch display", "4K resolution", 
                  "HDR", "Smart TV"],
        "description": "A stunning 4K TV with vibrant colors 
                  and smart features.",
        "price": 599.99
    },
    "SoundMax Home Theater": {
        "name": "SoundMax Home Theater",
        "category": "Televisions and Home Theater Systems",
        "brand": "SoundMax",
        "model_number": "SM-HT100",
        "warranty": "1 year",
        "rating": 4.4,
        "features": ["5.1 channel", "1000W output", 
                  "Wireless subwoofer", "Bluetooth"],
        "description": "A powerful home theater system for 
                  an immersive audio experience.",
        "price": 399.99
    },
    "CineView 8K TV": {
        "name": "CineView 8K TV",
        "category": "Televisions and Home Theater Systems",
        "brand": "CineView",
        "model_number": "CV-8K65",
        "warranty": "2 years",
        "rating": 4.9,
        "features": ["65-inch display", "8K resolution", 
                  "HDR", "Smart TV"],
        "description": "Experience the future of television 
                  with this stunning 8K TV.",
        "price": 2999.99
    },
    "SoundMax Soundbar": {
        "name": "SoundMax Soundbar",
        "category": "Televisions and Home Theater Systems",
        "brand": "SoundMax",
        "model_number": "SM-SB50",
        "warranty": "1 year",
        "rating": 4.3,
        "features": ["2.1 channel", "300W output", 
                  "Wireless subwoofer", "Bluetooth"],
        "description": "Upgrade your TV's audio with this 
                  sleek and powerful soundbar.",
        "price": 199.99
    },
    "CineView OLED TV": {
        "name": "CineView OLED TV",
        "category": "Televisions and Home Theater Systems",
        "brand": "CineView",
        "model_number": "CV-OLED55",
        "warranty": "2 years",
        "rating": 4.7,
        "features": ["55-inch display", "4K resolution", 
                  "HDR", "Smart TV"],
        "description": "Experience true blacks and vibrant 
                  colors with this OLED TV.",
        "price": 1499.99
    },

    "GameSphere X": {
        "name": "GameSphere X",
        "category": "Gaming Consoles and Accessories",
        "brand": "GameSphere",
        "model_number": "GS-X",
        "warranty": "1 year",
        "rating": 4.9,
        "features": ["4K gaming", "1TB storage", 
                  "Backward compatibility", 
                  "Online multiplayer"],
        "description": 
                  "A next-generation gaming console for 
                  the ultimate gaming experience.",
        "price": 499.99
    },
    "ProGamer Controller": {
        "name": "ProGamer Controller",
        "category": "Gaming Consoles and Accessories",
        "brand": "ProGamer",
        "model_number": "PG-C100",
        "warranty": "1 year",
        "rating": 4.2,
        "features": ["Ergonomic design", 
                  "Customizable buttons", 
                  "Wireless", "Rechargeable battery"],
        "description": "A high-quality gaming controller 
                  for precision and comfort.",
        "price": 59.99
    },
    "GameSphere Y": {
        "name": "GameSphere Y",
        "category": "Gaming Consoles and Accessories",
        "brand": "GameSphere",
        "model_number": "GS-Y",
        "warranty": "1 year",
        "rating": 4.8,
        "features": ["4K gaming", "500GB storage", 
                  "Backward compatibility", 
                  "Online multiplayer"],
        "description": "A compact gaming console 
                  with powerful performance.",
        "price": 399.99
    },
    "ProGamer Racing Wheel": {
        "name": "ProGamer Racing Wheel",
        "category": "Gaming Consoles and Accessories",
        "brand": "ProGamer",
        "model_number": "PG-RW200",
        "warranty": "1 year",
        "rating": 4.5,
        "features": ["Force feedback", "Adjustable pedals", 
                  "Paddle shifters", 
                  "Compatible with GameSphere X"],
        "description": "Enhance your racing games with 
                  this realistic racing wheel.",
        "price": 249.99
    },
    "GameSphere VR Headset": {
        "name": "GameSphere VR Headset",
        "category": "Gaming Consoles and Accessories",
        "brand": "GameSphere",
        "model_number": "GS-VR",
        "warranty": "1 year",
        "rating": 4.6,
        "features": ["Immersive VR experience", 
            "Built-in headphones", 
            "Adjustable headband", 
            "Compatible with GameSphere X"],
        "description": 
             "Step into the world of virtual reality 
             with this comfortable VR headset.",
        "price": 299.99
    },

    "AudioPhonic Noise-Canceling Headphones": {
        "name": "AudioPhonic Noise-Canceling Headphones",
        "category": "Audio Equipment",
        "brand": "AudioPhonic",
        "model_number": "AP-NC100",
        "warranty": "1 year",
        "rating": 4.6,
        "features": ["Active noise-canceling", "Bluetooth", 
                  "20-hour battery life", "Comfortable fit"],
        "description": "Experience immersive sound with 
                  these noise-canceling headphones.",
        "price": 199.99
    },
    "WaveSound Bluetooth Speaker": {
        "name": "WaveSound Bluetooth Speaker",
        "category": "Audio Equipment",
        "brand": "WaveSound",
        "model_number": "WS-BS50",
        "warranty": "1 year",
        "rating": 4.5,
        "features": ["Portable", "10-hour battery life", 
                  "Water-resistant", "Built-in microphone"],
        "description": "A compact and versatile Bluetooth 
                  speaker for music on the go.",
        "price": 49.99
    },
    "AudioPhonic True Wireless Earbuds": {
        "name": "AudioPhonic True Wireless Earbuds",
        "category": "Audio Equipment",
        "brand": "AudioPhonic",
        "model_number": "AP-TW20",
        "warranty": "1 year",
        "rating": 4.4,
        "features": ["True wireless", "Bluetooth 5.0", 
                  "Touch controls", "18-hour battery life"],
        "description": "Enjoy music without wires with these 
                  comfortable true wireless earbuds.",
        "price": 79.99
    },
    "WaveSound Soundbar": {
        "name": "WaveSound Soundbar",
        "category": "Audio Equipment",
        "brand": "WaveSound",
        "model_number": "WS-SB40",
        "warranty": "1 year",
        "rating": 4.3,
        "features": ["2.0 channel", "80W output", 
                  "Bluetooth", "Wall-mountable"],
        "description": "Upgrade your TV's audio with 
                  this slim and powerful soundbar.",
        "price": 99.99
    },
    "AudioPhonic Turntable": {
        "name": "AudioPhonic Turntable",
        "category": "Audio Equipment",
        "brand": "AudioPhonic",
        "model_number": "AP-TT10",
        "warranty": "1 year",
        "rating": 4.2,
        "features": ["3-speed", "Built-in speakers", 
                  "Bluetooth", "USB recording"],
        "description": "Rediscover your vinyl collection 
                  with this modern turntable.",
        "price": 149.99
    },

    "FotoSnap DSLR Camera": {
        "name": "FotoSnap DSLR Camera",
        "category": "Cameras and Camcorders",
        "brand": "FotoSnap",
        "model_number": "FS-DSLR200",
        "warranty": "1 year",
        "rating": 4.7,
        "features": ["24.2MP sensor", "1080p video", 
              "3-inch LCD", 
              "Interchangeable lenses"],
        "description": 
              "Capture stunning photos and videos 
              with this versatile DSLR camera.",
        "price": 599.99
    },
    "ActionCam 4K": {
        "name": "ActionCam 4K",
        "category": "Cameras and Camcorders",
        "brand": "ActionCam",
        "model_number": "AC-4K",
        "warranty": "1 year",
        "rating": 4.4,
        "features": ["4K video", "Waterproof", 
                  "Image stabilization", "Wi-Fi"],
        "description": "Record your adventures with this 
                  rugged and compact 4K action camera.",
        "price": 299.99
    },
    "FotoSnap Mirrorless Camera": {
        "name": "FotoSnap Mirrorless Camera",
        "category": "Cameras and Camcorders",
        "brand": "FotoSnap",
        "model_number": "FS-ML100",
        "warranty": "1 year",
        "rating": 4.6,
        "features": ["20.1MP sensor", "4K video", 
             "3-inch touchscreen", 
             "Interchangeable lenses"],
        "description": "A compact and lightweight mirrorless 
                  camera with advanced features.",
        "price": 799.99
    },
    "ZoomMaster Camcorder": {
        "name": "ZoomMaster Camcorder",
        "category": "Cameras and Camcorders",
        "brand": "ZoomMaster",
        "model_number": "ZM-CM50",
        "warranty": "1 year",
        "rating": 4.3,
        "features": ["1080p video", "30x optical zoom", 
                  "3-inch LCD", "Image stabilization"],
        "description": "Capture life's moments with this 
                  easy-to-use camcorder.",
        "price": 249.99
    },
    "FotoSnap Instant Camera": {
        "name": "FotoSnap Instant Camera",
        "category": "Cameras and Camcorders",
        "brand": "FotoSnap",
        "model_number": "FS-IC10",
        "warranty": "1 year",
        "rating": 4.1,
        "features": ["Instant prints", "Built-in flash", 
                  "Selfie mirror", "Battery-powered"],
        "description": "Create instant memories with this 
                  fun and portable instant camera.",
        "price": 69.99
    }
}
"""




class ChatGpt:
    def answer_question(
        self,
        model="gpt-3.5-turbo-instruct",
        comment="Am I allowed to publish model outputs to Twitter, without a human review?",
        max_len=1800,
        size="ada",
        debug=False,
        max_tokens=500,
        context="Asuming that you provide customer support for an electronic product company.",
        stop_sequence=None

    ):
        """
        Answer a question based on the most similar context from the dataframe texts
        """
        
        # If debug, print the raw model response


        try:
            # Create a completions using the questin and context
            response = openai.Completion.create(
                prompt=f"""context: {context} comment: {comment} answer:""",
                temperature=0,
                max_tokens=max_tokens,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=stop_sequence,
                model=model,
            )
            return response["choices"][0]["text"].strip()
        except Exception as e:
            print(e)
            return ""
    
    def email_subject(self, comment):
        context = "Asuming that you provide customer support for an electronic product company.\n The following text is the customer's comment about the products, please generate a subject in English of the comment. The subject will be used as the subject of the email to be sent to the customer. "
        return self.answer_question(comment=comment, context=context, stop_sequence="###").strip('"')

    def generate_summary(self, comment):
        context = "Asuming that you provide customer support for an electronic product company.\n The following text is the customer's comment about the products, please generate a summary in English of the comment. The summary will be used as the body of the email to be sent to the customer. Our Comapany is called Z company Use this as signing the email "
        return self.answer_question(comment=comment, context=context, stop_sequence="###").strip('"')
    
    def sentiment_analysis(self, comment):
        context = "Asuming that you provide customer support for an electronic product company.\nPlease do sentiment analysis based on the following comment.\nThe result of the sentiment analysis shows whether the customer's comment is\nPositive or Negative"
        return self.answer_question(comment=comment, context=context, stop_sequence="###").strip('"')

    def generate_email(self, comment, language="English"):
        context = f"""Asuming that you provide customer support for an electronic product company name Z company.
Please create an email in {language} language to be sent to the customer based on
1. The customer's comment {comment}
2. The email content should be like this { self.generate_summary(comment=comment)}
3. The result of the sentiment analysis of the customer's comment { self.sentiment_analysis(comment=comment) }
4. The Subject of the email {self.email_subject(comment=comment)} """
        
        # print(context)
        
        return self.answer_question(comment=comment, context=context, stop_sequence="###").strip('"')
    

if __name__ == "__main__":
    comments = [
    " I purchased the BlueWave Gaming Laptop, and I must say it's a beast of a machine. The NVIDIA GeForce RTX 3060 provides stunning graphics, and the 16GB RAM ensures smooth gameplay. The 2-year warranty gives me peace of mind, and the overall build quality is excellent. Highly recommended for gamers!",
   "The SmartX ProPhone is a top-notch smartphone. Its 5G capabilities make browsing and streaming lightning-fast, and the camera quality is impressive. The 128GB storage is more than enough for my needs, and the 1-year warranty is reassuring. It's definitely worth the price.",
    "I'm disappointed with the MobiTech PowerCase. While it does provide extra battery life, it feels bulky and adds significant weight to my phone. The wireless charging is slow, and it's not as convenient as I had hoped. Not worth the price in my opinion.",
    "I bought the CineView 4K TV, and it's like having a mini cinema at home. The 55-inch 4K display and HDR support offer breathtaking visuals. The 2-year warranty is a nice bonus, and the smart TV features are convenient. Movie nights have never been better!",
    "The SmartX MiniPhone fell short of my expectations. The 4.7-inch display feels outdated, and the 64GB storage is limited. It struggles with multitasking, and the 4G connectivity isn't up to par with modern smartphones. I regret not investing more for a better device.",
    "The AudioPhonic Noise-Canceling Headphones are a game-changer. The active noise-canceling works wonders, and the sound quality is crystal clear. They're comfortable for extended use, and the 20-hour battery life is impressive. A must-have for music lovers!",
    "I encountered issues with the WaveSound Bluetooth Speaker after a few months of use. The battery life has significantly decreased, and the water-resistance feature doesn't seem as reliable as advertised. It's a letdown considering the initial price.",
    "I'm thrilled with my purchase of the GameSphere X gaming console. The 4K gaming experience is mind-blowing, and the backward compatibility is a huge plus. The 1TB storage ensures I have plenty of games to enjoy, and the online multiplayer is a blast.",
    "The ProGamer Controller didn't live up to the hype. The buttons started to stick after a few weeks of use, and the wireless connection occasionally drops. It's frustrating during intense gaming sessions. I expected better quality for the price.",
    "The SmartX EarBuds are a true gem. They provide a seamless wireless experience with Bluetooth 5.0 and have a remarkable 24-hour battery life. The touch controls are intuitive, and the sound quality is fantastic. A great investment for music enthusiasts on the go."
    ]
    ChatGpt = ChatGpt()
    for comment in comments[:1]:
        print(ChatGpt.generate_email(comment=comment, language="Spanish"))

