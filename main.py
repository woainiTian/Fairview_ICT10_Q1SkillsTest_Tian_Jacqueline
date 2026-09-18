from pyscript import document, display

def order(e):
    document.getElementById("subtotal").innerHTML = ""
    OrchO = 500
    BreadB = 450
    PickP = 420
    LoveL = 400

    OrchO_checked = document.getElementById("1").checked
    BreadB_checked = document.getElementById("2").checked
    PickP_checked = document.getElementById("3").checked
    LoveL_checked = document.getElementById("4").checked

    subtotal = OrchO * OrchO_checked + BreadB * BreadB_checked + PickP * PickP_checked + LoveL * LoveL_checked 
    vat = subtotal * 0.12
    total = subtotal - vat


    document.getElementById("subtotal").innerText = f"₱{subtotal:.2f}"
    document.getElementById("VAT").innerText = f"₱{vat:.2f}"
    document.getElementById("total").innerText = f"₱{total:.2f}"