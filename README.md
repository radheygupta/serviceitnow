# serviceitnow

URL: http://radhey0105.pythonanywhere.com/
Admin Portal: http://radhey0105.pythonanywhere.com/admin/

A web application that allows the user to create "feature requests".

A "feature request" is a request for a new feature that will be added onto an existing
piece of software. Assume that the user is an employee who would be
entering this information after having some correspondence with the client that is
requesting the feature.

Below are the Fields of a "feature request":
  Title: A short, descriptive name of the feature request.
  Description: A long description of the feature request.
  Client: A selection list of clients (like "Client A", "Client B", "Client C")
  Client Priority: Currently priority from 1 to 15 are available. Client Priority numbers will not be repeated for the given client,
  so if a priority is set on a new feature as "1", then all other feature requests for that client should be reordered. 
  Priority 0 means no priority is set yet.
  Target Date: The date that the client is hoping to have the feature.
  Product Area: A selection list of product areas (like 'Policies', 'Billing', 'Claims', 'Reports')
  Status: Current status of the request.

DB Schema:
  1. features: Stores feature requests. Have Many to one relationship with "clients" and "productarea"
  2. clients: Stores client's information.
  3. productarea: Stores product area information.
  4. Django's default auth models are being used.
  
Note:
  1. Clients, Product Areas and users can be added via admin portal.
  2. Feature Request can be also added via admin portal but the priority reordering is not implemented on admin portal. 
  Priority reordering will work on URL http://radhey0105.pythonanywhere.com/features/add/
  
Features to be implemented:
  1. At "Create Feature request" page on select of client fetch already assigned priorities of the client via ajax and display to the user.
  So that he/she can select the priority accordingly.
  2. Enhance the design to improve UX.
  3. Implement priority reordering on admin portal as well.
  
