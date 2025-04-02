// Delete everything first (if needed)
MATCH (n) DETACH DELETE n;

// --- PRODUCTS ---
CREATE (p1:Product {name: "Physical Product"})
CREATE (p2:Product {name: "Digital Product"})

// --- TOPICS ---
CREATE (t1:Topic {name: "Returns"})
CREATE (t2:Topic {name: "Shipping"})
CREATE (t3:Topic {name: "Refunds"})
CREATE (t4:Topic {name: "Orders"})
CREATE (t5:Topic {name: "Account"})
CREATE (t6:Topic {name: "Payments"})
CREATE (t7:Topic {name: "Delivery"})
CREATE (t8:Topic {name: "Security"})
CREATE (t9:Topic {name: "Subscriptions"})

// --- POLICIES ---
CREATE (rp:Policy {name: "Return Policy", details: "Products can be returned within 30 days. Refunds take 5-7 business days."})
CREATE (sp:Policy {name: "Shipping Zones", details: "Shipping available in US, EU, and Canada. Customs may apply."})
CREATE (rf:Policy {name: "Refund Timeline", details: "Refunds are issued 5-7 days after return is received."})
CREATE (pp:Policy {name: "Payment Policy", details: "We accept Visa, Mastercard, and PayPal. Refunds go to the original method."})
CREATE (dp:Policy {name: "Delivery Guarantee", details: "Orders are delivered in 3–5 business days. Delays are notified."})
CREATE (ap:Policy {name: "Account Policy", details: "You must register with a valid email. Keep your account secure."})
CREATE (sp2:Policy {name: "Subscription Policy", details: "Subscriptions renew monthly. Cancel anytime from your dashboard."})

// --- ACTIONS ---
CREATE (a1:Action {name: "Request Return"})
CREATE (a2:Action {name: "Track Order"})
CREATE (a3:Action {name: "Reset Password"})
CREATE (a4:Action {name: "Update Payment Info"})
CREATE (a5:Action {name: "Cancel Subscription"})
CREATE (a6:Action {name: "Report Fraud"})

// --- CHANNELS ---
CREATE (c1:Channel {name: "Email"})
CREATE (c2:Channel {name: "Live Chat"})
CREATE (c3:Channel {name: "Phone"})

// --- RELATIONSHIPS ---
// Returns
CREATE (t1)-[:COVERS]->(rp)
CREATE (t1)-[:RELATED_TO]->(t3)
CREATE (t1)-[:CONTACT_VIA]->(c1)
CREATE (t1)-[:CONTACT_VIA]->(c2)
CREATE (rp)-[:ALLOWS]->(a1)
CREATE (rp)-[:APPLIES_TO]->(p1)

// Refunds
CREATE (t3)-[:COVERS]->(rf)
CREATE (t3)-[:CONTACT_VIA]->(c1)
CREATE (rf)-[:ALLOWS]->(a1)

// Shipping
CREATE (t2)-[:COVERS]->(sp)
CREATE (t2)-[:RELATED_TO]->(t7)
CREATE (t2)-[:CONTACT_VIA]->(c2)

// Orders
CREATE (t4)-[:ALLOWS]->(a2)
CREATE (t4)-[:RELATED_TO]->(t2)

// Account
CREATE (t5)-[:ALLOWS]->(a3)
CREATE (t5)-[:COVERS]->(ap)
CREATE (t5)-[:CONTACT_VIA]->(c1)
CREATE (t5)-[:RELATED_TO]->(t8)

// Payments
CREATE (t6)-[:COVERS]->(pp)
CREATE (pp)-[:ALLOWS]->(a4)
CREATE (t6)-[:CONTACT_VIA]->(c2)
CREATE (t6)-[:RELATED_TO]->(t3)

// Subscriptions
CREATE (t9)-[:COVERS]->(sp2)
CREATE (sp2)-[:ALLOWS]->(a5)
CREATE (t9)-[:RELATED_TO]->(t6)

// Security
CREATE (t8)-[:ALLOWS]->(a6)
CREATE (t8)-[:CONTACT_VIA]->(c3)