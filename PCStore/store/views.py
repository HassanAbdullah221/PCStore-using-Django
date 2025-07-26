from decimal import Decimal
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import *
from django.contrib import messages

def add_pc_view(request: HttpRequest):
    if request.method == "POST":
        new_pc = PC(
            name=request.POST["name"],
            cpu=request.POST["cpu"],
            gpu=request.POST["gpu"],
            ram=request.POST["ram"],
            storage=request.POST["storage"],
            price=request.POST["price"],
            image=request.FILES["image"],
        )
        new_pc.save()
        return redirect('store:admin_pc_view')
    
    return render(request, "store/add_pc.html")


def add_product_view(request: HttpRequest):
    products = [
    {"name": "PC", "url_name": "store:admin_pc_view", "image_url": "/static/images/Products/PC.png"},
    {"name": "Monitor", "url_name": "store:admin_monitor_view", "image_url": "/static/images/Products/monitor.png"},
    {"name": "Keyboard", "url_name": "store:admin_keyboard_view", "image_url": "/static/images/Products/keyboard.png"},
    {"name": "Headset", "url_name": "store:admin_headset_view", "image_url": "/static/images/Products/headset.png"},
    {"name": "Mouse", "url_name": "store:admin_mouse_view", "image_url": "/static/images/Products/mouse.png"},
    {"name": "Gaming Chair", "url_name": "store:admin_chair_view", "image_url": "/static/images/Products/chair.png"},
    ]

    return render(request, "store/add_product.html", {"products": products})



def pc_detail_view(request: HttpRequest , pc_id :int):
     
    pc = PC.objects.get(pk=pc_id)

    pcs = PC.objects.filter(category=pc.category).exclude(pk=pc.id)[0:6]
   
    comments = PC_comment.objects.filter(pc=pc)

    return render(request, "store/pc_detail.html", {"pc" : pc , "pcs" : pcs , "comments" : comments})

    

def update_pc_view(request: HttpRequest, pc_id: int):

    pc = PC.objects.get(pk=pc_id)

    if request.method == "POST":
        pc.name=request.POST["name"]
        pc.cpu=request.POST["cpu"]
        pc.gpu=request.POST["gpu"]
        pc.ram=request.POST["ram"]
        pc.storage=request.POST["storage"]
        pc.stock=request.POST["stock"]

        pc.price=request.POST["price"]
        pc.price = Decimal(request.POST["price"])

        if "image" in request.FILES : pc.image = request.FILES["image"]
        
        pc.save()
        
        return redirect('store:admin_pc_view' )
    
    return render(request, "store/update_pc.html", {"pc": pc})


def delete_pc_view(request: HttpRequest , pc_id: int):

    pc = PC.objects.get(pk=pc_id)

    pc.delete()
    return redirect('store:admin_pc_view')

def delete_monitor_view(request: HttpRequest , monitor_id: int):

    monitor = Monitor.objects.get(pk=monitor_id)

    monitor.delete()
    return redirect('store:admin_monitor_view')

def display_all_view(request: HttpRequest):
    pcs = PC.objects.all()
    monitors  = Monitor.objects.all()
    mouses  = Mouse.objects.all()
    chairs  = Chair.objects.all()
    headsets  = Headset.objects.all()
    keyboards  = Keyboard.objects.all()

    return render(request, "store/display_all.html", {
        "pcs" : pcs , 
        "monitors" : monitors , 
        "mouses" : mouses , 
        "chairs" : chairs,
        "headsets" : headsets,
        "keyboards" : keyboards,
        })
    
    
    
def add_monitor_view(request: HttpRequest):
    if request.method == "POST":
        new_monitor = Monitor(
            name=request.POST["name"],
            size_in_inches=request.POST["size_in_inches"],
            resolution=request.POST["resolution"],
            refresh_rate=request.POST["refresh_rate"],
            price=Decimal(request.POST["price"]),
            image=request.FILES["image"],
        )
        new_monitor.save()
        return redirect('store:admin_monitor_view')
    
    return render(request, "store/add_monitor.html")

def update_monitor_view(request: HttpRequest, monitor_id: int):
    monitor = Monitor.objects.get( pk=monitor_id)

    if request.method == "POST":
        monitor.name = request.POST["name"]
        monitor.size_in_inches = request.POST["size_in_inches"]
        monitor.resolution = request.POST["resolution"]
        monitor.refresh_rate = request.POST["refresh_rate"]
        monitor.stock=request.POST["stock"]

        monitor.price = Decimal(request.POST["price"])

        if "image" in request.FILES:
            monitor.image = request.FILES["image"]
        
        monitor.save()

        return redirect('store:admin_monitor_view')
    
    return render(request, "store/update_monitor.html", {"monitor": monitor})

def monitor_detail_view(request: HttpRequest , monitor_id :int):
    monitor = Monitor.objects.get(pk=monitor_id)
    monitors = Monitor.objects.filter(category=monitor.category).exclude(pk=monitor.id)[0:6]
    comments = Monitor_comment.objects.filter(monitor=monitor)

    return render(request, "store/monitor_detail.html", {"monitor" : monitor , "monitors" : monitors , "comments" : comments})


def add_mouse_view(request: HttpRequest):
    if request.method == "POST":
        new_mouse = Mouse(
            name=request.POST["name"],
            dpi=request.POST["dpi"],
            connection_type=request.POST["connection_type"],
            price=request.POST["price"],
            image=request.FILES["image"],
        )
        new_mouse.save()
        return redirect('store:admin_mouse_view')
    
    return render(request, "store/add_mouse.html")
   
def delete_mouse_view(request: HttpRequest , mouse_id: int):

    mouse = Mouse.objects.get(pk=mouse_id)

    mouse.delete()
    return redirect('store:admin_mouse_view')


def mouse_detail_view(request: HttpRequest , mouse_id :int):
    mouse = Mouse.objects.get(pk=mouse_id)
    comments = Mouse_comment.objects.filter(mouse=mouse)
    mouses = Mouse.objects.filter(category=mouse.category).exclude(pk=mouse.id)[0:6]

    return render(request, "store/mouse_detail.html", {"mouse" : mouse , "mouses" : mouses , "comments" : comments })

def update_mouse_view(request: HttpRequest, mouse_id: int):
    mouse = Mouse.objects.get(pk=mouse_id)

    if request.method == "POST":
        mouse.name=request.POST["name"]
        mouse.dpi=request.POST["dpi"]
        mouse.stock=request.POST["stock"]

        mouse.connection_type=request.POST["connection_type"]
        mouse.price=request.POST["price"]
        
        if "image" in request.FILES:
            mouse.image = request.FILES["image"]
        
        mouse.save()
        
        return redirect('store:admin_mouse_view')
    
    return render(request, "store/update_mouse.html", {"mouse": mouse})

def add_chair_view(request: HttpRequest):
    if request.method == "POST":
        new_chair = Chair(
            name=request.POST["name"],
            color=request.POST["color"],
            material=request.POST["material"],
            adjustable=request.POST["adjustable"],
            max_weight=request.POST["max_weight"],
            price=request.POST["price"],
            image=request.FILES["image"],
        )
        new_chair.save()
        return redirect('store:admin_chair_view')

    return render(request, "store/add_chair.html")

def chair_detail_view(request: HttpRequest , chair_id :int):
    chair = Chair.objects.get(pk=chair_id)
    comments = Chair_comment.objects.filter(chair=chair)
    chairs = Chair.objects.filter(category=chair.category).exclude(pk=chair.id)[0:6]

    return render(request, "store/chair_detail.html", {"chair" : chair ,"chairs" : chairs , "comments" : comments})

def delete_chair_view(request: HttpRequest , chair_id: int):

    chair = Chair.objects.get(pk=chair_id)

    chair.delete()
    return redirect('store:admin_chair_view')

def update_chair_view(request: HttpRequest, chair_id: int):
    chair = Chair.objects.get( pk=chair_id)

    if request.method == "POST":
        chair.name = request.POST["name"]
        chair.color = request.POST["color"]
        chair.material = request.POST["material"]
        chair.adjustable = request.POST["adjustable"]
        chair.max_weight = request.POST["max_weight"]
        chair.stock=request.POST["stock"]

        chair.price = request.POST["price"]

        if "image" in request.FILES:
            chair.image = request.FILES["image"]

        chair.save()
        return redirect('store:admin_chair_view')

    return render(request, "store/update_chair.html", {"chair": chair})

def add_headset_view(request: HttpRequest):
    
    if request.method == "POST":
        new_headset = Headset(
            name=request.POST["name"],
            connection_type=request.POST["connection_type"],
            has_microphone=request.POST["has_microphone"],
            price=request.POST["price"],
            image=request.FILES["image"],
        )
        new_headset.save()
        return redirect('store:admin_headset_view')
    
    return render(request, "store/add_headset.html")

def headset_detail_view(request: HttpRequest , headset_id :int):
    headset = Headset.objects.get(pk=headset_id)
    comments = Headset_comment.objects.filter(headset=headset)
    headsets = Headset.objects.filter(category=headset.category).exclude(pk=headset.id)[0:6]

    return render(request, "store/headset_detail.html", {"headset" : headset ,"headsets" : headsets , "comments" : comments })

def delete_headset_view(request: HttpRequest , headset_id :int):

    headset = Headset.objects.get(pk=headset_id)

    headset.delete()
    return redirect('store:admin_headset_view')




def update_headset_view(request: HttpRequest, headset_id: int):
    headset = Headset.objects.get( pk=headset_id)

    if request.method == "POST":
        headset.name = request.POST["name"]
        headset.connection_type = request.POST["connection_type"]
        headset.has_microphone = request.POST["has_microphone"]
        headset.stock=request.POST["stock"]

        headset.price = request.POST["price"]

        if "image" in request.FILES:
            headset.image = request.FILES["image"]

        headset.save()
        return redirect('store:admin_headset_view')

    return render(request, "store/update_headset.html", {"headset": headset})

def add_keyboard_view(request: HttpRequest):
    if request.method == "POST":
        new_keyboard = Keyboard(
            name=request.POST["name"],
            type=request.POST["type"],
            language=request.POST["language"],
            price=request.POST["price"],
            image=request.FILES["image"],
        )
        new_keyboard.save()
        return redirect('store:admin_keyboard_view')
    
    return render(request, "store/add_keyboard.html")

def update_keyboard_view(request: HttpRequest, keyboard_id: int):
    keyboard = Keyboard.objects.get(pk=keyboard_id)
  

    if request.method == "POST":
        keyboard.name = request.POST["name"]
        keyboard.type = request.POST["type"]
        keyboard.language = request.POST["language"]
        keyboard.stock=request.POST["stock"]

        keyboard.price = request.POST["price"]

        if "image" in request.FILES:
            keyboard.image = request.FILES["image"]


        keyboard.save()
        return redirect('store:admin_keyboard_view' )

    return render(request, "store/update_keyboard.html", {"keyboard": keyboard})

def delete_keyboard_view(request: HttpRequest , keyboard_id :int):

    keyboard = Keyboard.objects.get(pk=keyboard_id)

    keyboard.delete()
    return redirect('store:admin_keyboard_view')


def keyboard_detail_view(request: HttpRequest , keyboard_id :int):
    keyboard = Keyboard.objects.get(pk=keyboard_id)
    comments = Keyboard_comment.objects.filter(keyboard=keyboard)
    keyboards = Keyboard.objects.filter(category=keyboard.category).exclude(pk=keyboard.id)[0:6]

    return render(request, "store/keyboard_detail.html", {"keyboard" : keyboard ,"keyboards" : keyboards , "comments" : comments })

def search_view(request):
    category = request.GET.get("category", "all")
    search_query = request.GET.get("search", "")

    pcs = monitors = mouses = chairs = headsets = keyboards = []

    if category == "all":
        if search_query:
            pcs = PC.objects.filter(name__icontains=search_query)
            monitors = Monitor.objects.filter(name__icontains=search_query)
            mouses = Mouse.objects.filter(name__icontains=search_query)
            chairs = Chair.objects.filter(name__icontains=search_query)
            headsets = Headset.objects.filter(name__icontains=search_query)
            keyboards = Keyboard.objects.filter(name__icontains=search_query)
        else:
            pcs = PC.objects.all()
            monitors = Monitor.objects.all()
            mouses = Mouse.objects.all()
            chairs = Chair.objects.all()
            headsets = Headset.objects.all()
            keyboards = Keyboard.objects.all()

    elif category == "pc":
        pcs = PC.objects.filter(name__icontains=search_query) if search_query else PC.objects.all()

    elif category == "monitor":
        monitors = Monitor.objects.filter(name__icontains=search_query) if search_query else Monitor.objects.all()

    elif category == "mouse":
        mouses = Mouse.objects.filter(name__icontains=search_query) if search_query else Mouse.objects.all()

    elif category == "chair":
        chairs = Chair.objects.filter(name__icontains=search_query) if search_query else Chair.objects.all()

    elif category == "headset":
        headsets = Headset.objects.filter(name__icontains=search_query) if search_query else Headset.objects.all()

    elif category == "keyboard":
        keyboards = Keyboard.objects.filter(name__icontains=search_query) if search_query else Keyboard.objects.all()

    return render(request, "store/search.html", {
        "pcs": pcs,
        "monitors": monitors,
        "mouses": mouses,
        "chairs": chairs,
        "headsets": headsets,
        "keyboards": keyboards,
        "category": category,
        "search_query": search_query,
    })



def pc_comment_view(request: HttpRequest , pc_id: int ):
    pc = PC.objects.get(pk=pc_id)

    if request.method == "POST":

        new_comment = PC_comment(
                pc = pc, #pc from db = pc object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:pc_detail_view" , pc_id = pc_id)
    
def monitor_comment_view(request: HttpRequest , monitor_id: int ):
    monitor = Monitor.objects.get(pk=monitor_id)

    if request.method == "POST":

        new_comment = Monitor_comment(
                monitor =  monitor, #monitor from db = monitor object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:monitor_detail_view" , monitor_id = monitor_id)
    

def headset_comment_view(request: HttpRequest , headset_id: int ):
    headset = Headset.objects.get(pk=headset_id)

    if request.method == "POST":

        new_comment = Headset_comment(
                headset =  headset, #headset from db = headset object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:headset_detail_view" , headset_id = headset_id)
    

def mouse_comment_view(request: HttpRequest , mouse_id: int ):
    mouse = Mouse.objects.get(pk=mouse_id)

    if request.method == "POST":

        new_comment = Mouse_comment(
                mouse =  mouse, #mouse from db = mouse object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:mouse_detail_view" , mouse_id = mouse_id)
    

def keyboard_comment_view(request: HttpRequest , keyboard_id: int ):
    keyboard = Keyboard.objects.get(pk=keyboard_id)

    if request.method == "POST":

        new_comment = Keyboard_comment(
                keyboard =  keyboard, #keyboard from db = keyboard object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:keyboard_detail_view" , keyboard_id = keyboard_id)


def chair_comment_view(request: HttpRequest , chair_id: int ):
    chair = Chair.objects.get(pk=chair_id)

    if request.method == "POST":

        new_comment = Chair_comment(
                chair =  chair, #chair from db = chair object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:chair_detail_view" , chair_id = chair_id)
   
def admin_pc_view(request):
    pcs = PC.objects.all()
    return render(request, 'store/pcs_admin.html', {'pcs': pcs})

def admin_monitor_view(request):
    monitors = Monitor.objects.all()
    return render(request, 'store/monitors_admin.html', {'monitors': monitors})

def admin_mouse_view(request):
    mouses = Mouse.objects.all()
    return render(request, 'store/mouses_admin.html', {'mouses': mouses})

def admin_headset_view(request):
    headsets = Headset.objects.all()
    return render(request, 'store/headsets_admin.html', {'headsets': headsets})

def admin_keyboard_view(request):
    keyboards = Keyboard.objects.all()
    return render(request, 'store/keyboards_admin.html', {'keyboards': keyboards})

def admin_chair_view(request):
    chairs = Chair.objects.all()
    return render(request, 'store/chairs_admin.html', {'chairs': chairs})


MODEL_MAP = {
    "PC": PC,
    "Monitor": Monitor,
    "Keyboard": Keyboard,
    "Mouse": Mouse,
    "Headset": Headset,
    "Chair": Chair,
}

def add_to_cart(request, category, product_id):
    model = MODEL_MAP.get(category)
    if not model:
        return redirect('store:cart_view')

    try:
        product = model.objects.get(pk=product_id)
    except model.DoesNotExist:
        messages.error(request, "Product not found.")
        return redirect('store:cart_view')

    cart = request.session.get('cart', {})
    current_quantity = cart.get(category, {}).get(str(product_id), 0)

    if product.stock > current_quantity:
        cart.setdefault(category, {})[str(product_id)] = current_quantity + 1
        request.session['cart'] = cart
    else:
        messages.error(request, f"Only {product.stock} of {product.name} available in stock.")

    return redirect('store:cart_view')

def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total_price = 0

    for category, products in cart.items():
        model = MODEL_MAP.get(category)
        if not model:
            continue
        for product_id, quantity in products.items():
            product = model.objects.get(pk=product_id)
            subtotal = product.price * quantity
            items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
                'category': category,
            })
            total_price += subtotal

    return render(request, 'store/cart.html', {
        'items': items,
        'total_price': total_price
    })
    
def remove_from_cart(request, category, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if category in cart and product_id in cart[category]:
        del cart[category][product_id]
        if not cart[category]:  
            del cart[category]

    request.session['cart'] = cart
    return redirect('store:cart_view')

def checkout_view(request):
    return render(request, 'store/checkout.html')


def process_payment(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        for category, products in cart.items():
            model = MODEL_MAP.get(category)
            if not model:
                continue

            for product_id, quantity in products.items():
                try:
                    product = model.objects.get(pk=product_id)

                    if product.stock >= quantity:
                        product.stock -= quantity
                        product.save()
                    else:
                        messages.error(request, f"Not enough stock for {product.name}")
                        return redirect('store:cart_view')

                except model.DoesNotExist:
                    messages.error(request, f"Product not found in category {category}")
                    return redirect('store:cart_view')

        request.session['cart'] = {}
        return redirect('store:payment_success')

    return redirect('store:cart_view')

def payment_success(request):
    return render(request, 'store/payment_success.html')


def update_cart_quantity(request, category, product_id):
    if request.method == 'POST':
        change = int(request.POST.get('change', 0))  

        cart = request.session.get('cart', {})
        product_id = str(product_id)

        if category in cart and product_id in cart[category]:
            current_quantity = cart[category][product_id]
            new_quantity = current_quantity + change

            if new_quantity < 1:
                return redirect('store:remove_from_cart', category=category, product_id=product_id)

            cart[category][product_id] = new_quantity
            request.session['cart'] = cart

    return redirect('store:cart_view')

from django.shortcuts import render
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect

from django.shortcuts import render, redirect

def ask_view(request):
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    if request.method == 'POST':
        question = request.POST.get('question', '').strip()
        normalized_q = question.lower()

        responses = [
            (["ram", "memory"], 
             "RAM (Random Access Memory) helps your PC run multiple tasks smoothly. "
             "16GB is ideal for most users, while 32GB is better for gaming or editing."),

            (["ssd", "solid state"], 
             "An SSD (Solid State Drive) is fast storage for booting and loading files quickly. "
             "NVMe SSDs like the Samsung 970 EVO or WD Black SN850 are top choices."),

            (["gpu", "graphics card"], 
             "A GPU (Graphics Processing Unit) handles visuals and gaming graphics. "
             "Best options include NVIDIA RTX 4060–4080 or AMD RX 6700–7900 series."),

            (["cpu", "processor"], 
             "The CPU (Central Processing Unit) is your computer’s brain. "
             "Intel i5/i7 or AMD Ryzen 5/7 (latest gen) provide excellent performance."),

            (["storage"], 
             "Storage saves your data and files. "
             "A 1TB SSD is a good mix of speed and capacity for most users."),

            (["gaming pc", "best pc for gaming", "pc build"], 
             "A powerful gaming PC includes a strong GPU, fast CPU, and SSD. "
             "Ideal setup: RTX 4070+, 16GB+ RAM, Ryzen 7 or i7 CPU, 1TB NVMe SSD."),

            (["overclock"], 
             "Overclocking boosts your CPU/GPU performance by increasing speed. "
             "Use proper cooling and compatible motherboards (Z-series or X-series)."),

            (["cooling", "fan", "temperature"], 
             "PC cooling keeps your components from overheating. "
             "Good options include air coolers (Noctua NH-D15) or liquid AIO coolers (NZXT Kraken)."),

            (["psu", "power supply"], 
             "The PSU delivers power to your PC parts. "
             "Get an 80+ Bronze or better PSU with 650–750W for gaming PCs."),

            (["monitor"], 
             "Monitors display your PC output. "
             "For gaming, 24–27 inch, 144Hz+ refresh rate, and 1ms response are ideal."),

            (["motherboard"], 
             "The motherboard connects all PC components. "
             "Choose one based on CPU compatibility and features (e.g., B650 for Ryzen, Z790 for Intel)."),

            (["mouse"], 
             "A mouse controls your pointer and is essential for navigation. "
             "Best for gaming: Logitech G502 or Razer DeathAdder. Wireless mice are great for productivity."),

            (["keyboard"], 
             "A keyboard lets you type and control your PC. "
             "Mechanical keyboards with RGB (e.g., Keychron, Logitech G) are preferred by gamers and typists."),

            (["headset", "headphones"], 
             "Headsets provide sound and often include microphones. "
             "For gaming, look for over-ear headsets like HyperX Cloud II or SteelSeries Arctis 7."),

            (["chair", "gaming chair"], 
             "Gaming chairs support your back during long sessions. "
             "Top models include Secretlab Titan or Razer Iskur, offering ergonomic design and adjustability."),

            (["pc", "computer"], 
             "A PC (Personal Computer) is a machine for work, study, or gaming. "
             "Choose a PC based on your needs—budget builds for basic use, gaming rigs for performance.")
        ]

        answer = "Sorry, I don't have an answer for that yet. Try asking about RAM, SSD, GPU, mouse, or gaming chairs."

        for keywords, response in responses:
            if any(keyword in normalized_q for keyword in keywords):
                answer = response
                break

        request.session['chat_history'].append({'question': question, 'answer': answer})
        request.session.modified = True
        return redirect('store:ask_view')

    return render(request, 'store/asks.html', {
        'chat_history': request.session.get('chat_history', [])
    })
