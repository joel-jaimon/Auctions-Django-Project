# Auctions-Django
 Design of an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”
 
 <h2>Django Admin Credentials:</h2>
 <li>UserID : "joel__jaimon"</li>
 <li>Password : "12345678rr"</li>

<h2>Homepage</h2>
<img src="/dem_img/1.PNG">
<h2>List Page</h2>
<img src = "/dem_img/2.PNG">
  
<h2>Specifications:</h2>
 
<h4>Create Listing Page:</h4>
<li>Create Listing Page:
 <p>Users will be able to visit a page to create a new listing. They will be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users can also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).</p>
</li>

<h4>Active Listings Page:</h4>
<li>
 <p>The default route let users view all of the currently active auction listings. For each active listing, this page display the title, description, current price, and photo (if one exists for the listing).</p>
</li>

<h4>Listing Page: </h4>
<li>
 <p>Clicking on a listing take users to a page specific to that listing. On that page, users will be able to view all details about the listing, including the current price for the listing.
  <li>If the user is signed in, the user will be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user will be able to remove it.</li>
  <li>If the user is signed in, the user will be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user will be presented with an error.</li>
  <li>If the user is signed in and is the one who created the listing, the user have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.</li>
  <li>Users who are signed in will be able to add comments to the listing page. The listing page displays all comments that have been made on the listing.</li>
 </p>
</li>

<h4>Watchlist:</h4>
<li>
 <p> Users who are signed in will be able to visit a Watchlist page, which displays all of the listings that a user has added to their watchlist. Clicking on any of those listings take the user to that listing’s page.</p>
</li>

<h4>Categories:</h4>
<li>
 <p>Users will be able to visit a page that displays a list of all listing categories. Clicking on the name of any category takes the user to a page that displays all of the active listings in that category.</p>
</li>

<h4>Django Admin Interface:</h4>
<li>
<p>Via the Django admin interface, a site administrator will be able to view, add, edit, and delete any listings, comments, and bids made on the site.</p>
</li>

