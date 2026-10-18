"""Generates the legal pages in English (root), Dutch (nl/) and French (fr/)."""
import sys, os
root = sys.argv[1]
L = lambda k: f'<span data-legal="{k}"></span>'
S = lambda k: f'<span data-store="{k}"></span>'
PAGES = ['terms', 'returns', 'shipping', 'privacy', 'contact']

UI = {
 'en': dict(back='← Back to the shop', nav=['Terms &amp; conditions','Returns &amp; withdrawal','Shipping','Privacy','Contact'], rights='All rights reserved.'),
 'nl': dict(back='← Terug naar de winkel', nav=['Algemene voorwaarden','Retourneren &amp; herroeping','Verzending','Privacy','Contact'], rights='Alle rechten voorbehouden.'),
 'fr': dict(back='← Retour à la boutique', nav=['Conditions générales','Retours &amp; rétractation','Livraison','Confidentialité','Contact'], rights='Tous droits réservés.'),
}

def seller(lang):
    w = {'en': ('enterprise number','VAT number','email','phone'),
         'nl': ('ondernemingsnummer','btw-nummer','e-mail','telefoon'),
         'fr': ("numéro d'entreprise",'numéro de TVA','e-mail','téléphone')}[lang]
    return f'{L("businessName")}, {L("address")}, {w[0]} {L("enterpriseNumber")}, {w[1]} {L("vatNumber")}, {w[2]} {L("email")}, {w[3]} {L("phone")}'

C = {}
# ---------------------------------------------------------------- English
C['en'] = {
'terms': ('Terms and conditions', 'These terms apply to every order placed on this website by a consumer. Last updated: <span data-store="updated"></span>.', f'''
    <h2>1. Who we are</h2>
    <p>This shop is run by {seller('en')}.</p>
    <h2>2. Products and prices</h2>
    <p>We describe and photograph our products as accurately as we can. Colours on screen can differ slightly from the real item. Each product page shows its material, care instructions and manufacturer.</p>
    <p>Prices are in euros. <span data-vat-text></span> Delivery costs are shown in the cart and on the payment page before you pay: {S("shippingFee")} per order, free for orders of {S("freeShippingThreshold")} or more.</p>
    <h2>3. Your order and the contract</h2>
    <p>The contract is concluded when your payment is confirmed. You receive a confirmation and receipt by email. If an item turns out to be unavailable after you paid, we tell you as soon as possible and refund that item in full within 14 days.</p>
    <h2>4. Payment</h2>
    <p>Payments are processed by Stripe. You can pay with Bancontact, iDEAL/Wero, credit or debit card, Apple Pay or Google Pay. We never see or store your full card details.</p>
    <h2>5. Delivery</h2>
    <p>We deliver to Belgium and the Netherlands. Delivery usually takes 2 to 6 business days; see our <a href="shipping.html">shipping page</a>. If we cannot deliver within 30 days of your order, you may cancel the order and receive a full refund. The risk of loss or damage passes to you when you or a person you named receive the parcel.</p>
    <h2>6. Right of withdrawal (14 days)</h2>
    <p>You can withdraw from your purchase without giving a reason within 14 days of the day you received the goods. How this works, and the model withdrawal form, are on our <a href="returns.html">returns page</a>.</p>
    <h2>7. Legal guarantee</h2>
    <p>All products come with the legal guarantee of conformity of two years from delivery. If an item is faulty or does not match its description, we repair or replace it, or, if that is not possible, give you a price reduction or a refund. Please tell us within two months of noticing the defect. Normal wear and tear and damage from incorrect use or washing are not covered.</p>
    <h2>8. Liability</h2>
    <p>Nothing in these terms limits your rights as a consumer under mandatory law.</p>
    <h2>9. Complaints and disputes</h2>
    <p>Contact us first at {L("email")}; we reply within 2 business days. If we cannot solve the problem together, you can contact the Consumer Mediation Service (Consumentenombudsdienst / Service de Médiation pour le Consommateur) at <a href="https://www.consumentenombudsdienst.be" rel="noopener">consumentenombudsdienst.be</a>.</p>
    <h2>10. Applicable law</h2>
    <p>These terms are governed by Belgian law. If you live in another EU country, you keep the protection of the mandatory consumer law of that country.</p>
    <h2>11. Personal data</h2>
    <p>How we use your data is explained in our <a href="privacy.html">privacy policy</a>.</p>
'''),
'returns': ('Returns and right of withdrawal', 'You have 14 days to change your mind. Here is how to return an item and get your money back.', f'''
    <h2>Your right of withdrawal</h2>
    <p>You have the right to withdraw from this contract within 14 days without giving any reason. The withdrawal period ends 14 days after the day you, or a person you named (other than the carrier), receive the goods. If you ordered several items that arrive separately, the period starts when you receive the last item.</p>
    <p>To withdraw, tell us clearly before the period ends, for example by email to {L("email")} or by letter to {L("address")}. You may use the model form below, but you don't have to.</p>
    <h2>How to return</h2>
    <ol>
      <li>Email us your order number and the items you want to return. We reply with the return address.</li>
      <li>Send the items back within 14 days of telling us. Pack them carefully, unworn, with labels attached.</li>
      <li>You pay the direct cost of returning the goods, unless the item is faulty or we sent the wrong item.</li>
    </ol>
    <h2>Your refund</h2>
    <p>We refund all payments we received from you, including the standard delivery cost, within 14 days of the day you told us you are withdrawing. We use the same payment method you used, at no cost to you. We may wait with the refund until we have received the goods back, or until you show proof that you sent them, whichever comes first.</p>
    <p>You may handle the items as you would in a shop to check them. If an item is worn, washed or damaged beyond that, we may deduct the loss in value from the refund.</p>
    <h2>Items that cannot be returned once opened</h2>
    <p>For hygiene reasons, socks and base layers that were delivered sealed cannot be returned once the seal has been removed.</p>
    <h2>Faulty or wrong item?</h2>
    <p>Email us a photo within two months of noticing the problem. We cover the return cost and repair, replace or refund the item under the legal guarantee.</p>
    <h2>Model withdrawal form</h2>
    <div class="form-box">
      <p>(Complete and return this form only if you wish to withdraw from the contract.)</p>
      <p>To: {L("businessName")}, {L("address")}, {L("email")}</p>
      <p>I/We (*) hereby give notice that I/We (*) withdraw from my/our (*) contract of sale of the following goods (*):</p>
      <p>Ordered on (*) / received on (*):</p>
      <p>Name of consumer(s):</p>
      <p>Address of consumer(s):</p>
      <p>Signature of consumer(s) (only if this form is sent on paper):</p>
      <p>Date:</p>
      <p>(*) Delete as appropriate.</p>
    </div>
'''),
'shipping': ('Shipping', 'We ship to Belgium and the Netherlands from warehouses inside the EU, so there are no customs fees.', f'''
    <table class="info-table">
      <tr><th>Countries</th><td>Belgium, the Netherlands</td></tr>
      <tr><th>Cost</th><td>{S("shippingFee")} per order, free from {S("freeShippingThreshold")}</td></tr>
      <tr><th>Delivery time</th><td>Usually 2 to 6 business days after payment</td></tr>
      <tr><th>Tracking</th><td>You receive a tracking link by email once your order ships</td></tr>
      <tr><th>Customs and import fees</th><td>None: all orders ship from within the EU</td></tr>
    </table>
    <h2>Good to know</h2>
    <ul>
      <li>If you order several items, they may arrive in separate parcels. You never pay extra for that.</li>
      <li>Delivery times are estimates. Around Black Friday and the December holidays they can be a few days longer.</li>
      <li>If your parcel has not arrived after 10 business days, or tracking has not changed for 5 days, email us at {L("email")} and we will look into it.</li>
      <li>Check your address on the payment page carefully. If a parcel is returned because of a wrong address, we can re-send it at cost.</li>
    </ul>
'''),
'privacy': ('Privacy policy', 'This policy explains what personal data we collect, why, and what your rights are under the GDPR. Last updated: <span data-store="updated"></span>.', f'''
    <h2>Who is responsible for your data</h2>
    <p>The controller is {seller('en')}.</p>
    <h2>What we collect and why</h2>
    <table class="info-table">
      <tr><th>Data</th><th>Why</th><th>Legal basis</th><th>How long we keep it</th></tr>
      <tr><td>Name, delivery address, email, phone, order details</td><td>To process, deliver and support your order</td><td>Performance of the contract</td><td>10 years (Belgian accounting obligations)</td></tr>
      <tr><td>Payment data</td><td>To take payment; handled by Stripe, we never see your full card details</td><td>Performance of the contract</td><td>As required by Stripe and accounting law</td></tr>
      <tr><td>Email address (newsletter)</td><td>To tell you about new collections</td><td>Your consent</td><td>Until you unsubscribe</td></tr>
      <tr><td>Emails you send us</td><td>To answer your questions and complaints</td><td>Our legitimate interest in helping you</td><td>Up to 2 years after the last contact</td></tr>
    </table>
    <h2>Who we share it with</h2>
    <ul>
      <li><strong>Stripe</strong> (payments).</li>
      <li><strong>Netlify</strong> (website hosting and newsletter sign-ups).</li>
      <li><strong>Our fulfilment partner</strong>, which packs and ships your order and receives your name, delivery address and phone number for that purpose only.</li>
      <li>Delivery companies, to deliver your parcel.</li>
    </ul>
    <p>Some of these providers are based outside the European Economic Area; transfers are covered by the European Commission's standard contractual clauses or another legal safeguard. We never sell your data.</p>
    <h2>Cookies and storage</h2>
    <p>We do not use tracking or advertising cookies. Your shopping cart is saved in your own browser (local storage) so it is still there when you come back; it never leaves your device until you check out. Stripe uses cookies that are needed for secure payment and fraud prevention on its payment page.</p>
    <h2>Your rights</h2>
    <p>You can ask to see, correct or delete your data, to restrict or object to its use, and to receive it in a portable format. You can withdraw your newsletter consent at any time. Email {L("email")}; we answer within one month.</p>
    <p>If you are not satisfied, you can complain to the Belgian Data Protection Authority (Gegevensbeschermingsautoriteit / Autorité de protection des données) at <a href="https://www.dataprotectionauthority.be" rel="noopener">dataprotectionauthority.be</a>.</p>
'''),
'contact': ('Contact', 'Questions about an order, a return or a product? We answer within 2 business days.', f'''
    <table class="info-table">
      <tr><th>Email</th><td>{L("email")}</td></tr>
      <tr><th>Phone</th><td>{L("phone")}</td></tr>
      <tr><th>Address</th><td>{L("address")}</td></tr>
      <tr><th>Business name</th><td>{L("businessName")}</td></tr>
      <tr><th>Enterprise number</th><td>{L("enterpriseNumber")}</td></tr>
      <tr><th>VAT number</th><td>{L("vatNumber")}</td></tr>
    </table>
    <p>Please include your order number when you write about an order. Returns are explained on the <a href="returns.html">returns page</a>.</p>
'''),
}
# ---------------------------------------------------------------- Dutch
C['nl'] = {
'terms': ('Algemene voorwaarden', 'Deze voorwaarden gelden voor elke bestelling die een consument op deze website plaatst. Laatst bijgewerkt: <span data-store="updated"></span>.', f'''
    <h2>1. Wie we zijn</h2>
    <p>Deze webwinkel wordt uitgebaat door {seller('nl')}.</p>
    <h2>2. Producten en prijzen</h2>
    <p>We beschrijven en fotograferen onze producten zo nauwkeurig mogelijk. Kleuren op een scherm kunnen licht afwijken van het echte product. Elke productpagina vermeldt het materiaal, de wasvoorschriften en de fabrikant.</p>
    <p>Prijzen zijn in euro. <span data-vat-text></span> De verzendkosten zie je in het winkelmandje en op de betaalpagina voordat je betaalt: {S("shippingFee")} per bestelling, gratis vanaf {S("freeShippingThreshold")}.</p>
    <h2>3. Je bestelling en de overeenkomst</h2>
    <p>De overeenkomst komt tot stand zodra je betaling bevestigd is. Je ontvangt een bevestiging en een betaalbewijs per e-mail. Blijkt een artikel na je betaling toch niet beschikbaar, dan laten we je dat zo snel mogelijk weten en betalen we dat artikel binnen 14 dagen volledig terug.</p>
    <h2>4. Betaling</h2>
    <p>Betalingen worden verwerkt door Stripe. Je kunt betalen met Bancontact, iDEAL/Wero, krediet- of debetkaart, Apple Pay of Google Pay. Wij zien of bewaren nooit je volledige kaartgegevens.</p>
    <h2>5. Levering</h2>
    <p>We leveren in België en Nederland. Levering duurt meestal 2 tot 6 werkdagen; zie onze <a href="shipping.html">verzendpagina</a>. Kunnen we niet binnen 30 dagen na je bestelling leveren, dan mag je de bestelling annuleren en krijg je je geld volledig terug. Het risico op verlies of beschadiging gaat op jou over wanneer jij of een door jou aangewezen persoon het pakket ontvangt.</p>
    <h2>6. Herroepingsrecht (14 dagen)</h2>
    <p>Je kunt je aankoop zonder opgave van redenen herroepen binnen 14 dagen na de dag waarop je de goederen ontving. Hoe dat werkt, en het modelformulier voor herroeping, vind je op onze <a href="returns.html">retourpagina</a>.</p>
    <h2>7. Wettelijke garantie</h2>
    <p>Op alle producten geldt de wettelijke garantie van overeenstemming van twee jaar vanaf de levering. Is een artikel defect of komt het niet overeen met de beschrijving, dan herstellen of vervangen we het, of, als dat niet mogelijk is, krijg je een prijsvermindering of terugbetaling. Meld het gebrek binnen twee maanden nadat je het vaststelde. Normale slijtage en schade door verkeerd gebruik of verkeerd wassen vallen niet onder de garantie.</p>
    <h2>8. Aansprakelijkheid</h2>
    <p>Niets in deze voorwaarden beperkt je rechten als consument volgens de dwingende wetgeving.</p>
    <h2>9. Klachten en geschillen</h2>
    <p>Neem eerst contact met ons op via {L("email")}; we antwoorden binnen 2 werkdagen. Komen we samen niet tot een oplossing, dan kun je terecht bij de Consumentenombudsdienst via <a href="https://www.consumentenombudsdienst.be" rel="noopener">consumentenombudsdienst.be</a>.</p>
    <h2>10. Toepasselijk recht</h2>
    <p>Op deze voorwaarden is het Belgische recht van toepassing. Woon je in een ander EU-land, dan behoud je de bescherming van het dwingende consumentenrecht van dat land.</p>
    <h2>11. Persoonsgegevens</h2>
    <p>Hoe we je gegevens gebruiken, lees je in onze <a href="privacy.html">privacyverklaring</a>.</p>
'''),
'returns': ('Retourneren en herroepingsrecht', 'Je hebt 14 dagen bedenktijd. Zo stuur je een artikel terug en krijg je je geld terug.', f'''
    <h2>Je herroepingsrecht</h2>
    <p>Je hebt het recht om binnen 14 dagen zonder opgave van redenen deze overeenkomst te herroepen. De herroepingstermijn verstrijkt 14 dagen na de dag waarop jij, of een door jou aangewezen persoon (niet de vervoerder), de goederen ontvangt. Bestel je meerdere artikelen die apart aankomen, dan begint de termijn wanneer je het laatste artikel ontvangt.</p>
    <p>Om te herroepen laat je ons dat vóór het einde van de termijn duidelijk weten, bijvoorbeeld per e-mail naar {L("email")} of per brief naar {L("address")}. Je mag het modelformulier hieronder gebruiken, maar dat hoeft niet.</p>
    <h2>Zo stuur je terug</h2>
    <ol>
      <li>Mail ons je bestelnummer en de artikelen die je wilt terugsturen. We antwoorden met het retouradres.</li>
      <li>Stuur de artikelen binnen 14 dagen nadat je ons dat liet weten terug. Verpak ze zorgvuldig, ongedragen en met de labels eraan.</li>
      <li>De rechtstreekse kosten van het terugsturen zijn voor jou, tenzij het artikel defect is of we het verkeerde artikel stuurden.</li>
    </ol>
    <h2>Je terugbetaling</h2>
    <p>We betalen alle betalingen die we van je ontvingen terug, inclusief de standaard verzendkosten, binnen 14 dagen na de dag waarop je ons liet weten dat je herroept. We gebruiken hetzelfde betaalmiddel als jij, zonder kosten voor jou. We mogen wachten met terugbetalen tot we de goederen terug hebben, of tot je aantoont dat je ze verstuurd hebt, al naargelang wat eerst gebeurt.</p>
    <p>Je mag de artikelen behandelen zoals je dat in een winkel zou doen om ze te bekijken. Is een artikel daarbuiten gedragen, gewassen of beschadigd, dan mogen we de waardevermindering van de terugbetaling aftrekken.</p>
    <h2>Artikelen die na opening niet terug kunnen</h2>
    <p>Om hygiënische redenen kunnen sokken en thermisch ondergoed die verzegeld geleverd werden, niet meer worden teruggestuurd zodra de verzegeling verbroken is.</p>
    <h2>Defect of verkeerd artikel?</h2>
    <p>Mail ons een foto binnen twee maanden nadat je het probleem vaststelde. Wij betalen de retourkosten en herstellen, vervangen of terugbetalen het artikel onder de wettelijke garantie.</p>
    <h2>Modelformulier voor herroeping</h2>
    <div class="form-box">
      <p>(Dit formulier alleen invullen en terugzenden als je de overeenkomst wilt herroepen.)</p>
      <p>Aan: {L("businessName")}, {L("address")}, {L("email")}</p>
      <p>Ik/Wij (*) deel/delen (*) u hierbij mede dat ik/wij (*) onze overeenkomst betreffende de verkoop van de volgende goederen (*) herroep/herroepen (*):</p>
      <p>Besteld op (*) / ontvangen op (*):</p>
      <p>Naam/namen consument(en):</p>
      <p>Adres consument(en):</p>
      <p>Handtekening van consument(en) (alleen wanneer dit formulier op papier wordt ingediend):</p>
      <p>Datum:</p>
      <p>(*) Doorhalen wat niet van toepassing is.</p>
    </div>
'''),
'shipping': ('Verzending', 'We verzenden naar België en Nederland vanuit magazijnen binnen de EU, dus zonder douanekosten.', f'''
    <table class="info-table">
      <tr><th>Landen</th><td>België, Nederland</td></tr>
      <tr><th>Kosten</th><td>{S("shippingFee")} per bestelling, gratis vanaf {S("freeShippingThreshold")}</td></tr>
      <tr><th>Levertijd</th><td>Meestal 2 tot 6 werkdagen na betaling</td></tr>
      <tr><th>Track &amp; trace</th><td>Je ontvangt een trackinglink per e-mail zodra je bestelling verzonden is</td></tr>
      <tr><th>Douane- en invoerkosten</th><td>Geen: alle bestellingen worden verzonden vanuit de EU</td></tr>
    </table>
    <h2>Goed om te weten</h2>
    <ul>
      <li>Bestel je meerdere artikelen, dan kunnen ze in aparte pakketten aankomen. Daarvoor betaal je nooit extra.</li>
      <li>Levertijden zijn schattingen. Rond Black Friday en de feestdagen in december kunnen ze enkele dagen langer zijn.</li>
      <li>Is je pakket na 10 werkdagen nog niet aangekomen, of is de tracking 5 dagen niet veranderd, mail ons dan via {L("email")} en we zoeken het uit.</li>
      <li>Controleer je adres goed op de betaalpagina. Komt een pakket terug door een verkeerd adres, dan kunnen we het opnieuw versturen tegen kostprijs.</li>
    </ul>
'''),
'privacy': ('Privacyverklaring', 'Hier lees je welke persoonsgegevens we verzamelen, waarom, en welke rechten je hebt volgens de AVG (GDPR). Laatst bijgewerkt: <span data-store="updated"></span>.', f'''
    <h2>Wie is verantwoordelijk voor je gegevens</h2>
    <p>De verwerkingsverantwoordelijke is {seller('nl')}.</p>
    <h2>Wat we verzamelen en waarom</h2>
    <table class="info-table">
      <tr><th>Gegevens</th><th>Waarom</th><th>Rechtsgrond</th><th>Hoe lang we ze bewaren</th></tr>
      <tr><td>Naam, leveradres, e-mail, telefoon, bestelgegevens</td><td>Om je bestelling te verwerken, te leveren en je te helpen</td><td>Uitvoering van de overeenkomst</td><td>10 jaar (Belgische boekhoudverplichtingen)</td></tr>
      <tr><td>Betaalgegevens</td><td>Om de betaling te ontvangen; verwerkt door Stripe, wij zien nooit je volledige kaartgegevens</td><td>Uitvoering van de overeenkomst</td><td>Zoals vereist door Stripe en de boekhoudwetgeving</td></tr>
      <tr><td>E-mailadres (nieuwsbrief)</td><td>Om je te laten weten wanneer er nieuwe collecties zijn</td><td>Jouw toestemming</td><td>Tot je je uitschrijft</td></tr>
      <tr><td>E-mails die je ons stuurt</td><td>Om je vragen en klachten te beantwoorden</td><td>Ons gerechtvaardigd belang om je te helpen</td><td>Tot 2 jaar na het laatste contact</td></tr>
    </table>
    <h2>Met wie we ze delen</h2>
    <ul>
      <li><strong>Stripe</strong> (betalingen).</li>
      <li><strong>Netlify</strong> (hosting van de website en inschrijvingen voor de nieuwsbrief).</li>
      <li><strong>Onze fulfilmentpartner</strong>, die je bestelling inpakt en verzendt en daarvoor alleen je naam, leveradres en telefoonnummer ontvangt.</li>
      <li>Bezorgdiensten, om je pakket te leveren.</li>
    </ul>
    <p>Sommige van deze dienstverleners zijn gevestigd buiten de Europese Economische Ruimte; doorgiftes zijn beschermd door de modelcontractbepalingen van de Europese Commissie of een andere wettelijke waarborg. We verkopen je gegevens nooit.</p>
    <h2>Cookies en opslag</h2>
    <p>We gebruiken geen tracking- of advertentiecookies. Je winkelmandje wordt in je eigen browser bewaard (local storage), zodat het er nog is als je terugkomt; het verlaat je toestel pas bij het afrekenen. Stripe gebruikt op zijn betaalpagina cookies die nodig zijn voor veilig betalen en fraudepreventie.</p>
    <h2>Je rechten</h2>
    <p>Je kunt vragen om je gegevens in te zien, te verbeteren of te wissen, het gebruik ervan te beperken of je ertegen te verzetten, en ze in een overdraagbaar formaat te ontvangen. Je kunt je toestemming voor de nieuwsbrief altijd intrekken. Mail naar {L("email")}; we antwoorden binnen een maand.</p>
    <p>Ben je niet tevreden, dan kun je een klacht indienen bij de Gegevensbeschermingsautoriteit via <a href="https://www.gegevensbeschermingsautoriteit.be" rel="noopener">gegevensbeschermingsautoriteit.be</a>.</p>
'''),
'contact': ('Contact', 'Vragen over een bestelling, een retour of een product? We antwoorden binnen 2 werkdagen.', f'''
    <table class="info-table">
      <tr><th>E-mail</th><td>{L("email")}</td></tr>
      <tr><th>Telefoon</th><td>{L("phone")}</td></tr>
      <tr><th>Adres</th><td>{L("address")}</td></tr>
      <tr><th>Handelsnaam</th><td>{L("businessName")}</td></tr>
      <tr><th>Ondernemingsnummer</th><td>{L("enterpriseNumber")}</td></tr>
      <tr><th>Btw-nummer</th><td>{L("vatNumber")}</td></tr>
    </table>
    <p>Vermeld je bestelnummer als je ons over een bestelling schrijft. Hoe retourneren werkt, lees je op de <a href="returns.html">retourpagina</a>.</p>
'''),
}
# ---------------------------------------------------------------- French
C['fr'] = {
'terms': ('Conditions générales de vente', 'Ces conditions s’appliquent à toute commande passée par un consommateur sur ce site. Dernière mise à jour : <span data-store="updated"></span>.', f'''
    <h2>1. Qui sommes-nous</h2>
    <p>Cette boutique est exploitée par {seller('fr')}.</p>
    <h2>2. Produits et prix</h2>
    <p>Nous décrivons et photographions nos produits aussi fidèlement que possible. Les couleurs à l’écran peuvent légèrement différer du produit réel. Chaque fiche produit indique la matière, les conseils d’entretien et le fabricant.</p>
    <p>Les prix sont en euros. <span data-vat-text></span> Les frais de livraison sont affichés dans le panier et sur la page de paiement avant que vous ne payiez : {S("shippingFee")} par commande, gratuits à partir de {S("freeShippingThreshold")}.</p>
    <h2>3. Votre commande et le contrat</h2>
    <p>Le contrat est conclu dès la confirmation de votre paiement. Vous recevez une confirmation et un reçu par e-mail. Si un article s’avère indisponible après votre paiement, nous vous en informons au plus vite et vous remboursons intégralement cet article dans les 14 jours.</p>
    <h2>4. Paiement</h2>
    <p>Les paiements sont traités par Stripe. Vous pouvez payer par Bancontact, iDEAL/Wero, carte de crédit ou de débit, Apple Pay ou Google Pay. Nous ne voyons ni ne conservons jamais vos données de carte complètes.</p>
    <h2>5. Livraison</h2>
    <p>Nous livrons en Belgique et aux Pays-Bas. La livraison prend généralement 2 à 6 jours ouvrables ; voir notre <a href="shipping.html">page livraison</a>. Si nous ne pouvons pas livrer dans les 30 jours suivant votre commande, vous pouvez annuler la commande et être intégralement remboursé. Le risque de perte ou d’endommagement vous est transféré lorsque vous, ou la personne que vous avez désignée, recevez le colis.</p>
    <h2>6. Droit de rétractation (14 jours)</h2>
    <p>Vous pouvez vous rétracter de votre achat sans donner de motif dans les 14 jours suivant le jour où vous avez reçu les biens. Le fonctionnement, ainsi que le formulaire type de rétractation, figurent sur notre <a href="returns.html">page retours</a>.</p>
    <h2>7. Garantie légale</h2>
    <p>Tous les produits bénéficient de la garantie légale de conformité de deux ans à compter de la livraison. Si un article est défectueux ou ne correspond pas à sa description, nous le réparons ou le remplaçons ou, si ce n’est pas possible, vous accordons une réduction de prix ou un remboursement. Merci de nous signaler le défaut dans les deux mois suivant sa constatation. L’usure normale et les dommages dus à une mauvaise utilisation ou à un mauvais lavage ne sont pas couverts.</p>
    <h2>8. Responsabilité</h2>
    <p>Rien dans ces conditions ne limite vos droits de consommateur prévus par la loi impérative.</p>
    <h2>9. Plaintes et litiges</h2>
    <p>Contactez-nous d’abord à {L("email")} ; nous répondons dans les 2 jours ouvrables. Si nous ne trouvons pas de solution ensemble, vous pouvez vous adresser au Service de Médiation pour le Consommateur via <a href="https://www.mediationconsommateur.be" rel="noopener">mediationconsommateur.be</a>.</p>
    <h2>10. Droit applicable</h2>
    <p>Ces conditions sont régies par le droit belge. Si vous résidez dans un autre pays de l’UE, vous conservez la protection du droit impératif de la consommation de ce pays.</p>
    <h2>11. Données personnelles</h2>
    <p>L’utilisation de vos données est expliquée dans notre <a href="privacy.html">politique de confidentialité</a>.</p>
'''),
'returns': ('Retours et droit de rétractation', 'Vous disposez de 14 jours pour changer d’avis. Voici comment renvoyer un article et être remboursé.', f'''
    <h2>Votre droit de rétractation</h2>
    <p>Vous avez le droit de vous rétracter du présent contrat sans donner de motif dans un délai de 14 jours. Le délai de rétractation expire 14 jours après le jour où vous-même, ou un tiers autre que le transporteur et désigné par vous, prenez physiquement possession des biens. Si vous avez commandé plusieurs articles livrés séparément, le délai court à partir de la réception du dernier article.</p>
    <p>Pour vous rétracter, informez-nous clairement avant la fin du délai, par exemple par e-mail à {L("email")} ou par courrier à {L("address")}. Vous pouvez utiliser le formulaire type ci-dessous, mais ce n’est pas obligatoire.</p>
    <h2>Comment renvoyer</h2>
    <ol>
      <li>Envoyez-nous par e-mail votre numéro de commande et les articles que vous souhaitez renvoyer. Nous vous répondons avec l’adresse de retour.</li>
      <li>Renvoyez les articles dans les 14 jours suivant votre notification. Emballez-les soigneusement, non portés, étiquettes attachées.</li>
      <li>Les frais directs de renvoi sont à votre charge, sauf si l’article est défectueux ou si nous avons envoyé le mauvais article.</li>
    </ol>
    <h2>Votre remboursement</h2>
    <p>Nous remboursons tous les paiements reçus de votre part, y compris les frais de livraison standard, dans les 14 jours suivant le jour où vous nous avez informés de votre rétractation. Nous utilisons le même moyen de paiement que vous, sans frais pour vous. Nous pouvons différer le remboursement jusqu’à la réception des biens ou jusqu’à ce que vous ayez fourni une preuve de leur expédition, la date retenue étant celle du premier de ces faits.</p>
    <p>Vous pouvez manipuler les articles comme vous le feriez en magasin pour les examiner. Si un article a été porté, lavé ou abîmé au-delà, nous pouvons déduire la dépréciation du remboursement.</p>
    <h2>Articles non repris une fois ouverts</h2>
    <p>Pour des raisons d’hygiène, les chaussettes et sous-vêtements thermiques livrés scellés ne peuvent plus être renvoyés une fois le scellé retiré.</p>
    <h2>Article défectueux ou erroné ?</h2>
    <p>Envoyez-nous une photo par e-mail dans les deux mois suivant la constatation du problème. Nous prenons en charge les frais de retour et réparons, remplaçons ou remboursons l’article dans le cadre de la garantie légale.</p>
    <h2>Formulaire de rétractation</h2>
    <div class="form-box">
      <p>(Veuillez compléter et renvoyer le présent formulaire uniquement si vous souhaitez vous rétracter du contrat.)</p>
      <p>À l’attention de : {L("businessName")}, {L("address")}, {L("email")}</p>
      <p>Je/Nous (*) vous notifie/notifions (*) par la présente ma/notre (*) rétractation du contrat portant sur la vente du bien (*) ci-dessous :</p>
      <p>Commandé le (*) / reçu le (*) :</p>
      <p>Nom du (des) consommateur(s) :</p>
      <p>Adresse du (des) consommateur(s) :</p>
      <p>Signature du (des) consommateur(s) (uniquement en cas de notification du présent formulaire sur papier) :</p>
      <p>Date :</p>
      <p>(*) Rayez la mention inutile.</p>
    </div>
'''),
'shipping': ('Livraison', 'Nous expédions en Belgique et aux Pays-Bas depuis des entrepôts situés dans l’UE, donc sans frais de douane.', f'''
    <table class="info-table">
      <tr><th>Pays</th><td>Belgique, Pays-Bas</td></tr>
      <tr><th>Frais</th><td>{S("shippingFee")} par commande, gratuits à partir de {S("freeShippingThreshold")}</td></tr>
      <tr><th>Délai de livraison</th><td>Généralement 2 à 6 jours ouvrables après paiement</td></tr>
      <tr><th>Suivi</th><td>Vous recevez un lien de suivi par e-mail dès l’expédition de votre commande</td></tr>
      <tr><th>Douane et frais d’importation</th><td>Aucun : toutes les commandes sont expédiées depuis l’UE</td></tr>
    </table>
    <h2>Bon à savoir</h2>
    <ul>
      <li>Si vous commandez plusieurs articles, ils peuvent arriver dans des colis séparés. Cela ne vous coûte jamais plus cher.</li>
      <li>Les délais sont indicatifs. Autour du Black Friday et des fêtes de décembre, ils peuvent être prolongés de quelques jours.</li>
      <li>Si votre colis n’est pas arrivé après 10 jours ouvrables, ou si le suivi n’a pas évolué depuis 5 jours, écrivez-nous à {L("email")} et nous nous en occupons.</li>
      <li>Vérifiez bien votre adresse sur la page de paiement. Si un colis nous revient à cause d’une adresse erronée, nous pouvons le renvoyer au prix coûtant.</li>
    </ul>
'''),
'privacy': ('Politique de confidentialité', 'Cette politique explique quelles données personnelles nous collectons, pourquoi, et quels sont vos droits selon le RGPD. Dernière mise à jour : <span data-store="updated"></span>.', f'''
    <h2>Qui est responsable de vos données</h2>
    <p>Le responsable du traitement est {seller('fr')}.</p>
    <h2>Ce que nous collectons et pourquoi</h2>
    <table class="info-table">
      <tr><th>Données</th><th>Pourquoi</th><th>Base légale</th><th>Durée de conservation</th></tr>
      <tr><td>Nom, adresse de livraison, e-mail, téléphone, détails de commande</td><td>Traiter, livrer et suivre votre commande</td><td>Exécution du contrat</td><td>10 ans (obligations comptables belges)</td></tr>
      <tr><td>Données de paiement</td><td>Encaisser le paiement ; traité par Stripe, nous ne voyons jamais vos données de carte complètes</td><td>Exécution du contrat</td><td>Selon les exigences de Stripe et du droit comptable</td></tr>
      <tr><td>Adresse e-mail (newsletter)</td><td>Vous informer des nouvelles collections</td><td>Votre consentement</td><td>Jusqu’à votre désinscription</td></tr>
      <tr><td>E-mails que vous nous envoyez</td><td>Répondre à vos questions et réclamations</td><td>Notre intérêt légitime à vous aider</td><td>Jusqu’à 2 ans après le dernier contact</td></tr>
    </table>
    <h2>Avec qui nous les partageons</h2>
    <ul>
      <li><strong>Stripe</strong> (paiements).</li>
      <li><strong>Netlify</strong> (hébergement du site et inscriptions à la newsletter).</li>
      <li><strong>Notre partenaire logistique</strong>, qui prépare et expédie votre commande et reçoit uniquement à cette fin votre nom, adresse de livraison et numéro de téléphone.</li>
      <li>Les transporteurs, pour livrer votre colis.</li>
    </ul>
    <p>Certains de ces prestataires sont établis hors de l’Espace économique européen ; les transferts sont encadrés par les clauses contractuelles types de la Commission européenne ou une autre garantie légale. Nous ne vendons jamais vos données.</p>
    <h2>Cookies et stockage</h2>
    <p>Nous n’utilisons pas de cookies de suivi ou publicitaires. Votre panier est enregistré dans votre propre navigateur (stockage local) afin qu’il soit toujours là à votre retour ; il ne quitte votre appareil qu’au moment du paiement. Sur sa page de paiement, Stripe utilise des cookies nécessaires au paiement sécurisé et à la prévention de la fraude.</p>
    <h2>Vos droits</h2>
    <p>Vous pouvez demander à consulter, rectifier ou effacer vos données, à en limiter l’usage ou à vous y opposer, et à les recevoir dans un format portable. Vous pouvez retirer à tout moment votre consentement à la newsletter. Écrivez à {L("email")} ; nous répondons dans un délai d’un mois.</p>
    <p>Si vous n’êtes pas satisfait, vous pouvez introduire une plainte auprès de l’Autorité de protection des données via <a href="https://www.autoriteprotectiondonnees.be" rel="noopener">autoriteprotectiondonnees.be</a>.</p>
'''),
'contact': ('Contact', 'Une question sur une commande, un retour ou un produit ? Nous répondons dans les 2 jours ouvrables.', f'''
    <table class="info-table">
      <tr><th>E-mail</th><td>{L("email")}</td></tr>
      <tr><th>Téléphone</th><td>{L("phone")}</td></tr>
      <tr><th>Adresse</th><td>{L("address")}</td></tr>
      <tr><th>Dénomination</th><td>{L("businessName")}</td></tr>
      <tr><th>Numéro d’entreprise</th><td>{L("enterpriseNumber")}</td></tr>
      <tr><th>Numéro de TVA</th><td>{L("vatNumber")}</td></tr>
    </table>
    <p>Indiquez votre numéro de commande lorsque vous nous écrivez au sujet d’une commande. Les retours sont expliqués sur la <a href="returns.html">page retours</a>.</p>
'''),
}

FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 22 22'%3E%3Crect width='10' height='10' rx='3' fill='%232f5d8a'/%3E%3Crect x='12' width='10' height='10' rx='3' fill='%234f8a4a'/%3E%3Crect y='12' width='10' height='10' rx='3' fill='%239a4a2a'/%3E%3Crect x='12' y='12' width='10' height='10' rx='3' fill='%23c27a1a'/%3E%3C/svg%3E"

def write(lang, slug):
    title, intro, body = C[lang][slug]
    up = '' if lang == 'en' else '../'
    ui = UI[lang]
    # links to the same page in each language
    def href(target):
        if target == lang: return f'{slug}.html'
        if lang == 'en': return f'{target}/{slug}.html'
        return f'../{slug}.html' if target == 'en' else f'../{target}/{slug}.html'
    switch = ' '.join(
        f'<a href="{href(t)}" hreflang="{t}"{" aria-current=\"page\"" if t == lang else ""}>{t.upper()}</a>'
        for t in ['en', 'nl', 'fr'])
    nav = '\n      '.join(f'<a href="{p}.html">{n}</a>' for p, n in zip(PAGES, ui['nav']))
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — Fourfold</title>
  <link rel="icon" href="{FAVICON}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{up}css/styles.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="{up}index.html" class="logo" aria-label="Fourfold home">
        <span class="logo-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
        <span class="logo-text">Fourfold</span>
      </a>
      <nav class="lang-switch" aria-label="Language">{switch}</nav>
    </div>
  </header>

  <main class="container legal-page">
    <a href="{up}index.html" class="back-link">{ui['back']}</a>
    <h1>{title}</h1>
    <p class="lead">{intro}</p>
{body}
  </main>

  <footer class="site-footer">
    <div class="container legal-nav">
      {nav}
    </div>
    <div class="container footer-bottom muted">
      <p class="legal-info" id="legalInfo"></p>
      <p class="legal-info" id="vatNote"></p>
      <p>© <span id="year"></span> Fourfold. {ui['rights']}</p>
    </div>
  </footer>

  <script src="{up}js/config.js"></script>
  <script src="{up}js/legal.js"></script>
</body>
</html>
'''
    d = root if lang == 'en' else os.path.join(root, lang)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, slug + '.html'), 'w').write(html)

for lang in C:
    for slug in PAGES:
        write(lang, slug)
