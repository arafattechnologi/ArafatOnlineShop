export default async function handler(req, res) {
    // Waxaan u oggolaaneynaa dukaankaaga oo kaliya inuu u soo diro codsiga
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    if (req.method === 'OPTIONS') {
        return res.status(200).end();
    }

    if (req.method !== 'POST') {
        return res.status(405).json({ message: 'Kaliya POST request ayaa loo oggol yahay' });
    }

    try {
        // Halkan waxaan codsiga si toos ah ugu tuureynaa server-ka WaafiPay (CORS halkan ma qabato)
        const waafiResponse = await fetch("https://api.waafipay.net/asm", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(req.body)
        });

        const data = await waafiResponse.json();
        return res.status(200).json(data);
    } catch (error) {
        return res.status(500).json({ error: "Xiriirka server-ka Waafi API waa go'an yahay" });
    }
}


// Qaybta kaydinta badeecadaha ee localStorage
function saveProduct(productName, productPrice) {
    let products = JSON.parse(localStorage.getItem('arafat_products')) || [];
    products.push({ name: productName, price: productPrice });
    localStorage.setItem('arafat_products', JSON.stringify(products));
    alert('Badeecaddu si guul leh ayay u kaydisay!');
}

function loadProducts() {
    let products = JSON.parse(localStorage.getItem('arafat_products')) || [];
    products.forEach(item => {
        console.log(item.name + ' - ' + item.price);
    });
}

