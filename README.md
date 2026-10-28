# Desert Star

Home page for Desert Star (Moshe Kogan, Mitzpe Ramon): Hebrew at `/`, English at `/en/`, Russian at `/ru/`.

- `index.html` is the Hebrew source. Edit it only.
- `python3 translate.py` regenerates `en/` and `ru/` from the Hebrew page (string map inside the script) and re-injects the language switcher and hreflang tags.
- Images and `og.jpg` live in `public/` so their URLs never change.
- `npm run dev` for local preview, `npm run build` for the `dist/` output.
- Deployed to GitHub Pages by `.github/workflows/deploy.yml` on every push to `main`.
