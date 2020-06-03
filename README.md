<h1 align="center">Tiny Expander</h1>
<p align="center">An API that returns the redirect of URLs</p>

<p align="center">
  <a href="https://deno.land/">
    <img src="https://img.shields.io/badge/Made%20With-Python-4a3fc2?style=flat-square&" alt="Made with Deno" />
  </a>
  <a href="http://makeapullrequest.com/">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="Make a PR" />
  </a>
  <img src="https://img.shields.io/github/license/ninest/drink-if-exists?style=flat-square" alt="MIT" />
  <a href="https://www.buymeacoffee.com/ninest">
    <img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-orange.svg?style=flat-square" alt="Buy Me A Coffee">
  </a>
</p>

## 🚀 Usage

Visiting the URL will return the expanded URL:

```
https://tiny-expander.now.sh/api/<tiny url without https>
```

For example, 

```
https://tiny-expander.now.sh/api/tinyurl.com/y6dqpgc7

# returns
http://www.google.com/
```

Warning: in the GET request, you have to provide the tinyurl **without** the `https://`. This is just a temporary solution until POST is added.

## 🛠 Build setup
Clone or fork the repository, then run

```
pipenv shell
flask run
```

### Hosting
Tiny Expander is hosted with vercel. To host, run

```
vercel
```

<!-- ## 😱 Issues and limitations -->
<!-- are there any limitations worth mentioning in the readme? -->
<!-- - The app won't run on iOS 11 or below -->

## 📜 License
MIT
<!-- replace MIT with whichever license you use -->

<!-- ## 🔖 Legal attribution
Google Play and the Google Play logo are trademarks of Google LLC. -->