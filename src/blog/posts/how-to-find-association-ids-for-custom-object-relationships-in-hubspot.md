---
title: "How to Find Association IDs for Custom Object Relationships in HubSpot"
description: Learn how to find Association IDs for Custom Object relationships in HubSpot using the CRM API, step by step.
date: 2025-04-03
image: /images/blog/association-ids/simple-hubl-template.png
imageAlt: "Simple HubL template preview"
imageWidth: 655
imageHeight: 423
tags:
  - post
  - hubspot
  - integrations
  - custom-objects
---

For this blog post, I set up two Custom Objects in HubSpot: **Car** and **AutomotiveService**. Car object is linked to Contacts, while AutomotiveService is associated with Cars.

I also created two test Contacts and assigned above Custom Objects to them. Both are named John.

Now, let's say that for every John I want to display a list of Cars and its related Automotive Services on a webpage. To make this happen, I created a standard HTML+HubL template.

![Simple HubL template](/images/blog/association-ids/simple-hubl-template.png)

_Simple template_

#### Using HubL functions: `crm_objects` and `crm_associations`

To pull this data, we can use two HubL functions: **crm_objects** and **crm_associations**.

1. First, we fetch Contacts.
2. Then, for each Contact, we find their associated Car.
3. Finally, we fetch the Car's related Automotive Services.

Let's add fetching contacts to our template using the **crm_objects** function:

```html
<h1>
  List of Johns cars
</h1>
```

In preview it looks like this:

![Preview of the template](/images/blog/association-ids/Screenshot-2025-04-02-at-16.43.13.png)

_Preview of the template_

We have a list of Contacts. Now, for every person we have to fetch associated Cars.

The **crm_associations** function does that, and its structure looks like this:

```text
crm_associations(objectId, associationCategory, associationId, query, property, formatting)
```

First three parameters are mandatory:

- **objectId**: This is the Contact ID, which we get from the crm_objects function.
- **associationCategory**: Mostly we will use two of them: `HUBSPOT_DEFINED` (used for default HubSpot associations like Contact-Company, Company-Deal, etc.) or `USER_DEFINED` (for Custom Object relationships).
- **associationId**: This is the tricky part. Finding the right ID for a custom association is not straightforward.

#### Finding `Association ID` value

HubSpot's documentation provides a list of default association IDs: [HubSpot Associations Docs](https://developers.hubspot.com/docs/guides/api/crm/associations/associations-v4#contact-to-object)

![Association IDs in HubSpot](/images/blog/association-ids/Screenshot-2025-04-03-at-09.11.45.png)

_Association IDs in HubSpot_

But what if you need the ID for a custom association? HubSpot does not show this anywhere. Fortunately, we can find it using the CRM API.

**Step 1: Create a Private App**  
First, create a **Private App** in HubSpot with access to Contacts and Custom Object schemas.

![Private Apps in Settings](/images/blog/association-ids/private-app-settings.png)

_Private Apps in Settings_

![Private App configuration](/images/blog/association-ids/creating-private-app.png)

_Private App configuration_

Make sure it has the proper scope:

![Private App scopes](/images/blog/association-ids/private-app-scopes.png)

_Private App scopes_

**Step 2: Use the Associations API**  
Once the app is set up, go to the **Associations API** and use the [List request](https://developers.hubspot.com/docs/reference/api/crm/associations/association-details#get-%2Fcrm%2Fv4%2Fobjects%2F%7Bobjecttype%7D%2F%7Bobjectid%7D%2Fassociations%2F%7Btoobjecttype%7D).

**Step 3: Retrieve the Association ID**  
Now, enter the correct values. We are trying to get the association between Contact and Car, so we have to put proper parameters. In my case it looks like this:

![Example request parameters](/images/blog/association-ids/Screenshot-2025-04-03-at-09.29.10.png)

_Example request parameters_

ObjectId `24211927251` is one of my Contacts, which is associated to Car Custom Object. We focus on getting only the association ID, so we can use any Contact ID. It only needs to have a connection to the Car object.

After executing a test request, we get the response with association ID.

![Executing the request](/images/blog/association-ids/executing-request.png)

_Executing the request_

![Response with association ID](/images/blog/association-ids/association-response.png)

_Response with association ID_

Key **typeId** is the one we are looking for.

Having the ID, we can add the first association to our template. We will add fetching Contact-Car association by adding `crm_association` function with ID `34`.

```html
<h1>
  List of Johns cars
</h1>
```

After adding that, we can see the cars on the list:

![Updated list of cars](/images/blog/association-ids/johns-cars.png)

_Updated list of cars_

Now, we can recreate the same steps for fetching association ID between Cars and AutomotiveServices Custom Objects. Let's change the params and make the test request.

![Parameters for fetching relation between Cars and AutomotiveServices](/images/blog/association-ids/cars-services-connection-params.png)

_Parameters for fetching relation between Cars and AutomotiveServices_

![Response from the test request](/images/blog/association-ids/Screenshot-2025-04-02-at-16.05.32.png)

_Response from the test request_

Our **typeId** is `54` for this one.

We already have all necessary information now, let's finish the code in the template:

```html
<h1>
  List of Johns cars
</h1>
```

It gives us the following result:

![Finished list of Contacts with Cars and AutomotiveServices](/images/blog/association-ids/finished-list.png)

_Finished list of Contacts with Cars and AutomotiveServices_

With this technique you can always get the right IDs for your custom associations to use in your template.

Take care.
