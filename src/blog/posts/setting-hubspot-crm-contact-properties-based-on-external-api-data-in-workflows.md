---
title: "Using External API Data to Set HubSpot CRM Contact Properties in Workflows"
description: Step-by-step tutorial showing how to set HubSpot contact properties based on external API data in workflows.
date: 2025-03-20
image: /images/blog/external-api-data-workflows.jpg
imageAlt: "Using External API Data to Set HubSpot CRM Contact Properties in Workflows"
imageWidth: 1200
imageHeight: 628
tags:
  - post
  - hubspot
  - workflows
  - integrations
alternateLangs:
  en: /en/blog/setting-hubspot-crm-contact-properties-based-on-external-api-data-in-workflows/
  pl: /pl/blog/ustawianie-wlasciwosci-kontaktu-hubspot-na-podstawie-danych-z-zewnetrznego-api/
---

<p>Imagine you need to create a workflow that updates a Contact property based on information from an external service. In this guide we’ll walk you through the entire process step by step, so by the end, you’ll be able to implement this solution or the similar one on your own.</p>
<!--more-->
<p>We’ll focus on Contacts here, but of course the same technique can be used with any other CRM objects, like Companies or even Custom Objects.</p>
<h2 id="case-study">Case study</h2>
<p>In this guide we’ll cover the following process:</p>
<p>Every time the email address is set in Contact object, we’ll send request to external service and check if this email is on the emails list returned by this service. Based on the response, we’ll set a value of custom Contact property.</p>
<h2 id="preparation">Preparation</h2>
<p>For the purpose of this guide, I prepared a simple external API, which we’ll call during the workflow action. The API sends a simple list of test email addresses</p>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step3---Testing---4-API-response.png" width="343" height="196" loading="lazy" alt="Step3---Testing---4-API-response" style="height: auto; max-width: 100%; width: 343px;"><br><span style="font-size: 14px;">Simple API response with a list of emails</span></p>
<p>We’ll use this API in the workflow we are going to create.</p>
<p>I also created a custom property in Contact, with a name `<strong>Found in external API</strong>`. This is just a<span>&nbsp;</span><em>true</em>/<em>false</em><span>&nbsp;</span>property and we’ll be setting it based on the response from external API.</p>
<p>Just in case you are not familiar with setting up custom properties, below is the simple guide. If you already know how to do that, you can just skip to `<strong>Step 1 - Setting up private app</strong>`.</p>
<ul>
<li>Go to Contacts and select one of your contact from the list</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1.1---Contacts---0-list.png" width="1600" height="439" loading="lazy" alt="Step1.1---Contacts---0-list" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Simple Contacts list</span></p>
<ul>
<li>In the left sidebar, you’ll see `<strong>Actions</strong>` dropdown. Select `<strong>View all properties</strong>` from it</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1.1---Contacts---1-view-1.png" width="1600" height="870" loading="lazy" alt="Step1.1---Contacts---1-view-1" style="height: auto; max-width: 100%; width: 1600px;"><br><span style="font-size: 14px;">Contact details view</span></p>
<ul>
<li>Click `<strong>Manage properties</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1.1---Contacts---2-all-properties.png" width="1600" height="931" loading="lazy" alt="Step1.1---Contacts---2-all-properties" style="height: auto; max-width: 100%; width: 1600px;"><br><span style="font-size: 14px;">All available properties</span></p>
<ul>
<li>Click `<strong>Create property</strong>` and the simple form will appear</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1.1---Contacts---3-manage-properties.png" width="1600" height="951" loading="lazy" alt="Step1.1---Contacts---3-manage-properties" style="height: auto; max-width: 100%; width: 1600px;"><br><span style="font-size: 14px;">Manage properties view</span></p>
<ul>
<li>Fill the form using values from the screen below:
<ul>
<li>Object type: `<strong>Contact</strong>`</li>
<li>Group: `<strong>Contact information</strong>` (you can select different one if you want)</li>
<li>Label: `<strong>Found in external API</strong>` (you can choose different name)</li>
<li>Description can be left empty</li>
</ul>
</li>
</ul>
<p style="text-align: center;"><br><br><img src="/images/blog/external-api-workflows/Step1.1---Contacts---4-create-property-1.png" width="420" height="380" loading="lazy" alt="Step1.1---Contacts---4-create-property-1" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Setting new property</span></p>
<ul>
<li>Click `<strong>Next</strong>` button at the bottom and you’ll see a `<strong>Field type</strong>` form. Select `<strong>Single checkbox</strong>` and click `<strong>Next</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1.1---Contacts---5-create-property-type.png" width="420" height="540" loading="lazy" alt="Step1.1---Contacts---5-create-property-type" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Setting new property</span></p>
<ul>
<li>The last screen of the wizard is just a selection box where you define whether you want to see this property in forms or not. You can uncheck it.</li>
<li>Click `<strong>Create</strong>`</li>
</ul>
<p>After coming back to `<strong>All properties</strong>` view, you can check if the property has been created. Write its name in search field and you should see it on the list.</p>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1.1---Contacts---6-create-property-result.png" width="1600" height="564" loading="lazy" alt="Step1.1---Contacts---6-create-property-result" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">New property visible in Contacts</span></p>
<p><span>The preparation is done, now we are ready to move further.</span></p>
<h2 id="step-1setting-up-private-app"><strong>Step 1 - Setting up private app</strong></h2>
<p>Since we are going to connect external API, we will have to choose slightly different workflow then usual. We will also have to write a piece of code (don’t worry, I’ll guide you through it).</p>
<p>First, we have to set up the private app in HubSpot.<span>&nbsp;</span><strong>Private app is a gateway for external services or pieces of code</strong>, which allows them to connect and manage parts of your HubSpot system. In this guide, our private app will have access to Contacts.</p>
<ul>
<li>First, go to settings</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1---Private-app---1-settings.png" width="748" height="112" loading="lazy" alt="Step1---Private-app---1-settings" style="height: auto; max-width: 100%; width: 748px;"><span style="font-size: 14px;">Settings icon</span></p>
<ul>
<li>Choose `<strong>Integrations</strong>` in the left sidebar and then `<strong>Private apps</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1---Private-app---2-settings-view.png" width="1600" height="769" loading="lazy" alt="Step1---Private-app---2-settings-view" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Private apps in settings view</span></p>
<ul>
<li>Click `<strong>Create private app</strong>` button</li>
<li>The app creator will appear and you’ll have to set up a few parameters. First one is a name</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1---Private-app---3-name.png" width="1600" height="717" loading="lazy" alt="Step1---Private-app---3-name" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Setting the name of private app</span></p>
<ul>
<li>Next, click the `<strong>Scopes</strong>` tab in the middle of top bar above the form</li>
<li>You need to define the available scopes that the application will have access to. Just write `<em>contacts</em>` in the `<strong>Find a scope</strong>` input, and you’ll get the list of possible scopes related to Contacts</li>
<li>Choose `<strong>crm.objects.contacts</strong>` and `<strong>crm.schemas.contacts</strong>` from the CRM section. Select both - `<strong>Read</strong>` and `<strong>Write</strong>`.</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1---Private-app---4-scopes.png" width="1600" height="874" loading="lazy" alt="Step1---Private-app---4-scopes" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Setting the scope of private app</span></p>
<ul>
<li>Click `<strong>Create app</strong>` button which will be enabled and turned to orange after you selected the scopes</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1---Private-app---4.1-create.png" width="1600" height="874" loading="lazy" alt="Step1---Private-app---4.1-create" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Enabled 'Create app' button</span></p>
<ul>
<li>You’ll see a modal with confirmation that the app has been created. There will be a partially hidden token, which you will use in the workflow</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1---Private-app---5-created.png" width="420" height="422" loading="lazy" alt="Step1---Private-app---5-created" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">App is created</span></p>
<ul>
<li>Click `<strong>show token</strong>` next to the token input, and then copy it</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step1---Private-app---6-show-token.png" width="420" height="422" loading="lazy" alt="Step1---Private-app---6-show-token" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Show token option</span></p>
<p><span>Your app is ready to use, so we can jump into the next step.</span></p>
<h2 id="step-2creating-workflow"><strong>Step 2 - Creating workflow</strong></h2>
<p>This is the biggest and the most important section of the tutorial, so let’s go straight into the step-by-step guide.</p>
<ul>
<li>Go to<span>&nbsp;</span><strong>Automation-&gt;Workflows</strong><span>&nbsp;</span>view from the main menu</li>
<li>Click `<strong>Create workflow</strong>` and select `<strong>From scratch</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---1-create.png" width="1600" height="374" loading="lazy" alt="Step2---Workflow---1-create" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Create workflow</span></p>
<ul>
<li>Our workflow will be `<strong>Contact-based</strong>` so select that box on the left. Select `<strong>Blank workflow</strong>` in the middle section and click `<strong>Next</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---2-create.png" width="1600" height="887" loading="lazy" alt="Step2---Workflow---2-create" style="height: auto; max-width: 100%; width: 1600px;"><span><span style="font-size: 14px;">Create workflow</span></span></p>
<ul>
<li>You’ll see the initial workflow screen. Click on the trigger box (<strong>right arrow on the screen below</strong>) to set up the trigger</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---3-trigger.png" width="1600" height="884" loading="lazy" alt="Step2---Workflow---3-trigger" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Setting up the trigger</span></p>
<ul>
<li>On the left side, click `<strong>When an event occurs</strong>` box (<strong>green arrow on the screen above</strong>)</li>
<li>You’ll see a list of all accessible properties in Contact object</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---4-trigger.png" width="1600" height="886" loading="lazy" alt="Step2---Workflow---4-trigger" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Setting up the trigger</span></p>
<ul>
<li>Select `<strong>Property value changed</strong>`, which is under `<strong>CRM</strong>` section. You can also search for it by starting writing the name in `<strong>Search field</strong>` input</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---5-trigger.png" width="1632" height="972" loading="lazy" alt="Step2---Workflow---5-trigger" style="height: auto; max-width: 100%; width: 1632px;"><span style="font-size: 14px;">Trigger setup</span></p>
<ul>
<li>When you click on it, you’ll have to select the property name, which the workflow will listen to. Find the `<strong>Email</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---5.1-trigger-1.png" width="1622" height="1070" loading="lazy" alt="Step2---Workflow---5.1-trigger-1" style="height: auto; max-width: 100%; width: 1622px;"><span style="font-size: 14px;">Trigger setup</span></p>
<p style="text-align: center;"><span><img src="/images/blog/external-api-workflows/Step2---Workflow---5.2-trigger-1.png" width="1624" height="1154" loading="lazy" alt="Step2---Workflow---5.2-trigger-1" style="height: auto; max-width: 100%; width: 1624px;"></span><span style="font-size: 14px;">Trigger setup</span></p>
<ul>
<li>Now you have to define the property value. Since we just want to check if the email is set, select `<strong>is known</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---5.3-trigger.png" width="1630" height="1156" loading="lazy" alt="Step2---Workflow---5.3-trigger" style="height: auto; max-width: 100%; width: 1630px;"><span style="font-size: 14px;">Trigger setup</span></p>
<ul>
<li>Click `<strong>Save</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---5.3.1-trigger-save.png" width="1630" height="1156" loading="lazy" alt="Step2---Workflow---5.3.1-trigger-save" style="height: auto; max-width: 100%; width: 1630px;"><span style="font-size: 14px;">Trigger setup</span></p>
<ul>
<li>You should see the trigger box similar to the one on the screen</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---5.4-trigger.png" width="420" height="493" loading="lazy" alt="Step2---Workflow---5.4-trigger" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Trigger view</span></p>
<p>Now let’s create another action.</p>
<ul>
<li>Click on a `<strong>plus</strong>` button below the box with created trigger</li>
<li>Select `<strong>Data ops</strong>` and `<strong>Custom code</strong>` from the left sidebar</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---6-custom-code.png" width="1600" height="1269" loading="lazy" alt="Step2---Workflow---6-custom-code" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Custom code action</span></p>
<ul>
<li>Sidebar will change and you’ll see a form with couple of properties to set, as well as the code editor</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---7-side-panel.png" width="1600" height="1087" loading="lazy" alt="Step2---Workflow---7-side-panel" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Side panel</span></p>
<p style="text-align: center;"><span><img src="/images/blog/external-api-workflows/Step2---Workflow---8-side-panel-code.png" width="2026" height="1340" loading="lazy" alt="Step2---Workflow---8-side-panel-code" style="height: auto; max-width: 100%; width: 2026px;"></span><span style="font-size: 14px;">Side panel</span></p>
<ul>
<li>To be able to connect our code to HubSpot Contacts, we have to use our previously created private app. Click the `<strong>Secrets</strong>` dropdown and select `<strong>Add secret</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---9-add-secret.png" width="420" height="357" loading="lazy" alt="Step2---Workflow---9-add-secret" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Add secret</span></p>
<ul>
<li>Write a name (can be just `<strong>SECRET</strong>`) and paste private app access token into the value field</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---10-add-secret-value.png" width="1600" height="504" loading="lazy" alt="Step2---Workflow---10-add-secret-value" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Add secret value</span></p>
<ul>
<li>Click `<strong>Save</strong>`</li>
</ul>
<p>Let’s take a look at the code editor. It’s written in NodeJS and by default it looks like this:</p>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---13-code.png" width="420" height="359" loading="lazy" alt="Step2---Workflow---13-code" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Default code</span></p>
<p>There are some elements which have to be present to execute the code. First one is<span>&nbsp;</span><code>export.main</code></p>
<p><code>exports.main = async (event, callback) =&gt; { ... }</code></p>
<p>It takes 2 arguments:</p>
<ul>
<li><strong>event</strong><span>&nbsp;</span>which is the workflow event we are working on</li>
<li><strong>callback</strong><span>&nbsp;</span>which is a function which returns values to next workflow actions</li>
</ul>
<p>Second must-have part is a<span>&nbsp;</span><code>callback</code><span>&nbsp;</span>function execution, which defines the output of the code</p>
<p>You can see that there is also a part which gets<span>&nbsp;</span><code>email</code><span>&nbsp;</span>from<span>&nbsp;</span><code>event.inputFields</code><span>&nbsp;</span>list.</p>
<p>To make it all work, we have to do some configuration.</p>
<ul>
<li>Find a section under `<strong>Secrets</strong>` with name `<strong>Property to include in code</strong>`. It has two inputs - `<strong>key</strong>` and `<strong>value</strong>`</li>
<li>Write `<strong>email</strong>` as a `<strong>key</strong>`</li>
<li>Select `<strong>Email</strong>` as a `<strong>value</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---14-set-input-field-1.png" width="1636" height="1480" loading="lazy" alt="Step2---Workflow---14-set-input-field-1" style="height: auto; max-width: 100%; width: 1636px;"><span style="font-size: 14px;">Setting up input field</span></p>
<ul>
<li>You’ll end up with filled form like the one on a screen</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---14.1-input-field-property-set.png" width="420" height="523" loading="lazy" alt="Step2---Workflow---14.1-input-field-property-set" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Setting up input field value</span></p>
<p><span>Below is the full code we’re going to use in this action. You can copy it and paste into your editor.</span></p>
<pre><code>const hubspot = require('@hubspot/api-client');

exports.main = async (event, callback) =&gt; {
  let contactFoundInExternalAPI = false;
  const email = event.inputFields['email'];

  const response = await fetch('https://d127-87-206-14-190.ngrok-free.app/v1/api/test');
  const data = await response.json();

  if(data) {
    contactFoundInExternalAPI = data.includes(email);

    const hubspotClient = new hubspot.Client({
      accessToken: process.env.SECRET,
    });
    
    const contactID = event.object.objectId;
    await hubspotClient.crm.contacts.basicApi.update(contactID, {
      properties: { found_in_external_api: contactFoundInExternalAPI },
    });
  }

  callback({
    outputFields: {
      contactFound: contactFoundInExternalAPI,
    }
  });
}
</code></pre>
<p>Let’s go through it so you can understand, what’s going on:</p>
<ul>
<li>In workflows custom actions we have access to some basic NodeJS libraries and one of them is<span>&nbsp;</span><code>@hubspot/api-client</code><span>&nbsp;</span>which allows us to connect to HubSpot API. We import it into the code:</li>
</ul>
<p><code>const hubspot = require('@hubspot/api-client');</code></p>
<ul>
<li>The main code section contains a result variable declaration and getting<span>&nbsp;</span><code>email</code><span>&nbsp;</span>from input fields we declared above</li>
</ul>
<pre><code>exports.main = async (event, callback) =&gt; {
  let contactFoundInExternalAPI = false;
  const email = event.inputFields['email'];
  
  ...
</code></pre>
<ul>
<li>Now we can connect to external API. We’ll use simple<span>&nbsp;</span><code>fetch</code><span>&nbsp;</span>library which is natively available in NodeJS</li>
</ul>
<pre><code>const response = await fetch('https://d127-87-206-14-190.ngrok-free.app/v1/api/test');

const data = await response.json();
</code></pre>
<p><a href="https://d127-87-206-14-190.ngrok-free.app/v1/api/test%60?ref=learnhs.com">https://d127-87-206-14-190.ngrok-free.app/v1/api/test</a><span>&nbsp;</span>is an url of my simple API, which I created only for the purpose of writing this guide. Replace it with the url you want to connect to.</p>
<ul>
<li>if server responded and we have the data, we can proceed and set a variable `<em>contactFoundInExternalAPI</em>` based on the response</li>
</ul>
<pre><code>if(data) {
  contactFoundInExternalAPI = data.includes(email);
</code></pre>
<ul>
<li>now we have to connect to our Contacts through HubSpot API. We’ll use `<em>SECRET</em>`, which we defined in one of the previous steps. It is availble in<span>&nbsp;</span><code>process.env</code><span>&nbsp;</span>object</li>
</ul>
<pre><code>const hubspotClient = new hubspot.Client({
  accessToken: process.env.SECRET,
});
</code></pre>
<ul>
<li>after setting the connection, we can update our Contact object. We’ll update only the Contact which triggers the workflow, so we have to get its<span>&nbsp;</span><code>id</code><span>&nbsp;</span>from<span>&nbsp;</span><code>event.object.objectId</code></li>
</ul>
<p>&nbsp; &nbsp;<span>&nbsp;</span><code>const contactID = event.object.objectId;</code></p>
<ul>
<li>we are updating only the property which we created previously - `<strong>Found in external API</strong>`. HubSpot automatically creates property names with underscore based on labels, so in our case, the property name is `<strong>found_in_external_api</strong>`. We’ll use it in the code</li>
</ul>
<pre><code>await hubspotClient.crm.contacts.basicApi.update(contactID, {
  properties: { found_in_external_api: contactFoundInExternalAPI },
});
</code></pre>
<ul>
<li>last part of code is just a callback which pass `<em>outputFields</em>` to another action (if needed). In our example, we’ll pass `<em>contactFound</em>` parameter, which will have `<em>true</em>` or `<em>false</em>` value</li>
</ul>
<pre><code>callback({
  outputFields: {
    contactFound: contactFoundInExternalAPI,
  }
});
</code></pre>
<p><span>Even if we defined `</span><em>outputFields</em><span>` in the code, we still have to add them to action output. To do that, find the `</span><strong>Add output</strong><span>` link placed below the code editor. Click it.</span></p>
<p style="text-align: center;"><span><img src="/images/blog/external-api-workflows/Step2---Workflow---15-add-output.png" width="420" height="715" loading="lazy" alt="Step2---Workflow---15-add-output" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"></span><span style="font-size: 14px;">Add output</span></p>
<ul>
<li>Fill the `<strong>Data type</strong>` which should be `<strong>Boolean</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---15.1-add-output---data-type.png" width="420" height="354" loading="lazy" alt="Step2---Workflow---15.1-add-output---data-type" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Output data type</span></p>
<ul>
<li>Fill the `<strong>Name</strong>` which should be exactly the same as in the `<em>callback</em>` action above. In our case it’s `<em>contactFound</em>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---15.2-add-output---data-value.png" width="420" height="433" loading="lazy" alt="Step2---Workflow---15.2-add-output---data-value" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Output data value</span></p>
<p><span>`<strong>Save</strong>` the action and you’ll see 2 boxes in workflows like on the image below.</span></p>
<p style="text-align: center;"><span><img src="/images/blog/external-api-workflows/Step2---Workflow---16-custom-action-is-set.png" width="420" height="839" loading="lazy" alt="Step2---Workflow---16-custom-action-is-set" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"></span><span style="font-size: 14px;">Workflow actions</span></p>
<h2 id="step-3testing"><strong>Step 3 - Testing</strong></h2>
<p>We are ready to test what we’ve created so far. If your left sidebar disappeared after save, you can bring it back by clicking the action box in the workflow - the one with `<strong>Custom code</strong>`.</p>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step2---Workflow---17-bring-back-sidebar.png" width="420" height="839" loading="lazy" alt="Step2---Workflow---17-bring-back-sidebar" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Workflow actions</span></p>
<p>Now you are ready to test the action.</p>
<ul>
<li>Scroll the sidebar to the very bottom. You’ll see the `<strong>Test action</strong>` expandable section. Click it.</li>
<li>Select any of your contacts you would like to test. For testing I strongly recommend using test contact</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step3---Testing---1-contact-select.png" width="420" height="260" loading="lazy" alt="Step3---Testing---1-contact-select" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Contact select</span></p>
<p style="text-align: center;"><span><img src="/images/blog/external-api-workflows/Step3---Testing---2-contact-select.png" width="420" height="243" loading="lazy" alt="Step3---Testing---2-contact-select" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"></span><span style="font-size: 14px;">Contact select</span></p>
<ul>
<li>Click `<strong>Test</strong>`</li>
<li>You’ll see the confirmation modal, click `<strong>Test</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step3---Testing---3-test-confirm.png" width="420" height="302" loading="lazy" alt="Step3---Testing---3-test-confirm" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Test confirm</span></p>
<ul>
<li>Just to remind, my simple API is responding with a list of the following email addresses</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step3---Testing---4-API-response.png" width="376" height="215" loading="lazy" alt="Step3---Testing---4-API-response" style="height: auto; max-width: 100%; width: 376px;"><br><span style="font-size: 14px;">API response</span></p>
<ul>
<li>When the test ends, you’ll see the response, like on the screen below. You’ll see the status of response (for example `<strong>Success</strong>` like on the screen), output fields which we defined previously and a few logs.</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step3---Testing---5-success-false.png" width="420" height="700" loading="lazy" alt="Step3---Testing---5-success-false" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Test 1</span></p>
<ul>
<li>My test contact has an email `<a href="mailto:bh@hubspot.com">bh@hubspot.com</a>` and it’s not on the list. That’s why the `<em>contactFound</em>` value in output of the action is `<em>false</em>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step3---Testing---5.1-success-false-point.png" width="420" height="700" loading="lazy" alt="Step3---Testing---5.1-success-false-point" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Test 1</span></p>
<ul>
<li>If you switch to the Contacts view and check all properties for the selected contact, you’ll see that the value of the property `<strong>Found in external API</strong>` has been set to `<strong>No</strong>`, which equals to `<em>false</em>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step3---Testing---6-contacts-result-no.png" width="1600" height="576" loading="lazy" alt="Step3---Testing---6-contacts-result-no" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Property updated</span></p>
<p><span>Before executing next test, I made some adjustments in my API. I added `</span><a href="mailto:bh@hubspot.com">bh@hubspot.com</a><span>` email address to the returned list.</span></p>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step3---Testing---7-API-response-extended.png" width="341" height="240" loading="lazy" alt="Step3---Testing---7-API-response-extended" style="height: auto; max-width: 100%; width: 341px;"><br><span style="font-size: 14px;">API response extended</span></p>
<p style="text-align: left;"><span>Now, after executing the same testing steps as above, this time I got `<em>contactFound</em>` value set to `<em>true</em>`, which means that this email has been found on the list.</span></p>
<p style="text-align: center;"><span><img src="/images/blog/external-api-workflows/Step3---Testing---8-success-true.png" width="420" height="558" loading="lazy" alt="Step3---Testing---8-success-true" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"></span><span style="font-size: 14px;">Test 2</span></p>
<p><span>Again, switch to the Contacts view and this time you should see the property `</span><strong>Found in external API</strong><span>` set to `</span><strong>Yes</strong><span>` 🚀</span></p>
<p style="text-align: center;"><span><img src="/images/blog/external-api-workflows/Step3---Testing---9-contacts-result-yes.png" width="1600" height="577" loading="lazy" alt="Step3---Testing---9-contacts-result-yes" style="height: auto; max-width: 100%; width: 1600px;"></span><span style="font-size: 14px;">Property updated</span></p>
<p><span>It’s also worth mentioning, that you can use&nbsp;<code>console.log</code>&nbsp;in the code if you want to debug it. For example, when I add&nbsp;<code>console.log(‘data’, data)</code>&nbsp;just to see what comes from the API, I’ll see this log at the bottom after executing the test.</span></p>
<p style="text-align: center;"><span><img src="/images/blog/external-api-workflows/Step3---Testing---10-console-logs.png" width="1462" height="1094" loading="lazy" alt="Step3---Testing---10-console-logs" style="height: auto; max-width: 100%; width: 1462px;"></span><span style="font-size: 14px;">Added console.log</span></p>
<p style="text-align: center;"><span><img src="/images/blog/external-api-workflows/Step3---Testing---11-logs.png" width="420" height="622" loading="lazy" alt="Step3---Testing---11-logs" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"></span><span style="font-size: 14px;">Logs in tests</span></p>
<h2 id="step-4possible-further-actions"><strong>Step 4 - Possible further actions</strong></h2>
<p>If you wish to add next action in the workflow and use the property we've just set, you can do it the following way.</p>
<ul>
<li>Click the `<strong>plus</strong>` icon below the `<strong>Custom code</strong>` box</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step4---Further-actions---1-next-action.png" width="420" height="454" loading="lazy" alt="Step4---Further-actions---1-next-action" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Next action in workflow</span></p>
<ul>
<li>Select action. Since the property we’ve created is true or false, the natural next action will be `<strong>Branch</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step4---Further-actions---2-action-type.png" width="1600" height="1267" loading="lazy" alt="Step4---Further-actions---2-action-type" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Action type</span></p>
<ul>
<li>Select `<strong>One property or action input</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step4---Further-actions---3-property-change.png" width="420" height="583" loading="lazy" alt="Step4---Further-actions---3-property-change" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Action type</span></p>
<ul>
<li>You’ll see the dropdown with properties. Click it</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step4---Further-actions---4-select-property.png" width="420" height="385" loading="lazy" alt="Step4---Further-actions---4-select-property" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Select property</span></p>
<p><span>There is a dropdown at the top - `<strong>View properties or action outputs from</strong>`. If you set `<strong>Enrolled contact</strong>`, you’ll be able to find our `<strong>Found in external API</strong>` property in the list below. It will be visible under `<strong>Enumeration properties</strong>`, because it’s&nbsp;<em>true</em>&nbsp;or&nbsp;<em>false</em></span></p>
<p style="text-align: center;"><span><em><img src="/images/blog/external-api-workflows/Step4---Further-actions---4.1-enrolled-property.png" width="1630" height="1588" loading="lazy" alt="Step4---Further-actions---4.1-enrolled-property" style="height: auto; max-width: 100%; width: 1630px;"></em></span><span style="font-size: 14px;">Properties list</span></p>
<p style="text-align: center;"><span><img src="/images/blog/external-api-workflows/Step4---Further-actions---5-select-property-value.png" width="1648" height="1688" loading="lazy" alt="Step4---Further-actions---5-select-property-value" style="height: auto; max-width: 100%; width: 1648px;"></span><span style="font-size: 14px;">Property in enrolled contacts</span></p>
<p><span>You can also switch to `<strong>Action output</strong>` in the dropdown and select `<strong>contactFound</strong>` field, which we created in a step before.</span></p>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step4---Further-actions---6-action-output.png" width="1626" height="698" loading="lazy" alt="Step4---Further-actions---6-action-output" style="height: auto; max-width: 100%; width: 1626px;"><span style="font-size: 14px;">Action outputs</span></p>
<h2 id="step-5review-and-turn-on"><strong>Step 5 - Review and turn on</strong></h2>
<p>Only a few steps left to run this workflow on production.</p>
<ul>
<li>First, you have to give it a name. Click the pencil icon at the top bar and write a name of your workflow and save it</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step5---Deploy---2-set-name.png" width="420" height="504" loading="lazy" alt="Step5---Deploy---2-set-name" style="height: auto; max-width: 100%; width: 420px; margin-left: auto; margin-right: auto; display: block;"><span style="font-size: 14px;">Set workflow name</span></p>
<ul>
<li>Click `<strong>Review and publish</strong>` and you’ll see the review of what does the workflow do</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step5---Deploy---3-review.png" width="1600" height="178" loading="lazy" alt="Step5---Deploy---3-review" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Workflow review</span></p>
<ul>
<li>If everything is ok, click `<strong>Turn on</strong>`</li>
</ul>
<p style="text-align: center;"><img src="/images/blog/external-api-workflows/Step5---Deploy---4-turn-on.png" width="1600" height="549" loading="lazy" alt="Step5---Deploy---4-turn-on" style="height: auto; max-width: 100%; width: 1600px;"><span style="font-size: 14px;">Turning on workflow </span></p>
<p><span>That’s it! Your workflow is up and running 😎</span></p>
<div>
<h2 id="conclusion">Conclusion</h2>
<p>As you can see, adding a custom code action in workflows opens up a lot of automation possibilities. With such solution you can create highly customized workflows which meet your unique needs.</p>
<p>Cheers!</p>
</div>
<div>&nbsp;</div>
