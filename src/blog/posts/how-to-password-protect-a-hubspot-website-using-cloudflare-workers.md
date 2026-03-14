---
title: "How to Password Protect a HubSpot Website Using Cloudflare Workers"
description: Add password protection to your HubSpot website using Cloudflare Workers and Basic Auth. A simple way to secure staging or preview pages.
date: 2025-04-11
image: /images/blog/how-to-password-protect-a-hubspot-website.jpg
imageAlt: "How to Password Protect a HubSpot Website Using Cloudflare Workers"
imageWidth: 1200
imageHeight: 628
tags:
  - post
  - hubspot
  - cloudflare
  - security
alternateLangs:
  en: /blog/how-to-password-protect-a-hubspot-website-using-cloudflare-workers/
  pl: /pl/blog/jak-zabezpieczyc-haslem-strone-hubspot-cloudflare-workers/
---

# Want to protect your HubSpot website with a password?

HubSpot makes it easy to build and host marketing websites, but what if you want to restrict access for staging, internal review, or client-only content?

Out of the box, HubSpot only allows password protection for landing pages, not your full website, blog, or other pages. But there is a workaround and it is surprisingly clean.

In this tutorial, I'll show you how to use [Cloudflare](https://www.cloudflare.com/) Workers to add a simple Basic Auth login to any HubSpot-hosted domain or subdomain, without needing a backend or server access.

## Start with connecting domain

Create a free Cloudflare account at `cloudflare.com` and connect your domain by following their onboarding process. You will be asked to change your nameservers at your domain registrar so Cloudflare can manage your DNS.

Next, log in to HubSpot and add your domain under `Settings -> Website -> Domains & URLs`. Use `www.yourdomain.com` as your primary domain. HubSpot will give you DNS records, copy those into Cloudflare's DNS settings.

Make sure the `www` CNAME record is proxied (orange cloud is on) to allow Cloudflare Workers to run.

Once the domain is live in both HubSpot and Cloudflare, you are ready to add password protection using a Worker.

## Create a Cloudflare Worker with Basic Auth

In your Cloudflare dashboard, go to `Workers & Pages` and click `Create Application -> Worker`. Choose the HTTP handler option.

Replace the default code with this example:

```js
addEventListener("fetch", event => {
  event.respondWith(handleRequest(event.request))
})

const username = "admin"
const password = "secretpassword"
const encoded = btoa(`${username}:${password}`)

async function handleRequest(request) {
  const authHeader = request.headers.get("Authorization")

  if (!authHeader || authHeader !== `Basic ${encoded}`) {
    return new Response("Unauthorized", {
      status: 401,
      headers: {
        "WWW-Authenticate": 'Basic realm="Protected Area"',
      },
    })
  }

  return fetch(request)
}
```

Click **Save and Deploy**. This Worker will require a username and password before allowing access to the site.

## Connect Worker to URL

Add a route like this:

```txt
www.yourdomain.com/*
```

Make sure your DNS record for `www` is proxied (orange cloud on), otherwise the Worker will not run.

Once added, open your site. It should now show a login popup asking for the credentials you set in the Worker.
