]633;E;{   echo "# Full Code Handoff"\x3b   echo\x3b   echo "Generated: 2026-03-09"\x3b   echo\x3b   echo "This file is a direct code snapshot for external AI review."\x3b   echo\x3b } > "$OUT";6038813a-2ff0-4309-81fb-b1a9ac334a73]633;C# Full Code Handoff

Generated: 2026-03-09

This file is a direct code snapshot for external AI review.

## README.md

```markdown
# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) (or [oxc](https://oxc.rs) when used in [rolldown-vite](https://vite.dev/guide/rolldown)) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

```

## .gitignore

```text
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

```

## index.html

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>membrane</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

## package.json

```json
{
  "name": "membrane",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "autoprefixer": "^10.4.27",
    "postcss": "^8.5.8",
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-router-dom": "^7.13.1",
    "tailwindcss": "^4.2.1"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.1",
    "@tailwindcss/postcss": "^4.2.1",
    "@types/node": "^24.10.1",
    "@types/react": "^19.2.7",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^5.1.1",
    "eslint": "^9.39.1",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-react-refresh": "^0.4.24",
    "globals": "^16.5.0",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.48.0",
    "vite": "^8.0.0-beta.13"
  },
  "overrides": {
    "vite": "^8.0.0-beta.13"
  }
}

```

## package-lock.json

```json
{
  "name": "membrane",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "membrane",
      "version": "0.0.0",
      "dependencies": {
        "autoprefixer": "^10.4.27",
        "postcss": "^8.5.8",
        "react": "^19.2.0",
        "react-dom": "^19.2.0",
        "react-router-dom": "^7.13.1",
        "tailwindcss": "^4.2.1"
      },
      "devDependencies": {
        "@eslint/js": "^9.39.1",
        "@tailwindcss/postcss": "^4.2.1",
        "@types/node": "^24.10.1",
        "@types/react": "^19.2.7",
        "@types/react-dom": "^19.2.3",
        "@vitejs/plugin-react": "^5.1.1",
        "eslint": "^9.39.1",
        "eslint-plugin-react-hooks": "^7.0.1",
        "eslint-plugin-react-refresh": "^0.4.24",
        "globals": "^16.5.0",
        "typescript": "~5.9.3",
        "typescript-eslint": "^8.48.0",
        "vite": "^8.0.0-beta.13"
      }
    },
    "node_modules/@alloc/quick-lru": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz",
      "integrity": "sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.0.tgz",
      "integrity": "sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.28.5",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.29.0.tgz",
      "integrity": "sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.29.0.tgz",
      "integrity": "sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42Pf1XTYED2Rni5f95npYeuwMDQA==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-compilation-targets": "^7.28.6",
        "@babel/helper-module-transforms": "^7.28.6",
        "@babel/helpers": "^7.28.6",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/traverse": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.29.1",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.29.1.tgz",
      "integrity": "sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.28.6.tgz",
      "integrity": "sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.28.6",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz",
      "integrity": "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.28.6.tgz",
      "integrity": "sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.28.6.tgz",
      "integrity": "sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.28.6",
        "@babel/helper-validator-identifier": "^7.28.5",
        "@babel/traverse": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.28.6.tgz",
      "integrity": "sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
      "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.27.1.tgz",
      "integrity": "sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.28.6.tgz",
      "integrity": "sha512-xOBvwq86HHdB7WUDTfKfT/Vuxh7gElQ+Sfti2Cy6yIWNW05P8iUslOVcZ4/sKbE+/jQaukQAdz/gf3724kYdqw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.0.tgz",
      "integrity": "sha512-IyDgFV5GeDUVX4YdF/3CPULtVGSXXMLh1xVIgdCgxApktqnQV0r7/8Nqthg+8YLGaAtdyIlo2qIdZrbCv4+7ww==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.0"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-self": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.27.1.tgz",
      "integrity": "sha512-6UzkCs+ejGdZ5mFFC/OCUrv028ab2fp1znZmCZjAOBKiBK2jXD1O+BPSfX8X2qjJ75fZBMSnQn3Rq2mrBJK2mw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-source": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.27.1.tgz",
      "integrity": "sha512-zbwoTsBruTeKB9hSq73ha66iFeJHuaFkUbwvqElnygoNbj/jHRsSeokowZFN3CZ64IvEqcmmkVe89OPXc7ldAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.28.6.tgz",
      "integrity": "sha512-YA6Ma2KsCdGb+WC6UpBVFJGXL58MDA6oyONbjyF/+5sBgxY/dwkhLogbMT2GXXyU84/IhRw/2D1Os1B/giz+BQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.28.6",
        "@babel/parser": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.0.tgz",
      "integrity": "sha512-4HPiQr0X7+waHfyXPZpWPfWL/J7dcN1mx9gL6WdQVMbPnF3+ZhSMs8tCxN7oHddJE9fhNE7+lxdnlyemKfJRuA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-globals": "^7.28.0",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.29.0",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.0.tgz",
      "integrity": "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.28.5"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@emnapi/core": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/@emnapi/core/-/core-1.8.1.tgz",
      "integrity": "sha512-AvT9QFpxK0Zd8J0jopedNm+w/2fIzvtPKPjqyw9jwvBaReTTqPBk9Hixaz7KbjimP+QNz605/XnjFcDAL2pqBg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/wasi-threads": "1.1.0",
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/runtime": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.8.1.tgz",
      "integrity": "sha512-mehfKSMWjjNol8659Z8KxEMrdSJDDot5SXMq00dM8BN4o+CLNXQ0xH2V7EchNHV4RmbZLmmPdEaXZc5H2FXmDg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/wasi-threads": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@emnapi/wasi-threads/-/wasi-threads-1.1.0.tgz",
      "integrity": "sha512-WI0DdZ8xFSbgMjR1sFsKABJ/C5OnRrjT06JXbZKexJGrDuPTzZdDYfFlsgcCXCyf+suG5QU2e/y1Wo2V/OapLQ==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@eslint-community/eslint-utils": {
      "version": "4.9.1",
      "resolved": "https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.9.1.tgz",
      "integrity": "sha512-phrYmNiYppR7znFEdqgfWHXR6NCkZEK7hwWDHZUjit/2/U0r6XvkDl0SYnoM51Hq7FhCGdLDT6zxCCOY1hexsQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "eslint-visitor-keys": "^3.4.3"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      },
      "peerDependencies": {
        "eslint": "^6.0.0 || ^7.0.0 || >=8.0.0"
      }
    },
    "node_modules/@eslint-community/eslint-utils/node_modules/eslint-visitor-keys": {
      "version": "3.4.3",
      "resolved": "https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-3.4.3.tgz",
      "integrity": "sha512-wpc+LXeiyiisxPlEkUzU6svyS1frIO3Mgxj1fdy7Pm8Ygzguax2N3Fa/D/ag1WqbOprdI+uY6wMUl8/a2G+iag==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/@eslint-community/regexpp": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.12.2.tgz",
      "integrity": "sha512-EriSTlt5OC9/7SXkRSCAhfSxxoSUgBm33OH+IkwbdpgoqsSsUg7y3uh+IICI/Qg4BBWr3U2i39RpmycbxMq4ew==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^12.0.0 || ^14.0.0 || >=16.0.0"
      }
    },
    "node_modules/@eslint/config-array": {
      "version": "0.21.2",
      "resolved": "https://registry.npmjs.org/@eslint/config-array/-/config-array-0.21.2.tgz",
      "integrity": "sha512-nJl2KGTlrf9GjLimgIru+V/mzgSK0ABCDQRvxw5BjURL7WfH5uoWmizbH7QB6MmnMBd8cIC9uceWnezL1VZWWw==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@eslint/object-schema": "^2.1.7",
        "debug": "^4.3.1",
        "minimatch": "^3.1.5"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      }
    },
    "node_modules/@eslint/config-helpers": {
      "version": "0.4.2",
      "resolved": "https://registry.npmjs.org/@eslint/config-helpers/-/config-helpers-0.4.2.tgz",
      "integrity": "sha512-gBrxN88gOIf3R7ja5K9slwNayVcZgK6SOUORm2uBzTeIEfeVaIhOpCtTox3P6R7o2jLFwLFTLnC7kU/RGcYEgw==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@eslint/core": "^0.17.0"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      }
    },
    "node_modules/@eslint/core": {
      "version": "0.17.0",
      "resolved": "https://registry.npmjs.org/@eslint/core/-/core-0.17.0.tgz",
      "integrity": "sha512-yL/sLrpmtDaFEiUj1osRP4TI2MDz1AddJL+jZ7KSqvBuliN4xqYY54IfdN8qD8Toa6g1iloph1fxQNkjOxrrpQ==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@types/json-schema": "^7.0.15"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      }
    },
    "node_modules/@eslint/eslintrc": {
      "version": "3.3.5",
      "resolved": "https://registry.npmjs.org/@eslint/eslintrc/-/eslintrc-3.3.5.tgz",
      "integrity": "sha512-4IlJx0X0qftVsN5E+/vGujTRIFtwuLbNsVUe7TO6zYPDR1O6nFwvwhIKEKSrl6dZchmYBITazxKoUYOjdtjlRg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ajv": "^6.14.0",
        "debug": "^4.3.2",
        "espree": "^10.0.1",
        "globals": "^14.0.0",
        "ignore": "^5.2.0",
        "import-fresh": "^3.2.1",
        "js-yaml": "^4.1.1",
        "minimatch": "^3.1.5",
        "strip-json-comments": "^3.1.1"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/@eslint/eslintrc/node_modules/globals": {
      "version": "14.0.0",
      "resolved": "https://registry.npmjs.org/globals/-/globals-14.0.0.tgz",
      "integrity": "sha512-oahGvuMGQlPw/ivIYBjVSrWAfWLBeku5tpPE2fOPLi+WHffIWbuh2tCjhyQhTBPMf5E9jDEH4FOmTYgYwbKwtQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/@eslint/js": {
      "version": "9.39.4",
      "resolved": "https://registry.npmjs.org/@eslint/js/-/js-9.39.4.tgz",
      "integrity": "sha512-nE7DEIchvtiFTwBw4Lfbu59PG+kCofhjsKaCWzxTpt4lfRjRMqG6uMBzKXuEcyXhOHoUp9riAm7/aWYGhXZ9cw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "url": "https://eslint.org/donate"
      }
    },
    "node_modules/@eslint/object-schema": {
      "version": "2.1.7",
      "resolved": "https://registry.npmjs.org/@eslint/object-schema/-/object-schema-2.1.7.tgz",
      "integrity": "sha512-VtAOaymWVfZcmZbp6E2mympDIHvyjXs/12LqWYjVw6qjrfF+VK+fyG33kChz3nnK+SU5/NeHOqrTEHS8sXO3OA==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      }
    },
    "node_modules/@eslint/plugin-kit": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/@eslint/plugin-kit/-/plugin-kit-0.4.1.tgz",
      "integrity": "sha512-43/qtrDUokr7LJqoF2c3+RInu/t4zfrpYdoSDfYyhg52rwLV6TnOvdG4fXm7IkSB3wErkcmJS9iEhjVtOSEjjA==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@eslint/core": "^0.17.0",
        "levn": "^0.4.1"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      }
    },
    "node_modules/@humanfs/core": {
      "version": "0.19.1",
      "resolved": "https://registry.npmjs.org/@humanfs/core/-/core-0.19.1.tgz",
      "integrity": "sha512-5DyQ4+1JEUzejeK1JGICcideyfUbGixgS9jNgex5nqkW+cY7WZhxBigmieN5Qnw9ZosSNVC9KQKyb+GUaGyKUA==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": ">=18.18.0"
      }
    },
    "node_modules/@humanfs/node": {
      "version": "0.16.7",
      "resolved": "https://registry.npmjs.org/@humanfs/node/-/node-0.16.7.tgz",
      "integrity": "sha512-/zUx+yOsIrG4Y43Eh2peDeKCxlRt/gET6aHfaKpuq267qXdYDFViVHfMaLyygZOnl0kGWxFIgsBy8QFuTLUXEQ==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@humanfs/core": "^0.19.1",
        "@humanwhocodes/retry": "^0.4.0"
      },
      "engines": {
        "node": ">=18.18.0"
      }
    },
    "node_modules/@humanwhocodes/module-importer": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/@humanwhocodes/module-importer/-/module-importer-1.0.1.tgz",
      "integrity": "sha512-bxveV4V8v5Yb4ncFTT3rPSgZBOpCkjfK0y4oVVVJwIuDVBRMDXrPyXRL988i5ap9m9bnyEEjWfm5WkBmtffLfA==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": ">=12.22"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/nzakas"
      }
    },
    "node_modules/@humanwhocodes/retry": {
      "version": "0.4.3",
      "resolved": "https://registry.npmjs.org/@humanwhocodes/retry/-/retry-0.4.3.tgz",
      "integrity": "sha512-bV0Tgo9K4hfPCek+aMAn81RppFKv2ySDQeMoSZuvTASywNTnVJCArCZE2FWqpvIatKu7VMRLWlR1EazvVhDyhQ==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": ">=18.18"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/nzakas"
      }
    },
    "node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.13",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
      "integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.0",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/remapping": {
      "version": "2.3.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/remapping/-/remapping-2.3.5.tgz",
      "integrity": "sha512-LI9u/+laYG4Ds1TDKSJW2YPrIlcVYOwi2fUC6xB43lueCjgxV4lffOCZCtYFiH6TNOX+tQKXx97T4IKHbhyHEQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/gen-mapping": "^0.3.5",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
      "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.31",
      "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
      "integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/@napi-rs/wasm-runtime": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@napi-rs/wasm-runtime/-/wasm-runtime-1.1.1.tgz",
      "integrity": "sha512-p64ah1M1ld8xjWv3qbvFwHiFVWrq1yFvV4f7w+mzaqiR4IlSgkqhcRdHwsGgomwzBH51sRY4NEowLxnaBjcW/A==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/core": "^1.7.1",
        "@emnapi/runtime": "^1.7.1",
        "@tybys/wasm-util": "^0.10.1"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/Brooooooklyn"
      }
    },
    "node_modules/@oxc-project/runtime": {
      "version": "0.115.0",
      "resolved": "https://registry.npmjs.org/@oxc-project/runtime/-/runtime-0.115.0.tgz",
      "integrity": "sha512-Rg8Wlt5dCbXhQnsXPrkOjL1DTSvXLgb2R/KYfnf1/K+R0k6UMLEmbQXPM+kwrWqSmWA2t0B1EtHy2/3zikQpvQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxc-project/types": {
      "version": "0.115.0",
      "resolved": "https://registry.npmjs.org/@oxc-project/types/-/types-0.115.0.tgz",
      "integrity": "sha512-4n91DKnebUS4yjUHl2g3/b2T+IUdCfmoZGhmwsovZCDaJSs+QkVAM+0AqqTxHSsHfeiMuueT75cZaZcT/m0pSw==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/Boshen"
      }
    },
    "node_modules/@rolldown/binding-android-arm64": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-android-arm64/-/binding-android-arm64-1.0.0-rc.8.tgz",
      "integrity": "sha512-5bcmMQDWEfWUq3m79Mcf/kbO6e5Jr6YjKSsA1RnpXR6k73hQ9z1B17+4h93jXpzHvS18p7bQHM1HN/fSd+9zog==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-darwin-arm64": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-darwin-arm64/-/binding-darwin-arm64-1.0.0-rc.8.tgz",
      "integrity": "sha512-dcHPd5N4g9w2iiPRJmAvO0fsIWzF2JPr9oSuTjxLL56qu+oML5aMbBMNwWbk58Mt3pc7vYs9CCScwLxdXPdRsg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-darwin-x64": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-darwin-x64/-/binding-darwin-x64-1.0.0-rc.8.tgz",
      "integrity": "sha512-mw0VzDvoj8AuR761QwpdCFN0sc/jspuc7eRYJetpLWd+XyansUrH3C7IgNw6swBOgQT9zBHNKsVCjzpfGJlhUA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-freebsd-x64": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-freebsd-x64/-/binding-freebsd-x64-1.0.0-rc.8.tgz",
      "integrity": "sha512-xNrRa6mQ9NmMIJBdJtPMPG8Mso0OhM526pDzc/EKnRrIrrkHD1E0Z6tONZRmUeJElfsQ6h44lQQCcDilSNIvSQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm-gnueabihf": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm-gnueabihf/-/binding-linux-arm-gnueabihf-1.0.0-rc.8.tgz",
      "integrity": "sha512-WgCKoO6O/rRUwimWfEJDeztwJJmuuX0N2bYLLRxmXDTtCwjToTOqk7Pashl/QpQn3H/jHjx0b5yCMbcTVYVpNg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm64-gnu": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm64-gnu/-/binding-linux-arm64-gnu-1.0.0-rc.8.tgz",
      "integrity": "sha512-tOHgTOQa8G4Z3ULj4G3NYOGGJEsqPHR91dT72u63OtVsZ7B6wFJKOx+ZKv+pvwzxWz92/I2ycaqi2/Ll4l+rlg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm64-musl": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm64-musl/-/binding-linux-arm64-musl-1.0.0-rc.8.tgz",
      "integrity": "sha512-oRbxcgDujCi2Yp1GTxoUFsIFlZsuPHU4OV4AzNc3/6aUmR4lfm9FK0uwQu82PJsuUwnF2jFdop3Ep5c1uK7Uxg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-ppc64-gnu": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-ppc64-gnu/-/binding-linux-ppc64-gnu-1.0.0-rc.8.tgz",
      "integrity": "sha512-oaLRyUHw8kQE5M89RqrDJZ10GdmGJcMeCo8tvaE4ukOofqgjV84AbqBSH6tTPjeT2BHv+xlKj678GBuIb47lKA==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-s390x-gnu": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-s390x-gnu/-/binding-linux-s390x-gnu-1.0.0-rc.8.tgz",
      "integrity": "sha512-1hjSKFrod5MwBBdLOOA0zpUuSfSDkYIY+QqcMcIU1WOtswZtZdUkcFcZza9b2HcAb0bnpmmyo0LZcaxLb2ov1g==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-x64-gnu": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-x64-gnu/-/binding-linux-x64-gnu-1.0.0-rc.8.tgz",
      "integrity": "sha512-a1+F0aV4Wy9tT3o+cHl3XhOy6aFV+B8Ll+/JFj98oGkb6lGk3BNgrxd+80RwYRVd23oLGvj3LwluKYzlv1PEuw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-x64-musl": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-x64-musl/-/binding-linux-x64-musl-1.0.0-rc.8.tgz",
      "integrity": "sha512-bGyXCFU11seFrf7z8PcHSwGEiFVkZ9vs+auLacVOQrVsI8PFHJzzJROF3P6b0ODDmXr0m6Tj5FlDhcXVk0Jp8w==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-openharmony-arm64": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-openharmony-arm64/-/binding-openharmony-arm64-1.0.0-rc.8.tgz",
      "integrity": "sha512-n8d+L2bKgf9G3+AM0bhHFWdlz9vYKNim39ujRTieukdRek0RAo2TfG2uEnV9spa4r4oHUfL9IjcY3M9SlqN1gw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-wasm32-wasi": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-wasm32-wasi/-/binding-wasm32-wasi-1.0.0-rc.8.tgz",
      "integrity": "sha512-4R4iJDIk7BrJdteAbEAICXPoA7vZoY/M0OBfcRlQxzQvUYMcEp2GbC/C8UOgQJhu2TjGTpX1H8vVO1xHWcRqQA==",
      "cpu": [
        "wasm32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@napi-rs/wasm-runtime": "^1.1.1"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@rolldown/binding-win32-arm64-msvc": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-win32-arm64-msvc/-/binding-win32-arm64-msvc-1.0.0-rc.8.tgz",
      "integrity": "sha512-3lwnklba9qQOpFnQ7EW+A1m4bZTWXZE4jtehsZ0YOl2ivW1FQqp5gY7X2DLuKITggesyuLwcmqS11fA7NtrmrA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-win32-x64-msvc": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-win32-x64-msvc/-/binding-win32-x64-msvc-1.0.0-rc.8.tgz",
      "integrity": "sha512-VGjCx9Ha1P/r3tXGDZyG0Fcq7Q0Afnk64aaKzr1m40vbn1FL8R3W0V1ELDvPgzLXaaqK/9PnsqSaLWXfn6JtGQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/pluginutils": {
      "version": "1.0.0-rc.3",
      "resolved": "https://registry.npmjs.org/@rolldown/pluginutils/-/pluginutils-1.0.0-rc.3.tgz",
      "integrity": "sha512-eybk3TjzzzV97Dlj5c+XrBFW57eTNhzod66y9HrBlzJ6NsCrWCp/2kaPS3K9wJmurBC0Tdw4yPjXKZqlznim3Q==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@tailwindcss/node": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/node/-/node-4.2.1.tgz",
      "integrity": "sha512-jlx6sLk4EOwO6hHe1oCGm1Q4AN/s0rSrTTPBGPM0/RQ6Uylwq17FuU8IeJJKEjtc6K6O07zsvP+gDO6MMWo7pg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/remapping": "^2.3.5",
        "enhanced-resolve": "^5.19.0",
        "jiti": "^2.6.1",
        "lightningcss": "1.31.1",
        "magic-string": "^0.30.21",
        "source-map-js": "^1.2.1",
        "tailwindcss": "4.2.1"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss/-/lightningcss-1.31.1.tgz",
      "integrity": "sha512-l51N2r93WmGUye3WuFoN5k10zyvrVs0qfKBhyC5ogUQ6Ew6JUSswh78mbSO+IU3nTWsyOArqPCcShdQSadghBQ==",
      "dev": true,
      "license": "MPL-2.0",
      "dependencies": {
        "detect-libc": "^2.0.3"
      },
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      },
      "optionalDependencies": {
        "lightningcss-android-arm64": "1.31.1",
        "lightningcss-darwin-arm64": "1.31.1",
        "lightningcss-darwin-x64": "1.31.1",
        "lightningcss-freebsd-x64": "1.31.1",
        "lightningcss-linux-arm-gnueabihf": "1.31.1",
        "lightningcss-linux-arm64-gnu": "1.31.1",
        "lightningcss-linux-arm64-musl": "1.31.1",
        "lightningcss-linux-x64-gnu": "1.31.1",
        "lightningcss-linux-x64-musl": "1.31.1",
        "lightningcss-win32-arm64-msvc": "1.31.1",
        "lightningcss-win32-x64-msvc": "1.31.1"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-android-arm64": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-android-arm64/-/lightningcss-android-arm64-1.31.1.tgz",
      "integrity": "sha512-HXJF3x8w9nQ4jbXRiNppBCqeZPIAfUo8zE/kOEGbW5NZvGc/K7nMxbhIr+YlFlHW5mpbg/YFPdbnCh1wAXCKFg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-darwin-arm64": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-darwin-arm64/-/lightningcss-darwin-arm64-1.31.1.tgz",
      "integrity": "sha512-02uTEqf3vIfNMq3h/z2cJfcOXnQ0GRwQrkmPafhueLb2h7mqEidiCzkE4gBMEH65abHRiQvhdcQ+aP0D0g67sg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-darwin-x64": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-darwin-x64/-/lightningcss-darwin-x64-1.31.1.tgz",
      "integrity": "sha512-1ObhyoCY+tGxtsz1lSx5NXCj3nirk0Y0kB/g8B8DT+sSx4G9djitg9ejFnjb3gJNWo7qXH4DIy2SUHvpoFwfTA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-freebsd-x64": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-freebsd-x64/-/lightningcss-freebsd-x64-1.31.1.tgz",
      "integrity": "sha512-1RINmQKAItO6ISxYgPwszQE1BrsVU5aB45ho6O42mu96UiZBxEXsuQ7cJW4zs4CEodPUioj/QrXW1r9pLUM74A==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-linux-arm-gnueabihf": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm-gnueabihf/-/lightningcss-linux-arm-gnueabihf-1.31.1.tgz",
      "integrity": "sha512-OOCm2//MZJ87CdDK62rZIu+aw9gBv4azMJuA8/KB74wmfS3lnC4yoPHm0uXZ/dvNNHmnZnB8XLAZzObeG0nS1g==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-linux-arm64-gnu": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm64-gnu/-/lightningcss-linux-arm64-gnu-1.31.1.tgz",
      "integrity": "sha512-WKyLWztD71rTnou4xAD5kQT+982wvca7E6QoLpoawZ1gP9JM0GJj4Tp5jMUh9B3AitHbRZ2/H3W5xQmdEOUlLg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-linux-arm64-musl": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm64-musl/-/lightningcss-linux-arm64-musl-1.31.1.tgz",
      "integrity": "sha512-mVZ7Pg2zIbe3XlNbZJdjs86YViQFoJSpc41CbVmKBPiGmC4YrfeOyz65ms2qpAobVd7WQsbW4PdsSJEMymyIMg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-linux-x64-gnu": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-x64-gnu/-/lightningcss-linux-x64-gnu-1.31.1.tgz",
      "integrity": "sha512-xGlFWRMl+0KvUhgySdIaReQdB4FNudfUTARn7q0hh/V67PVGCs3ADFjw+6++kG1RNd0zdGRlEKa+T13/tQjPMA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-linux-x64-musl": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-x64-musl/-/lightningcss-linux-x64-musl-1.31.1.tgz",
      "integrity": "sha512-eowF8PrKHw9LpoZii5tdZwnBcYDxRw2rRCyvAXLi34iyeYfqCQNA9rmUM0ce62NlPhCvof1+9ivRaTY6pSKDaA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-win32-arm64-msvc": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-win32-arm64-msvc/-/lightningcss-win32-arm64-msvc-1.31.1.tgz",
      "integrity": "sha512-aJReEbSEQzx1uBlQizAOBSjcmr9dCdL3XuC/6HLXAxmtErsj2ICo5yYggg1qOODQMtnjNQv2UHb9NpOuFtYe4w==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/node/node_modules/lightningcss-win32-x64-msvc": {
      "version": "1.31.1",
      "resolved": "https://registry.npmjs.org/lightningcss-win32-x64-msvc/-/lightningcss-win32-x64-msvc-1.31.1.tgz",
      "integrity": "sha512-I9aiFrbd7oYHwlnQDqr1Roz+fTz61oDDJX7n9tYF9FJymH1cIN1DtKw3iYt6b8WZgEjoNwVSncwF4wx/ZedMhw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@tailwindcss/oxide": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide/-/oxide-4.2.1.tgz",
      "integrity": "sha512-yv9jeEFWnjKCI6/T3Oq50yQEOqmpmpfzG1hcZsAOaXFQPfzWprWrlHSdGPEF3WQTi8zu8ohC9Mh9J470nT5pUw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 20"
      },
      "optionalDependencies": {
        "@tailwindcss/oxide-android-arm64": "4.2.1",
        "@tailwindcss/oxide-darwin-arm64": "4.2.1",
        "@tailwindcss/oxide-darwin-x64": "4.2.1",
        "@tailwindcss/oxide-freebsd-x64": "4.2.1",
        "@tailwindcss/oxide-linux-arm-gnueabihf": "4.2.1",
        "@tailwindcss/oxide-linux-arm64-gnu": "4.2.1",
        "@tailwindcss/oxide-linux-arm64-musl": "4.2.1",
        "@tailwindcss/oxide-linux-x64-gnu": "4.2.1",
        "@tailwindcss/oxide-linux-x64-musl": "4.2.1",
        "@tailwindcss/oxide-wasm32-wasi": "4.2.1",
        "@tailwindcss/oxide-win32-arm64-msvc": "4.2.1",
        "@tailwindcss/oxide-win32-x64-msvc": "4.2.1"
      }
    },
    "node_modules/@tailwindcss/oxide-android-arm64": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-android-arm64/-/oxide-android-arm64-4.2.1.tgz",
      "integrity": "sha512-eZ7G1Zm5EC8OOKaesIKuw77jw++QJ2lL9N+dDpdQiAB/c/B2wDh0QPFHbkBVrXnwNugvrbJFk1gK2SsVjwWReg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-darwin-arm64": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-darwin-arm64/-/oxide-darwin-arm64-4.2.1.tgz",
      "integrity": "sha512-q/LHkOstoJ7pI1J0q6djesLzRvQSIfEto148ppAd+BVQK0JYjQIFSK3JgYZJa+Yzi0DDa52ZsQx2rqytBnf8Hw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-darwin-x64": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-darwin-x64/-/oxide-darwin-x64-4.2.1.tgz",
      "integrity": "sha512-/f/ozlaXGY6QLbpvd/kFTro2l18f7dHKpB+ieXz+Cijl4Mt9AI2rTrpq7V+t04nK+j9XBQHnSMdeQRhbGyt6fw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-freebsd-x64": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-freebsd-x64/-/oxide-freebsd-x64-4.2.1.tgz",
      "integrity": "sha512-5e/AkgYJT/cpbkys/OU2Ei2jdETCLlifwm7ogMC7/hksI2fC3iiq6OcXwjibcIjPung0kRtR3TxEITkqgn0TcA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-linux-arm-gnueabihf": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-arm-gnueabihf/-/oxide-linux-arm-gnueabihf-4.2.1.tgz",
      "integrity": "sha512-Uny1EcVTTmerCKt/1ZuKTkb0x8ZaiuYucg2/kImO5A5Y/kBz41/+j0gxUZl+hTF3xkWpDmHX+TaWhOtba2Fyuw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-linux-arm64-gnu": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-arm64-gnu/-/oxide-linux-arm64-gnu-4.2.1.tgz",
      "integrity": "sha512-CTrwomI+c7n6aSSQlsPL0roRiNMDQ/YzMD9EjcR+H4f0I1SQ8QqIuPnsVp7QgMkC1Qi8rtkekLkOFjo7OlEFRQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-linux-arm64-musl": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-arm64-musl/-/oxide-linux-arm64-musl-4.2.1.tgz",
      "integrity": "sha512-WZA0CHRL/SP1TRbA5mp9htsppSEkWuQ4KsSUumYQnyl8ZdT39ntwqmz4IUHGN6p4XdSlYfJwM4rRzZLShHsGAQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-linux-x64-gnu": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-x64-gnu/-/oxide-linux-x64-gnu-4.2.1.tgz",
      "integrity": "sha512-qMFzxI2YlBOLW5PhblzuSWlWfwLHaneBE0xHzLrBgNtqN6mWfs+qYbhryGSXQjFYB1Dzf5w+LN5qbUTPhW7Y5g==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-linux-x64-musl": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-x64-musl/-/oxide-linux-x64-musl-4.2.1.tgz",
      "integrity": "sha512-5r1X2FKnCMUPlXTWRYpHdPYUY6a1Ar/t7P24OuiEdEOmms5lyqjDRvVY1yy9Rmioh+AunQ0rWiOTPE8F9A3v5g==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-wasm32-wasi": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-wasm32-wasi/-/oxide-wasm32-wasi-4.2.1.tgz",
      "integrity": "sha512-MGFB5cVPvshR85MTJkEvqDUnuNoysrsRxd6vnk1Lf2tbiqNlXpHYZqkqOQalydienEWOHHFyyuTSYRsLfxFJ2Q==",
      "bundleDependencies": [
        "@napi-rs/wasm-runtime",
        "@emnapi/core",
        "@emnapi/runtime",
        "@tybys/wasm-util",
        "@emnapi/wasi-threads",
        "tslib"
      ],
      "cpu": [
        "wasm32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/core": "^1.8.1",
        "@emnapi/runtime": "^1.8.1",
        "@emnapi/wasi-threads": "^1.1.0",
        "@napi-rs/wasm-runtime": "^1.1.1",
        "@tybys/wasm-util": "^0.10.1",
        "tslib": "^2.8.1"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@tailwindcss/oxide-win32-arm64-msvc": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-win32-arm64-msvc/-/oxide-win32-arm64-msvc-4.2.1.tgz",
      "integrity": "sha512-YlUEHRHBGnCMh4Nj4GnqQyBtsshUPdiNroZj8VPkvTZSoHsilRCwXcVKnG9kyi0ZFAS/3u+qKHBdDc81SADTRA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-win32-x64-msvc": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-win32-x64-msvc/-/oxide-win32-x64-msvc-4.2.1.tgz",
      "integrity": "sha512-rbO34G5sMWWyrN/idLeVxAZgAKWrn5LiR3/I90Q9MkA67s6T1oB0xtTe+0heoBvHSpbU9Mk7i6uwJnpo4u21XQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/postcss": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/@tailwindcss/postcss/-/postcss-4.2.1.tgz",
      "integrity": "sha512-OEwGIBnXnj7zJeonOh6ZG9woofIjGrd2BORfvE5p9USYKDCZoQmfqLcfNiRWoJlRWLdNPn2IgVZuWAOM4iTYMw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@alloc/quick-lru": "^5.2.0",
        "@tailwindcss/node": "4.2.1",
        "@tailwindcss/oxide": "4.2.1",
        "postcss": "^8.5.6",
        "tailwindcss": "4.2.1"
      }
    },
    "node_modules/@tybys/wasm-util": {
      "version": "0.10.1",
      "resolved": "https://registry.npmjs.org/@tybys/wasm-util/-/wasm-util-0.10.1.tgz",
      "integrity": "sha512-9tTaPJLSiejZKx+Bmog4uSubteqTvFrVrURwkmHixBo0G4seD0zUxp98E1DzUBJxLQ3NPwXrGKDiVjwx/DpPsg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@types/babel__core": {
      "version": "7.20.5",
      "resolved": "https://registry.npmjs.org/@types/babel__core/-/babel__core-7.20.5.tgz",
      "integrity": "sha512-qoQprZvz5wQFJwMDqeseRXWv3rqMvhgpbXFfVyWhbx9X47POIA6i/+dXefEmZKoAgOaTdaIgNSMqMIU61yRyzA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.20.7",
        "@babel/types": "^7.20.7",
        "@types/babel__generator": "*",
        "@types/babel__template": "*",
        "@types/babel__traverse": "*"
      }
    },
    "node_modules/@types/babel__generator": {
      "version": "7.27.0",
      "resolved": "https://registry.npmjs.org/@types/babel__generator/-/babel__generator-7.27.0.tgz",
      "integrity": "sha512-ufFd2Xi92OAVPYsy+P4n7/U7e68fex0+Ee8gSG9KX7eo084CWiQ4sdxktvdl0bOPupXtVJPY19zk6EwWqUQ8lg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.0.0"
      }
    },
    "node_modules/@types/babel__template": {
      "version": "7.4.4",
      "resolved": "https://registry.npmjs.org/@types/babel__template/-/babel__template-7.4.4.tgz",
      "integrity": "sha512-h/NUaSyG5EyxBIp8YRxo4RMe2/qQgvyowRwVMzhYhBCONbW8PUsg4lkFMrhgZhUe5z3L3MiLDuvyJ/CaPa2A8A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.1.0",
        "@babel/types": "^7.0.0"
      }
    },
    "node_modules/@types/babel__traverse": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@types/babel__traverse/-/babel__traverse-7.28.0.tgz",
      "integrity": "sha512-8PvcXf70gTDZBgt9ptxJ8elBeBjcLOAcOtoO/mPJjtji1+CdGbHgm77om1GrsPxsiE+uXIpNSK64UYaIwQXd4Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.28.2"
      }
    },
    "node_modules/@types/estree": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/@types/estree/-/estree-1.0.8.tgz",
      "integrity": "sha512-dWHzHa2WqEXI/O1E9OjrocMTKJl2mSrEolh1Iomrv6U+JuNwaHXsXx9bLu5gG7BUWFIN0skIQJQ/L1rIex4X6w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/json-schema": {
      "version": "7.0.15",
      "resolved": "https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz",
      "integrity": "sha512-5+fP8P8MFNC+AyZCDxrB2pkZFPGzqQWUzpSeuuVLvm8VMcorNYavBqoFcxK8bQz4Qsbn4oUEEem4wDLfcysGHA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/node": {
      "version": "24.12.0",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-24.12.0.tgz",
      "integrity": "sha512-GYDxsZi3ChgmckRT9HPU0WEhKLP08ev/Yfcq2AstjrDASOYCSXeyjDsHg4v5t4jOj7cyDX3vmprafKlWIG9MXQ==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "undici-types": "~7.16.0"
      }
    },
    "node_modules/@types/react": {
      "version": "19.2.14",
      "resolved": "https://registry.npmjs.org/@types/react/-/react-19.2.14.tgz",
      "integrity": "sha512-ilcTH/UniCkMdtexkoCN0bI7pMcJDvmQFPvuPvmEaYA/NSfFTAgdUSLAoVjaRJm7+6PvcM+q1zYOwS4wTYMF9w==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "csstype": "^3.2.2"
      }
    },
    "node_modules/@types/react-dom": {
      "version": "19.2.3",
      "resolved": "https://registry.npmjs.org/@types/react-dom/-/react-dom-19.2.3.tgz",
      "integrity": "sha512-jp2L/eY6fn+KgVVQAOqYItbF0VY/YApe5Mz2F0aykSO8gx31bYCZyvSeYxCHKvzHG5eZjc+zyaS5BrBWya2+kQ==",
      "dev": true,
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "^19.2.0"
      }
    },
    "node_modules/@typescript-eslint/eslint-plugin": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/@typescript-eslint/eslint-plugin/-/eslint-plugin-8.56.1.tgz",
      "integrity": "sha512-Jz9ZztpB37dNC+HU2HI28Bs9QXpzCz+y/twHOwhyrIRdbuVDxSytJNDl6z/aAKlaRIwC7y8wJdkBv7FxYGgi0A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@eslint-community/regexpp": "^4.12.2",
        "@typescript-eslint/scope-manager": "8.56.1",
        "@typescript-eslint/type-utils": "8.56.1",
        "@typescript-eslint/utils": "8.56.1",
        "@typescript-eslint/visitor-keys": "8.56.1",
        "ignore": "^7.0.5",
        "natural-compare": "^1.4.0",
        "ts-api-utils": "^2.4.0"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      },
      "peerDependencies": {
        "@typescript-eslint/parser": "^8.56.1",
        "eslint": "^8.57.0 || ^9.0.0 || ^10.0.0",
        "typescript": ">=4.8.4 <6.0.0"
      }
    },
    "node_modules/@typescript-eslint/eslint-plugin/node_modules/ignore": {
      "version": "7.0.5",
      "resolved": "https://registry.npmjs.org/ignore/-/ignore-7.0.5.tgz",
      "integrity": "sha512-Hs59xBNfUIunMFgWAbGX5cq6893IbWg4KnrjbYwX3tx0ztorVgTDA6B2sxf8ejHJ4wz8BqGUMYlnzNBer5NvGg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 4"
      }
    },
    "node_modules/@typescript-eslint/parser": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/@typescript-eslint/parser/-/parser-8.56.1.tgz",
      "integrity": "sha512-klQbnPAAiGYFyI02+znpBRLyjL4/BrBd0nyWkdC0s/6xFLkXYQ8OoRrSkqacS1ddVxf/LDyODIKbQ5TgKAf/Fg==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "@typescript-eslint/scope-manager": "8.56.1",
        "@typescript-eslint/types": "8.56.1",
        "@typescript-eslint/typescript-estree": "8.56.1",
        "@typescript-eslint/visitor-keys": "8.56.1",
        "debug": "^4.4.3"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      },
      "peerDependencies": {
        "eslint": "^8.57.0 || ^9.0.0 || ^10.0.0",
        "typescript": ">=4.8.4 <6.0.0"
      }
    },
    "node_modules/@typescript-eslint/project-service": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/@typescript-eslint/project-service/-/project-service-8.56.1.tgz",
      "integrity": "sha512-TAdqQTzHNNvlVFfR+hu2PDJrURiwKsUvxFn1M0h95BB8ah5jejas08jUWG4dBA68jDMI988IvtfdAI53JzEHOQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@typescript-eslint/tsconfig-utils": "^8.56.1",
        "@typescript-eslint/types": "^8.56.1",
        "debug": "^4.4.3"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      },
      "peerDependencies": {
        "typescript": ">=4.8.4 <6.0.0"
      }
    },
    "node_modules/@typescript-eslint/scope-manager": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/@typescript-eslint/scope-manager/-/scope-manager-8.56.1.tgz",
      "integrity": "sha512-YAi4VDKcIZp0O4tz/haYKhmIDZFEUPOreKbfdAN3SzUDMcPhJ8QI99xQXqX+HoUVq8cs85eRKnD+rne2UAnj2w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@typescript-eslint/types": "8.56.1",
        "@typescript-eslint/visitor-keys": "8.56.1"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      }
    },
    "node_modules/@typescript-eslint/tsconfig-utils": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/@typescript-eslint/tsconfig-utils/-/tsconfig-utils-8.56.1.tgz",
      "integrity": "sha512-qOtCYzKEeyr3aR9f28mPJqBty7+DBqsdd63eO0yyDwc6vgThj2UjWfJIcsFeSucYydqcuudMOprZ+x1SpF3ZuQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      },
      "peerDependencies": {
        "typescript": ">=4.8.4 <6.0.0"
      }
    },
    "node_modules/@typescript-eslint/type-utils": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/@typescript-eslint/type-utils/-/type-utils-8.56.1.tgz",
      "integrity": "sha512-yB/7dxi7MgTtGhZdaHCemf7PuwrHMenHjmzgUW1aJpO+bBU43OycnM3Wn+DdvDO/8zzA9HlhaJ0AUGuvri4oGg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@typescript-eslint/types": "8.56.1",
        "@typescript-eslint/typescript-estree": "8.56.1",
        "@typescript-eslint/utils": "8.56.1",
        "debug": "^4.4.3",
        "ts-api-utils": "^2.4.0"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      },
      "peerDependencies": {
        "eslint": "^8.57.0 || ^9.0.0 || ^10.0.0",
        "typescript": ">=4.8.4 <6.0.0"
      }
    },
    "node_modules/@typescript-eslint/types": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/@typescript-eslint/types/-/types-8.56.1.tgz",
      "integrity": "sha512-dbMkdIUkIkchgGDIv7KLUpa0Mda4IYjo4IAMJUZ+3xNoUXxMsk9YtKpTHSChRS85o+H9ftm51gsK1dZReY9CVw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      }
    },
    "node_modules/@typescript-eslint/typescript-estree": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/@typescript-eslint/typescript-estree/-/typescript-estree-8.56.1.tgz",
      "integrity": "sha512-qzUL1qgalIvKWAf9C1HpvBjif+Vm6rcT5wZd4VoMb9+Km3iS3Cv9DY6dMRMDtPnwRAFyAi7YXJpTIEXLvdfPxg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@typescript-eslint/project-service": "8.56.1",
        "@typescript-eslint/tsconfig-utils": "8.56.1",
        "@typescript-eslint/types": "8.56.1",
        "@typescript-eslint/visitor-keys": "8.56.1",
        "debug": "^4.4.3",
        "minimatch": "^10.2.2",
        "semver": "^7.7.3",
        "tinyglobby": "^0.2.15",
        "ts-api-utils": "^2.4.0"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      },
      "peerDependencies": {
        "typescript": ">=4.8.4 <6.0.0"
      }
    },
    "node_modules/@typescript-eslint/typescript-estree/node_modules/balanced-match": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-4.0.4.tgz",
      "integrity": "sha512-BLrgEcRTwX2o6gGxGOCNyMvGSp35YofuYzw9h1IMTRmKqttAZZVU67bdb9Pr2vUHA8+j3i2tJfjO6C6+4myGTA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "18 || 20 || >=22"
      }
    },
    "node_modules/@typescript-eslint/typescript-estree/node_modules/brace-expansion": {
      "version": "5.0.4",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-5.0.4.tgz",
      "integrity": "sha512-h+DEnpVvxmfVefa4jFbCf5HdH5YMDXRsmKflpf1pILZWRFlTbJpxeU55nJl4Smt5HQaGzg1o6RHFPJaOqnmBDg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "balanced-match": "^4.0.2"
      },
      "engines": {
        "node": "18 || 20 || >=22"
      }
    },
    "node_modules/@typescript-eslint/typescript-estree/node_modules/minimatch": {
      "version": "10.2.4",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-10.2.4.tgz",
      "integrity": "sha512-oRjTw/97aTBN0RHbYCdtF1MQfvusSIBQM0IZEgzl6426+8jSC0nF1a/GmnVLpfB9yyr6g6FTqWqiZVbxrtaCIg==",
      "dev": true,
      "license": "BlueOak-1.0.0",
      "dependencies": {
        "brace-expansion": "^5.0.2"
      },
      "engines": {
        "node": "18 || 20 || >=22"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/@typescript-eslint/typescript-estree/node_modules/semver": {
      "version": "7.7.4",
      "resolved": "https://registry.npmjs.org/semver/-/semver-7.7.4.tgz",
      "integrity": "sha512-vFKC2IEtQnVhpT78h1Yp8wzwrf8CM+MzKMHGJZfBtzhZNycRFnXsHk6E5TxIkkMsgNS7mdX3AGB7x2QM2di4lA==",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@typescript-eslint/utils": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/@typescript-eslint/utils/-/utils-8.56.1.tgz",
      "integrity": "sha512-HPAVNIME3tABJ61siYlHzSWCGtOoeP2RTIaHXFMPqjrQKCGB9OgUVdiNgH7TJS2JNIQ5qQ4RsAUDuGaGme/KOA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@eslint-community/eslint-utils": "^4.9.1",
        "@typescript-eslint/scope-manager": "8.56.1",
        "@typescript-eslint/types": "8.56.1",
        "@typescript-eslint/typescript-estree": "8.56.1"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      },
      "peerDependencies": {
        "eslint": "^8.57.0 || ^9.0.0 || ^10.0.0",
        "typescript": ">=4.8.4 <6.0.0"
      }
    },
    "node_modules/@typescript-eslint/visitor-keys": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/@typescript-eslint/visitor-keys/-/visitor-keys-8.56.1.tgz",
      "integrity": "sha512-KiROIzYdEV85YygXw6BI/Dx4fnBlFQu6Mq4QE4MOH9fFnhohw6wX/OAvDY2/C+ut0I3RSPKenvZJIVYqJNkhEw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@typescript-eslint/types": "8.56.1",
        "eslint-visitor-keys": "^5.0.0"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      }
    },
    "node_modules/@typescript-eslint/visitor-keys/node_modules/eslint-visitor-keys": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-5.0.1.tgz",
      "integrity": "sha512-tD40eHxA35h0PEIZNeIjkHoDR4YjjJp34biM0mDvplBe//mB+IHCqHDGV7pxF+7MklTvighcCPPZC7ynWyjdTA==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/@vitejs/plugin-react": {
      "version": "5.1.4",
      "resolved": "https://registry.npmjs.org/@vitejs/plugin-react/-/plugin-react-5.1.4.tgz",
      "integrity": "sha512-VIcFLdRi/VYRU8OL/puL7QXMYafHmqOnwTZY50U1JPlCNj30PxCMx65c494b1K9be9hX83KVt0+gTEwTWLqToA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/core": "^7.29.0",
        "@babel/plugin-transform-react-jsx-self": "^7.27.1",
        "@babel/plugin-transform-react-jsx-source": "^7.27.1",
        "@rolldown/pluginutils": "1.0.0-rc.3",
        "@types/babel__core": "^7.20.5",
        "react-refresh": "^0.18.0"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "peerDependencies": {
        "vite": "^4.2.0 || ^5.0.0 || ^6.0.0 || ^7.0.0"
      }
    },
    "node_modules/acorn": {
      "version": "8.16.0",
      "resolved": "https://registry.npmjs.org/acorn/-/acorn-8.16.0.tgz",
      "integrity": "sha512-UVJyE9MttOsBQIDKw1skb9nAwQuR5wuGD3+82K6JgJlm/Y+KI92oNsMNGZCYdDsVtRHSak0pcV5Dno5+4jh9sw==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "bin": {
        "acorn": "bin/acorn"
      },
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/acorn-jsx": {
      "version": "5.3.2",
      "resolved": "https://registry.npmjs.org/acorn-jsx/-/acorn-jsx-5.3.2.tgz",
      "integrity": "sha512-rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==",
      "dev": true,
      "license": "MIT",
      "peerDependencies": {
        "acorn": "^6.0.0 || ^7.0.0 || ^8.0.0"
      }
    },
    "node_modules/ajv": {
      "version": "6.14.0",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-6.14.0.tgz",
      "integrity": "sha512-IWrosm/yrn43eiKqkfkHis7QioDleaXQHdDVPKg0FSwwd/DuvyX79TZnFOnYpB7dcsFAMmtFztZuXPDvSePkFw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fast-deep-equal": "^3.1.1",
        "fast-json-stable-stringify": "^2.0.0",
        "json-schema-traverse": "^0.4.1",
        "uri-js": "^4.2.2"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/epoberezkin"
      }
    },
    "node_modules/ansi-styles": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
      "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "color-convert": "^2.0.1"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/argparse": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/argparse/-/argparse-2.0.1.tgz",
      "integrity": "sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==",
      "dev": true,
      "license": "Python-2.0"
    },
    "node_modules/autoprefixer": {
      "version": "10.4.27",
      "resolved": "https://registry.npmjs.org/autoprefixer/-/autoprefixer-10.4.27.tgz",
      "integrity": "sha512-NP9APE+tO+LuJGn7/9+cohklunJsXWiaWEfV3si4Gi/XHDwVNgkwr1J3RQYFIvPy76GmJ9/bW8vyoU1LcxwKHA==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/autoprefixer"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "browserslist": "^4.28.1",
        "caniuse-lite": "^1.0.30001774",
        "fraction.js": "^5.3.4",
        "picocolors": "^1.1.1",
        "postcss-value-parser": "^4.2.0"
      },
      "bin": {
        "autoprefixer": "bin/autoprefixer"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      },
      "peerDependencies": {
        "postcss": "^8.1.0"
      }
    },
    "node_modules/balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/baseline-browser-mapping": {
      "version": "2.10.0",
      "resolved": "https://registry.npmjs.org/baseline-browser-mapping/-/baseline-browser-mapping-2.10.0.tgz",
      "integrity": "sha512-lIyg0szRfYbiy67j9KN8IyeD7q7hcmqnJ1ddWmNt19ItGpNN64mnllmxUNFIOdOm6by97jlL6wfpTTJrmnjWAA==",
      "license": "Apache-2.0",
      "bin": {
        "baseline-browser-mapping": "dist/cli.cjs"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/brace-expansion": {
      "version": "1.1.12",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.12.tgz",
      "integrity": "sha512-9T9UjW3r0UW5c1Q7GTwllptXwhvYmEzFhzMfZ9H7FQWt+uZePjZPjBP/W1ZEyZ1twGWom5/56TF4lPcqjnDHcg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "balanced-match": "^1.0.0",
        "concat-map": "0.0.1"
      }
    },
    "node_modules/browserslist": {
      "version": "4.28.1",
      "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-4.28.1.tgz",
      "integrity": "sha512-ZC5Bd0LgJXgwGqUknZY/vkUQ04r8NXnJZ3yYi4vDmSiZmC/pdSN0NbNRPxZpbtO4uAfDUAFffO8IZoM3Gj8IkA==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "baseline-browser-mapping": "^2.9.0",
        "caniuse-lite": "^1.0.30001759",
        "electron-to-chromium": "^1.5.263",
        "node-releases": "^2.0.27",
        "update-browserslist-db": "^1.2.0"
      },
      "bin": {
        "browserslist": "cli.js"
      },
      "engines": {
        "node": "^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7"
      }
    },
    "node_modules/callsites": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/callsites/-/callsites-3.1.0.tgz",
      "integrity": "sha512-P8BjAsXvZS+VIDUI11hHCQEv74YT67YUi5JJFNWIqL235sBmjX4+qx9Muvls5ivyNENctx46xQLQ3aTuE7ssaQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/caniuse-lite": {
      "version": "1.0.30001777",
      "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001777.tgz",
      "integrity": "sha512-tmN+fJxroPndC74efCdp12j+0rk0RHwV5Jwa1zWaFVyw2ZxAuPeG8ZgWC3Wz7uSjT3qMRQ5XHZ4COgQmsCMJAQ==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/caniuse-lite"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "CC-BY-4.0"
    },
    "node_modules/chalk": {
      "version": "4.1.2",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-4.1.2.tgz",
      "integrity": "sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-styles": "^4.1.0",
        "supports-color": "^7.1.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/color-convert": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
      "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "color-name": "~1.1.4"
      },
      "engines": {
        "node": ">=7.0.0"
      }
    },
    "node_modules/color-name": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
      "integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/convert-source-map": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-2.0.0.tgz",
      "integrity": "sha512-Kvp459HrV2FEJ1CAsi1Ku+MY3kasH19TFykTz2xWmMeq6bk2NU3XXvfJ+Q61m0xktWwt+1HSYf3JZsTms3aRJg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/cookie": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-1.1.1.tgz",
      "integrity": "sha512-ei8Aos7ja0weRpFzJnEA9UHJ/7XQmqglbRwnf2ATjcB9Wq874VKH9kfjjirM6UhU2/E5fFYadylyhFldcqSidQ==",
      "license": "MIT",
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/cross-spawn": {
      "version": "7.0.6",
      "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz",
      "integrity": "sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "path-key": "^3.1.0",
        "shebang-command": "^2.0.0",
        "which": "^2.0.1"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/csstype": {
      "version": "3.2.3",
      "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.2.3.tgz",
      "integrity": "sha512-z1HGKcYy2xA8AGQfwrn0PAy+PB7X/GSj3UVJW9qKyn43xWa+gl5nXmU4qqLMRzWVLFC8KusUX8T/0kCiOYpAIQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/deep-is": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/deep-is/-/deep-is-0.1.4.tgz",
      "integrity": "sha512-oIPzksmTg4/MriiaYGO+okXDT7ztn/w3Eptv/+gSIdMdKsJo0u4CfYNFJPy+4SKMuCqGw2wxnA+URMg3t8a/bQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/detect-libc": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/detect-libc/-/detect-libc-2.1.2.tgz",
      "integrity": "sha512-Btj2BOOO83o3WyH59e8MgXsxEQVcarkUOpEYrubB0urwnN10yQ364rsiByU11nZlqWYZm05i/of7io4mzihBtQ==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/electron-to-chromium": {
      "version": "1.5.307",
      "resolved": "https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.307.tgz",
      "integrity": "sha512-5z3uFKBWjiNR44nFcYdkcXjKMbg5KXNdciu7mhTPo9tB7NbqSNP2sSnGR+fqknZSCwKkBN+oxiiajWs4dT6ORg==",
      "license": "ISC"
    },
    "node_modules/enhanced-resolve": {
      "version": "5.20.0",
      "resolved": "https://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-5.20.0.tgz",
      "integrity": "sha512-/ce7+jQ1PQ6rVXwe+jKEg5hW5ciicHwIQUagZkp6IufBoY3YDgdTTY1azVs0qoRgVmvsNB+rbjLJxDAeHHtwsQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "graceful-fs": "^4.2.4",
        "tapable": "^2.3.0"
      },
      "engines": {
        "node": ">=10.13.0"
      }
    },
    "node_modules/escalade": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
      "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/escape-string-regexp": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-4.0.0.tgz",
      "integrity": "sha512-TtpcNJ3XAzx3Gq8sWRzJaVajRs0uVxA2YAkdb1jm2YkPz4G6egUFAyA3n5vtEIZefPk5Wa4UXbKuS5fKkJWdgA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/eslint": {
      "version": "9.39.4",
      "resolved": "https://registry.npmjs.org/eslint/-/eslint-9.39.4.tgz",
      "integrity": "sha512-XoMjdBOwe/esVgEvLmNsD3IRHkm7fbKIUGvrleloJXUZgDHig2IPWNniv+GwjyJXzuNqVjlr5+4yVUZjycJwfQ==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "@eslint-community/eslint-utils": "^4.8.0",
        "@eslint-community/regexpp": "^4.12.1",
        "@eslint/config-array": "^0.21.2",
        "@eslint/config-helpers": "^0.4.2",
        "@eslint/core": "^0.17.0",
        "@eslint/eslintrc": "^3.3.5",
        "@eslint/js": "9.39.4",
        "@eslint/plugin-kit": "^0.4.1",
        "@humanfs/node": "^0.16.6",
        "@humanwhocodes/module-importer": "^1.0.1",
        "@humanwhocodes/retry": "^0.4.2",
        "@types/estree": "^1.0.6",
        "ajv": "^6.14.0",
        "chalk": "^4.0.0",
        "cross-spawn": "^7.0.6",
        "debug": "^4.3.2",
        "escape-string-regexp": "^4.0.0",
        "eslint-scope": "^8.4.0",
        "eslint-visitor-keys": "^4.2.1",
        "espree": "^10.4.0",
        "esquery": "^1.5.0",
        "esutils": "^2.0.2",
        "fast-deep-equal": "^3.1.3",
        "file-entry-cache": "^8.0.0",
        "find-up": "^5.0.0",
        "glob-parent": "^6.0.2",
        "ignore": "^5.2.0",
        "imurmurhash": "^0.1.4",
        "is-glob": "^4.0.0",
        "json-stable-stringify-without-jsonify": "^1.0.1",
        "lodash.merge": "^4.6.2",
        "minimatch": "^3.1.5",
        "natural-compare": "^1.4.0",
        "optionator": "^0.9.3"
      },
      "bin": {
        "eslint": "bin/eslint.js"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "url": "https://eslint.org/donate"
      },
      "peerDependencies": {
        "jiti": "*"
      },
      "peerDependenciesMeta": {
        "jiti": {
          "optional": true
        }
      }
    },
    "node_modules/eslint-plugin-react-hooks": {
      "version": "7.0.1",
      "resolved": "https://registry.npmjs.org/eslint-plugin-react-hooks/-/eslint-plugin-react-hooks-7.0.1.tgz",
      "integrity": "sha512-O0d0m04evaNzEPoSW+59Mezf8Qt0InfgGIBJnpC0h3NH/WjUAR7BIKUfysC6todmtiZ/A0oUVS8Gce0WhBrHsA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/core": "^7.24.4",
        "@babel/parser": "^7.24.4",
        "hermes-parser": "^0.25.1",
        "zod": "^3.25.0 || ^4.0.0",
        "zod-validation-error": "^3.5.0 || ^4.0.0"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "eslint": "^3.0.0 || ^4.0.0 || ^5.0.0 || ^6.0.0 || ^7.0.0 || ^8.0.0-0 || ^9.0.0"
      }
    },
    "node_modules/eslint-plugin-react-refresh": {
      "version": "0.4.26",
      "resolved": "https://registry.npmjs.org/eslint-plugin-react-refresh/-/eslint-plugin-react-refresh-0.4.26.tgz",
      "integrity": "sha512-1RETEylht2O6FM/MvgnyvT+8K21wLqDNg4qD51Zj3guhjt433XbnnkVttHMyaVyAFD03QSV4LPS5iE3VQmO7XQ==",
      "dev": true,
      "license": "MIT",
      "peerDependencies": {
        "eslint": ">=8.40"
      }
    },
    "node_modules/eslint-scope": {
      "version": "8.4.0",
      "resolved": "https://registry.npmjs.org/eslint-scope/-/eslint-scope-8.4.0.tgz",
      "integrity": "sha512-sNXOfKCn74rt8RICKMvJS7XKV/Xk9kA7DyJr8mJik3S7Cwgy3qlkkmyS2uQB3jiJg6VNdZd/pDBJu0nvG2NlTg==",
      "dev": true,
      "license": "BSD-2-Clause",
      "dependencies": {
        "esrecurse": "^4.3.0",
        "estraverse": "^5.2.0"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/eslint-visitor-keys": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-4.2.1.tgz",
      "integrity": "sha512-Uhdk5sfqcee/9H/rCOJikYz67o0a2Tw2hGRPOG2Y1R2dg7brRe1uG0yaNQDHu+TO/uQPF/5eCapvYSmHUjt7JQ==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/espree": {
      "version": "10.4.0",
      "resolved": "https://registry.npmjs.org/espree/-/espree-10.4.0.tgz",
      "integrity": "sha512-j6PAQ2uUr79PZhBjP5C5fhl8e39FmRnOjsD5lGnWrFU8i2G776tBK7+nP8KuQUTTyAZUwfQqXAgrVH5MbH9CYQ==",
      "dev": true,
      "license": "BSD-2-Clause",
      "dependencies": {
        "acorn": "^8.15.0",
        "acorn-jsx": "^5.3.2",
        "eslint-visitor-keys": "^4.2.1"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/esquery": {
      "version": "1.7.0",
      "resolved": "https://registry.npmjs.org/esquery/-/esquery-1.7.0.tgz",
      "integrity": "sha512-Ap6G0WQwcU/LHsvLwON1fAQX9Zp0A2Y6Y/cJBl9r/JbW90Zyg4/zbG6zzKa2OTALELarYHmKu0GhpM5EO+7T0g==",
      "dev": true,
      "license": "BSD-3-Clause",
      "dependencies": {
        "estraverse": "^5.1.0"
      },
      "engines": {
        "node": ">=0.10"
      }
    },
    "node_modules/esrecurse": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/esrecurse/-/esrecurse-4.3.0.tgz",
      "integrity": "sha512-KmfKL3b6G+RXvP8N1vr3Tq1kL/oCFgn2NYXEtqP8/L3pKapUA4G8cFVaoF3SU323CD4XypR/ffioHmkti6/Tag==",
      "dev": true,
      "license": "BSD-2-Clause",
      "dependencies": {
        "estraverse": "^5.2.0"
      },
      "engines": {
        "node": ">=4.0"
      }
    },
    "node_modules/estraverse": {
      "version": "5.3.0",
      "resolved": "https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz",
      "integrity": "sha512-MMdARuVEQziNTeJD8DgMqmhwR11BRQ/cBP+pLtYdSTnf3MIO8fFeiINEbX36ZdNlfU/7A9f3gUw49B3oQsvwBA==",
      "dev": true,
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=4.0"
      }
    },
    "node_modules/esutils": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz",
      "integrity": "sha512-kVscqXk4OCp68SZ0dkgEKVi6/8ij300KBWTJq32P/dYeWTSwK41WyTxalN1eRmA5Z9UU/LX9D7FWSmV9SAYx6g==",
      "dev": true,
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/fast-deep-equal": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz",
      "integrity": "sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/fast-json-stable-stringify": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz",
      "integrity": "sha512-lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/fast-levenshtein": {
      "version": "2.0.6",
      "resolved": "https://registry.npmjs.org/fast-levenshtein/-/fast-levenshtein-2.0.6.tgz",
      "integrity": "sha512-DCXu6Ifhqcks7TZKY3Hxp3y6qphY5SJZmrWMDrKcERSOXWQdMhU9Ig/PYrzyw/ul9jOIyh0N4M0tbC5hodg8dw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/fdir": {
      "version": "6.5.0",
      "resolved": "https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz",
      "integrity": "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12.0.0"
      },
      "peerDependencies": {
        "picomatch": "^3 || ^4"
      },
      "peerDependenciesMeta": {
        "picomatch": {
          "optional": true
        }
      }
    },
    "node_modules/file-entry-cache": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/file-entry-cache/-/file-entry-cache-8.0.0.tgz",
      "integrity": "sha512-XXTUwCvisa5oacNGRP9SfNtYBNAMi+RPwBFmblZEF7N7swHYQS6/Zfk7SRwx4D5j3CH211YNRco1DEMNVfZCnQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "flat-cache": "^4.0.0"
      },
      "engines": {
        "node": ">=16.0.0"
      }
    },
    "node_modules/find-up": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/find-up/-/find-up-5.0.0.tgz",
      "integrity": "sha512-78/PXT1wlLLDgTzDs7sjq9hzz0vXD+zn+7wypEe4fXQxCmdmqfGsEPQxmiCSQI3ajFV91bVSsvNtrJRiW6nGng==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "locate-path": "^6.0.0",
        "path-exists": "^4.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/flat-cache": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/flat-cache/-/flat-cache-4.0.1.tgz",
      "integrity": "sha512-f7ccFPK3SXFHpx15UIGyRJ/FJQctuKZ0zVuN3frBo4HnK3cay9VEW0R6yPYFHC0AgqhukPzKjq22t5DmAyqGyw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "flatted": "^3.2.9",
        "keyv": "^4.5.4"
      },
      "engines": {
        "node": ">=16"
      }
    },
    "node_modules/flatted": {
      "version": "3.4.1",
      "resolved": "https://registry.npmjs.org/flatted/-/flatted-3.4.1.tgz",
      "integrity": "sha512-IxfVbRFVlV8V/yRaGzk0UVIcsKKHMSfYw66T/u4nTwlWteQePsxe//LjudR1AMX4tZW3WFCh3Zqa/sjlqpbURQ==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/fraction.js": {
      "version": "5.3.4",
      "resolved": "https://registry.npmjs.org/fraction.js/-/fraction.js-5.3.4.tgz",
      "integrity": "sha512-1X1NTtiJphryn/uLQz3whtY6jK3fTqoE3ohKs0tT+Ujr1W59oopxmoEh7Lu5p6vBaPbgoM0bzveAW4Qi5RyWDQ==",
      "license": "MIT",
      "engines": {
        "node": "*"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/rawify"
      }
    },
    "node_modules/fsevents": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
      "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
      }
    },
    "node_modules/gensync": {
      "version": "1.0.0-beta.2",
      "resolved": "https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.2.tgz",
      "integrity": "sha512-3hN7NaskYvMDLQY55gnW3NQ+mesEAepTqlg+VEbj7zzqEMBVNhzcGYYeqFo/TlYz6eQiFcp1HcsCZO+nGgS8zg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/glob-parent": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz",
      "integrity": "sha512-XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.3"
      },
      "engines": {
        "node": ">=10.13.0"
      }
    },
    "node_modules/globals": {
      "version": "16.5.0",
      "resolved": "https://registry.npmjs.org/globals/-/globals-16.5.0.tgz",
      "integrity": "sha512-c/c15i26VrJ4IRt5Z89DnIzCGDn9EcebibhAOjw5ibqEHsE1wLUgkPn9RDmNcUKyU87GeaL633nyJ+pplFR2ZQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/graceful-fs": {
      "version": "4.2.11",
      "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz",
      "integrity": "sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/has-flag": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz",
      "integrity": "sha512-EykJT/Q1KjTWctppgIAgfSO0tKVuZUjhgMr17kqTumMl6Afv3EISleU7qZUzoXDFTAHTDC4NOoG/ZxU3EvlMPQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/hermes-estree": {
      "version": "0.25.1",
      "resolved": "https://registry.npmjs.org/hermes-estree/-/hermes-estree-0.25.1.tgz",
      "integrity": "sha512-0wUoCcLp+5Ev5pDW2OriHC2MJCbwLwuRx+gAqMTOkGKJJiBCLjtrvy4PWUGn6MIVefecRpzoOZ/UV6iGdOr+Cw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/hermes-parser": {
      "version": "0.25.1",
      "resolved": "https://registry.npmjs.org/hermes-parser/-/hermes-parser-0.25.1.tgz",
      "integrity": "sha512-6pEjquH3rqaI6cYAXYPcz9MS4rY6R4ngRgrgfDshRptUZIc3lw0MCIJIGDj9++mfySOuPTHB4nrSW99BCvOPIA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "hermes-estree": "0.25.1"
      }
    },
    "node_modules/ignore": {
      "version": "5.3.2",
      "resolved": "https://registry.npmjs.org/ignore/-/ignore-5.3.2.tgz",
      "integrity": "sha512-hsBTNUqQTDwkWtcdYI2i06Y/nUBEsNEDJKjWdigLvegy8kDuJAS8uRlpkkcQpyEXL0Z/pjDy5HBmMjRCJ2gq+g==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 4"
      }
    },
    "node_modules/import-fresh": {
      "version": "3.3.1",
      "resolved": "https://registry.npmjs.org/import-fresh/-/import-fresh-3.3.1.tgz",
      "integrity": "sha512-TR3KfrTZTYLPB6jUjfx6MF9WcWrHL9su5TObK4ZkYgBdWKPOFoSoQIdEuTuR82pmtxH2spWG9h6etwfr1pLBqQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "parent-module": "^1.0.0",
        "resolve-from": "^4.0.0"
      },
      "engines": {
        "node": ">=6"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/imurmurhash": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz",
      "integrity": "sha512-JmXMZ6wuvDmLiHEml9ykzqO6lwFbof0GG4IkcGaENdCRDDmMVnny7s5HsIgHCbaq0w2MyPhDqkhTUgS2LU2PHA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.8.19"
      }
    },
    "node_modules/is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-extglob": "^2.1.1"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/isexe": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz",
      "integrity": "sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/jiti": {
      "version": "2.6.1",
      "resolved": "https://registry.npmjs.org/jiti/-/jiti-2.6.1.tgz",
      "integrity": "sha512-ekilCSN1jwRvIbgeg/57YFh8qQDNbwDb9xT/qu2DAHbFFZUicIl4ygVaAvzveMhMVr3LnpSKTNnwt8PoOfmKhQ==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "bin": {
        "jiti": "lib/jiti-cli.mjs"
      }
    },
    "node_modules/js-tokens": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
      "integrity": "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/js-yaml": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/js-yaml/-/js-yaml-4.1.1.tgz",
      "integrity": "sha512-qQKT4zQxXl8lLwBtHMWwaTcGfFOZviOJet3Oy/xmGk2gZH677CJM9EvtfdSkgWcATZhj/55JZ0rmy3myCT5lsA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "argparse": "^2.0.1"
      },
      "bin": {
        "js-yaml": "bin/js-yaml.js"
      }
    },
    "node_modules/jsesc": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz",
      "integrity": "sha512-/sM3dO2FOzXjKQhJuo0Q173wf2KOo8t4I8vHy6lF9poUp7bKT0/NHE8fPX23PwfhnykfqnC2xRxOnVw5XuGIaA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "jsesc": "bin/jsesc"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/json-buffer": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/json-buffer/-/json-buffer-3.0.1.tgz",
      "integrity": "sha512-4bV5BfR2mqfQTJm+V5tPPdf+ZpuhiIvTuAB5g8kcrXOZpTT/QwwVRWBywX1ozr6lEuPdbHxwaJlm9G6mI2sfSQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/json-schema-traverse": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz",
      "integrity": "sha512-xbbCH5dCYU5T8LcEhhuh7HJ88HXuW3qsI3Y0zOZFKfZEHcpWiHU/Jxzk629Brsab/mMiHQti9wMP+845RPe3Vg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/json-stable-stringify-without-jsonify": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/json-stable-stringify-without-jsonify/-/json-stable-stringify-without-jsonify-1.0.1.tgz",
      "integrity": "sha512-Bdboy+l7tA3OGW6FjyFHWkP5LuByj1Tk33Ljyq0axyzdk9//JSi2u3fP1QSmd1KNwq6VOKYGlAu87CisVir6Pw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/json5": {
      "version": "2.2.3",
      "resolved": "https://registry.npmjs.org/json5/-/json5-2.2.3.tgz",
      "integrity": "sha512-XmOWe7eyHYH14cLdVPoyg+GOH3rYX++KpzrylJwSW98t3Nk+U8XOl8FWKOgwtzdb8lXGf6zYwDUzeHMWfxasyg==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "json5": "lib/cli.js"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/keyv": {
      "version": "4.5.4",
      "resolved": "https://registry.npmjs.org/keyv/-/keyv-4.5.4.tgz",
      "integrity": "sha512-oxVHkHR/EJf2CNXnWxRLW6mg7JyCCUcG0DtEGmL2ctUo1PNTin1PUil+r/+4r5MpVgC/fn1kjsx7mjSujKqIpw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "json-buffer": "3.0.1"
      }
    },
    "node_modules/levn": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/levn/-/levn-0.4.1.tgz",
      "integrity": "sha512-+bT2uH4E5LGE7h/n3evcS/sQlJXCpIp6ym8OWJ5eV6+67Dsql/LaaT7qJBAt2rzfoa/5QBGBhxDix1dMt2kQKQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "prelude-ls": "^1.2.1",
        "type-check": "~0.4.0"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/lightningcss": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss/-/lightningcss-1.32.0.tgz",
      "integrity": "sha512-NXYBzinNrblfraPGyrbPoD19C1h9lfI/1mzgWYvXUTe414Gz/X1FD2XBZSZM7rRTrMA8JL3OtAaGifrIKhQ5yQ==",
      "dev": true,
      "license": "MPL-2.0",
      "dependencies": {
        "detect-libc": "^2.0.3"
      },
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      },
      "optionalDependencies": {
        "lightningcss-android-arm64": "1.32.0",
        "lightningcss-darwin-arm64": "1.32.0",
        "lightningcss-darwin-x64": "1.32.0",
        "lightningcss-freebsd-x64": "1.32.0",
        "lightningcss-linux-arm-gnueabihf": "1.32.0",
        "lightningcss-linux-arm64-gnu": "1.32.0",
        "lightningcss-linux-arm64-musl": "1.32.0",
        "lightningcss-linux-x64-gnu": "1.32.0",
        "lightningcss-linux-x64-musl": "1.32.0",
        "lightningcss-win32-arm64-msvc": "1.32.0",
        "lightningcss-win32-x64-msvc": "1.32.0"
      }
    },
    "node_modules/lightningcss-android-arm64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-android-arm64/-/lightningcss-android-arm64-1.32.0.tgz",
      "integrity": "sha512-YK7/ClTt4kAK0vo6w3X+Pnm0D2cf2vPHbhOXdoNti1Ga0al1P4TBZhwjATvjNwLEBCnKvjJc2jQgHXH0NEwlAg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-darwin-arm64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-darwin-arm64/-/lightningcss-darwin-arm64-1.32.0.tgz",
      "integrity": "sha512-RzeG9Ju5bag2Bv1/lwlVJvBE3q6TtXskdZLLCyfg5pt+HLz9BqlICO7LZM7VHNTTn/5PRhHFBSjk5lc4cmscPQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-darwin-x64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-darwin-x64/-/lightningcss-darwin-x64-1.32.0.tgz",
      "integrity": "sha512-U+QsBp2m/s2wqpUYT/6wnlagdZbtZdndSmut/NJqlCcMLTWp5muCrID+K5UJ6jqD2BFshejCYXniPDbNh73V8w==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-freebsd-x64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-freebsd-x64/-/lightningcss-freebsd-x64-1.32.0.tgz",
      "integrity": "sha512-JCTigedEksZk3tHTTthnMdVfGf61Fky8Ji2E4YjUTEQX14xiy/lTzXnu1vwiZe3bYe0q+SpsSH/CTeDXK6WHig==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-arm-gnueabihf": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm-gnueabihf/-/lightningcss-linux-arm-gnueabihf-1.32.0.tgz",
      "integrity": "sha512-x6rnnpRa2GL0zQOkt6rts3YDPzduLpWvwAF6EMhXFVZXD4tPrBkEFqzGowzCsIWsPjqSK+tyNEODUBXeeVHSkw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-arm64-gnu": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm64-gnu/-/lightningcss-linux-arm64-gnu-1.32.0.tgz",
      "integrity": "sha512-0nnMyoyOLRJXfbMOilaSRcLH3Jw5z9HDNGfT/gwCPgaDjnx0i8w7vBzFLFR1f6CMLKF8gVbebmkUN3fa/kQJpQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-arm64-musl": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm64-musl/-/lightningcss-linux-arm64-musl-1.32.0.tgz",
      "integrity": "sha512-UpQkoenr4UJEzgVIYpI80lDFvRmPVg6oqboNHfoH4CQIfNA+HOrZ7Mo7KZP02dC6LjghPQJeBsvXhJod/wnIBg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-x64-gnu": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-x64-gnu/-/lightningcss-linux-x64-gnu-1.32.0.tgz",
      "integrity": "sha512-V7Qr52IhZmdKPVr+Vtw8o+WLsQJYCTd8loIfpDaMRWGUZfBOYEJeyJIkqGIDMZPwPx24pUMfwSxxI8phr/MbOA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-x64-musl": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-x64-musl/-/lightningcss-linux-x64-musl-1.32.0.tgz",
      "integrity": "sha512-bYcLp+Vb0awsiXg/80uCRezCYHNg1/l3mt0gzHnWV9XP1W5sKa5/TCdGWaR/zBM2PeF/HbsQv/j2URNOiVuxWg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-win32-arm64-msvc": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-win32-arm64-msvc/-/lightningcss-win32-arm64-msvc-1.32.0.tgz",
      "integrity": "sha512-8SbC8BR40pS6baCM8sbtYDSwEVQd4JlFTOlaD3gWGHfThTcABnNDBda6eTZeqbofalIJhFx0qKzgHJmcPTnGdw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-win32-x64-msvc": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-win32-x64-msvc/-/lightningcss-win32-x64-msvc-1.32.0.tgz",
      "integrity": "sha512-Amq9B/SoZYdDi1kFrojnoqPLxYhQ4Wo5XiL8EVJrVsB8ARoC1PWW6VGtT0WKCemjy8aC+louJnjS7U18x3b06Q==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/locate-path": {
      "version": "6.0.0",
      "resolved": "https://registry.npmjs.org/locate-path/-/locate-path-6.0.0.tgz",
      "integrity": "sha512-iPZK6eYjbxRu3uB4/WZ3EsEIMJFMqAoopl3R+zuq0UjcAm/MO6KCweDgPfP3elTztoKP3KtnVHxTn2NHBSDVUw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "p-locate": "^5.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/lodash.merge": {
      "version": "4.6.2",
      "resolved": "https://registry.npmjs.org/lodash.merge/-/lodash.merge-4.6.2.tgz",
      "integrity": "sha512-0KpjqXRVvrYyCsX1swR/XTK0va6VQkQM6MNo7PqW77ByjAhoARA8EfrP1N4+KlKj8YS0ZUCtRT/YUuhyYDujIQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/lru-cache": {
      "version": "5.1.1",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz",
      "integrity": "sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "yallist": "^3.0.2"
      }
    },
    "node_modules/magic-string": {
      "version": "0.30.21",
      "resolved": "https://registry.npmjs.org/magic-string/-/magic-string-0.30.21.tgz",
      "integrity": "sha512-vd2F4YUyEXKGcLHoq+TEyCjxueSeHnFxyyjNp80yg0XV4vUhnDer/lvvlqM/arB5bXQN5K2/3oinyCRyx8T2CQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.5"
      }
    },
    "node_modules/minimatch": {
      "version": "3.1.5",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.1.5.tgz",
      "integrity": "sha512-VgjWUsnnT6n+NUk6eZq77zeFdpW2LWDzP6zFGrCbHXiYNul5Dzqk2HHQ5uFH2DNW5Xbp8+jVzaeNt94ssEEl4w==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "brace-expansion": "^1.1.7"
      },
      "engines": {
        "node": "*"
      }
    },
    "node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/nanoid": {
      "version": "3.3.11",
      "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.11.tgz",
      "integrity": "sha512-N8SpfPUnUp1bK+PMYW8qSWdl9U+wwNWI4QKxOYDy9JAro3WMX7p2OeVRF9v+347pnakNevPmiHhNmZ2HbFA76w==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "bin": {
        "nanoid": "bin/nanoid.cjs"
      },
      "engines": {
        "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
      }
    },
    "node_modules/natural-compare": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/natural-compare/-/natural-compare-1.4.0.tgz",
      "integrity": "sha512-OWND8ei3VtNC9h7V60qff3SVobHr996CTwgxubgyQYEpg290h9J0buyECNNJexkFm5sOajh5G116RYA1c8ZMSw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/node-releases": {
      "version": "2.0.36",
      "resolved": "https://registry.npmjs.org/node-releases/-/node-releases-2.0.36.tgz",
      "integrity": "sha512-TdC8FSgHz8Mwtw9g5L4gR/Sh9XhSP/0DEkQxfEFXOpiul5IiHgHan2VhYYb6agDSfp4KuvltmGApc8HMgUrIkA==",
      "license": "MIT"
    },
    "node_modules/optionator": {
      "version": "0.9.4",
      "resolved": "https://registry.npmjs.org/optionator/-/optionator-0.9.4.tgz",
      "integrity": "sha512-6IpQ7mKUxRcZNLIObR0hz7lxsapSSIYNZJwXPGeF0mTVqGKFIXj1DQcMoT22S3ROcLyY/rz0PWaWZ9ayWmad9g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "deep-is": "^0.1.3",
        "fast-levenshtein": "^2.0.6",
        "levn": "^0.4.1",
        "prelude-ls": "^1.2.1",
        "type-check": "^0.4.0",
        "word-wrap": "^1.2.5"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/p-limit": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/p-limit/-/p-limit-3.1.0.tgz",
      "integrity": "sha512-TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "yocto-queue": "^0.1.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/p-locate": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/p-locate/-/p-locate-5.0.0.tgz",
      "integrity": "sha512-LaNjtRWUBY++zB5nE/NwcaoMylSPk+S+ZHNB1TzdbMJMny6dynpAGt7X/tl/QYq3TIeE6nxHppbo2LGymrG5Pw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "p-limit": "^3.0.2"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/parent-module": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/parent-module/-/parent-module-1.0.1.tgz",
      "integrity": "sha512-GQ2EWRpQV8/o+Aw8YqtfZZPfNRWZYkbidE9k5rpl/hC3vtHHBfGm2Ifi6qWV+coDGkrUKZAxE3Lot5kcsRlh+g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "callsites": "^3.0.0"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/path-exists": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz",
      "integrity": "sha512-ak9Qy5Q7jYb2Wwcey5Fpvg2KoAc/ZIhLSLOSBmRmygPsGwkVVt0fZa0qrtMz+m6tJTAHfZQ8FnmB4MG4LWy7/w==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/path-key": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz",
      "integrity": "sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/picocolors": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
      "integrity": "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==",
      "license": "ISC"
    },
    "node_modules/picomatch": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.3.tgz",
      "integrity": "sha512-5gTmgEY/sqK6gFXLIsQNH19lWb4ebPDLA4SdLP7dsWkIXHWlG66oPuVvXSGFPppYZz8ZDZq0dYYrbHfBCVUb1Q==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/postcss": {
      "version": "8.5.8",
      "resolved": "https://registry.npmjs.org/postcss/-/postcss-8.5.8.tgz",
      "integrity": "sha512-OW/rX8O/jXnm82Ey1k44pObPtdblfiuWnrd8X7GJ7emImCOstunGbXUpp7HdBrFQX6rJzn3sPT397Wp5aCwCHg==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/postcss"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "nanoid": "^3.3.11",
        "picocolors": "^1.1.1",
        "source-map-js": "^1.2.1"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      }
    },
    "node_modules/postcss-value-parser": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz",
      "integrity": "sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ==",
      "license": "MIT"
    },
    "node_modules/prelude-ls": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/prelude-ls/-/prelude-ls-1.2.1.tgz",
      "integrity": "sha512-vkcDPrRZo1QZLbn5RLGPpg/WmIQ65qoWWhcGKf/b5eplkkarX0m9z8ppCat4mlOqUsWpyNuYgO3VRyrYHSzX5g==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/punycode": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz",
      "integrity": "sha512-vYt7UD1U9Wg6138shLtLOvdAu+8DsC/ilFtEVHcH+wydcSpNE20AfSOduf6MkRFahL5FY7X1oU7nKVZFtfq8Fg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/react": {
      "version": "19.2.4",
      "resolved": "https://registry.npmjs.org/react/-/react-19.2.4.tgz",
      "integrity": "sha512-9nfp2hYpCwOjAN+8TZFGhtWEwgvWHXqESH8qT89AT/lWklpLON22Lc8pEtnpsZz7VmawabSU0gCjnj8aC0euHQ==",
      "license": "MIT",
      "peer": true,
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-dom": {
      "version": "19.2.4",
      "resolved": "https://registry.npmjs.org/react-dom/-/react-dom-19.2.4.tgz",
      "integrity": "sha512-AXJdLo8kgMbimY95O2aKQqsz2iWi9jMgKJhRBAxECE4IFxfcazB2LmzloIoibJI3C12IlY20+KFaLv+71bUJeQ==",
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "scheduler": "^0.27.0"
      },
      "peerDependencies": {
        "react": "^19.2.4"
      }
    },
    "node_modules/react-refresh": {
      "version": "0.18.0",
      "resolved": "https://registry.npmjs.org/react-refresh/-/react-refresh-0.18.0.tgz",
      "integrity": "sha512-QgT5//D3jfjJb6Gsjxv0Slpj23ip+HtOpnNgnb2S5zU3CB26G/IDPGoy4RJB42wzFE46DRsstbW6tKHoKbhAxw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-router": {
      "version": "7.13.1",
      "resolved": "https://registry.npmjs.org/react-router/-/react-router-7.13.1.tgz",
      "integrity": "sha512-td+xP4X2/6BJvZoX6xw++A2DdEi++YypA69bJUV5oVvqf6/9/9nNlD70YO1e9d3MyamJEBQFEzk6mbfDYbqrSA==",
      "license": "MIT",
      "dependencies": {
        "cookie": "^1.0.1",
        "set-cookie-parser": "^2.6.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "react": ">=18",
        "react-dom": ">=18"
      },
      "peerDependenciesMeta": {
        "react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/react-router-dom": {
      "version": "7.13.1",
      "resolved": "https://registry.npmjs.org/react-router-dom/-/react-router-dom-7.13.1.tgz",
      "integrity": "sha512-UJnV3Rxc5TgUPJt2KJpo1Jpy0OKQr0AjgbZzBFjaPJcFOb2Y8jA5H3LT8HUJAiRLlWrEXWHbF1Z4SCZaQjWDHw==",
      "license": "MIT",
      "dependencies": {
        "react-router": "7.13.1"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "react": ">=18",
        "react-dom": ">=18"
      }
    },
    "node_modules/resolve-from": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/resolve-from/-/resolve-from-4.0.0.tgz",
      "integrity": "sha512-pb/MYmXstAkysRFx8piNI1tGFNQIFA3vkE3Gq4EuA1dF6gHp/+vgZqsCGJapvy8N3Q+4o7FwvquPJcnZ7RYy4g==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/rolldown": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/rolldown/-/rolldown-1.0.0-rc.8.tgz",
      "integrity": "sha512-RGOL7mz/aoQpy/y+/XS9iePBfeNRDUdozrhCEJxdpJyimW8v6yp4c30q6OviUU5AnUJVLRL9GP//HUs6N3ALrQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@oxc-project/types": "=0.115.0",
        "@rolldown/pluginutils": "1.0.0-rc.8"
      },
      "bin": {
        "rolldown": "bin/cli.mjs"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "optionalDependencies": {
        "@rolldown/binding-android-arm64": "1.0.0-rc.8",
        "@rolldown/binding-darwin-arm64": "1.0.0-rc.8",
        "@rolldown/binding-darwin-x64": "1.0.0-rc.8",
        "@rolldown/binding-freebsd-x64": "1.0.0-rc.8",
        "@rolldown/binding-linux-arm-gnueabihf": "1.0.0-rc.8",
        "@rolldown/binding-linux-arm64-gnu": "1.0.0-rc.8",
        "@rolldown/binding-linux-arm64-musl": "1.0.0-rc.8",
        "@rolldown/binding-linux-ppc64-gnu": "1.0.0-rc.8",
        "@rolldown/binding-linux-s390x-gnu": "1.0.0-rc.8",
        "@rolldown/binding-linux-x64-gnu": "1.0.0-rc.8",
        "@rolldown/binding-linux-x64-musl": "1.0.0-rc.8",
        "@rolldown/binding-openharmony-arm64": "1.0.0-rc.8",
        "@rolldown/binding-wasm32-wasi": "1.0.0-rc.8",
        "@rolldown/binding-win32-arm64-msvc": "1.0.0-rc.8",
        "@rolldown/binding-win32-x64-msvc": "1.0.0-rc.8"
      }
    },
    "node_modules/rolldown/node_modules/@rolldown/pluginutils": {
      "version": "1.0.0-rc.8",
      "resolved": "https://registry.npmjs.org/@rolldown/pluginutils/-/pluginutils-1.0.0-rc.8.tgz",
      "integrity": "sha512-wzJwL82/arVfeSP3BLr1oTy40XddjtEdrdgtJ4lLRBu06mP3q/8HGM6K0JRlQuTA3XB0pNJx2so/nmpY4xyOew==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/scheduler": {
      "version": "0.27.0",
      "resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.27.0.tgz",
      "integrity": "sha512-eNv+WrVbKu1f3vbYJT/xtiF5syA5HPIMtf9IgY/nKg0sWqzAUEvqY/xm7OcZc/qafLx/iO9FgOmeSAp4v5ti/Q==",
      "license": "MIT"
    },
    "node_modules/semver": {
      "version": "6.3.1",
      "resolved": "https://registry.npmjs.org/semver/-/semver-6.3.1.tgz",
      "integrity": "sha512-BR7VvDCVHO+q2xBEWskxS6DJE1qRnb7DxzUrogb71CWoSficBxYsiAGd+Kl0mmq/MprG9yArRkyrQxTO6XjMzA==",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      }
    },
    "node_modules/set-cookie-parser": {
      "version": "2.7.2",
      "resolved": "https://registry.npmjs.org/set-cookie-parser/-/set-cookie-parser-2.7.2.tgz",
      "integrity": "sha512-oeM1lpU/UvhTxw+g3cIfxXHyJRc/uidd3yK1P242gzHds0udQBYzs3y8j4gCCW+ZJ7ad0yctld8RYO+bdurlvw==",
      "license": "MIT"
    },
    "node_modules/shebang-command": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz",
      "integrity": "sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "shebang-regex": "^3.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/shebang-regex": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz",
      "integrity": "sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/source-map-js": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz",
      "integrity": "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==",
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/strip-json-comments": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-3.1.1.tgz",
      "integrity": "sha512-6fPc+R4ihwqP6N/aIv2f1gMH8lOVtWQHoqC4yK6oSDVVocumAsfCqjkXnqiYMhmMwS/mEHLp7Vehlt3ql6lEig==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/supports-color": {
      "version": "7.2.0",
      "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-7.2.0.tgz",
      "integrity": "sha512-qpCAvRl9stuOHveKsn7HncJRvv501qIacKzQlO/+Lwxc9+0q2wLyv4Dfvt80/DPn2pqOBsJdDiogXGR9+OvwRw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "has-flag": "^4.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/tailwindcss": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/tailwindcss/-/tailwindcss-4.2.1.tgz",
      "integrity": "sha512-/tBrSQ36vCleJkAOsy9kbNTgaxvGbyOamC30PRePTQe/o1MFwEKHQk4Cn7BNGaPtjp+PuUrByJehM1hgxfq4sw==",
      "license": "MIT"
    },
    "node_modules/tapable": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/tapable/-/tapable-2.3.0.tgz",
      "integrity": "sha512-g9ljZiwki/LfxmQADO3dEY1CbpmXT5Hm2fJ+QaGKwSXUylMybePR7/67YW7jOrrvjEgL1Fmz5kzyAjWVWLlucg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/webpack"
      }
    },
    "node_modules/tinyglobby": {
      "version": "0.2.15",
      "resolved": "https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.15.tgz",
      "integrity": "sha512-j2Zq4NyQYG5XMST4cbs02Ak8iJUdxRM0XI5QyxXuZOzKOINmWurp3smXu3y5wDcJrptwpSjgXHzIQxR0omXljQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fdir": "^6.5.0",
        "picomatch": "^4.0.3"
      },
      "engines": {
        "node": ">=12.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/SuperchupuDev"
      }
    },
    "node_modules/ts-api-utils": {
      "version": "2.4.0",
      "resolved": "https://registry.npmjs.org/ts-api-utils/-/ts-api-utils-2.4.0.tgz",
      "integrity": "sha512-3TaVTaAv2gTiMB35i3FiGJaRfwb3Pyn/j3m/bfAvGe8FB7CF6u+LMYqYlDh7reQf7UNvoTvdfAqHGmPGOSsPmA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18.12"
      },
      "peerDependencies": {
        "typescript": ">=4.8.4"
      }
    },
    "node_modules/tslib": {
      "version": "2.8.1",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
      "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
      "dev": true,
      "license": "0BSD",
      "optional": true
    },
    "node_modules/type-check": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/type-check/-/type-check-0.4.0.tgz",
      "integrity": "sha512-XleUoc9uwGXqjWwXaUTZAmzMcFZ5858QA2vvx1Ur5xIcixXIP+8LnFDgRplU30us6teqdlskFfu+ae4K79Ooew==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "prelude-ls": "^1.2.1"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/typescript": {
      "version": "5.9.3",
      "resolved": "https://registry.npmjs.org/typescript/-/typescript-5.9.3.tgz",
      "integrity": "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw==",
      "dev": true,
      "license": "Apache-2.0",
      "peer": true,
      "bin": {
        "tsc": "bin/tsc",
        "tsserver": "bin/tsserver"
      },
      "engines": {
        "node": ">=14.17"
      }
    },
    "node_modules/typescript-eslint": {
      "version": "8.56.1",
      "resolved": "https://registry.npmjs.org/typescript-eslint/-/typescript-eslint-8.56.1.tgz",
      "integrity": "sha512-U4lM6pjmBX7J5wk4szltF7I1cGBHXZopnAXCMXb3+fZ3B/0Z3hq3wS/CCUB2NZBNAExK92mCU2tEohWuwVMsDQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@typescript-eslint/eslint-plugin": "8.56.1",
        "@typescript-eslint/parser": "8.56.1",
        "@typescript-eslint/typescript-estree": "8.56.1",
        "@typescript-eslint/utils": "8.56.1"
      },
      "engines": {
        "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/typescript-eslint"
      },
      "peerDependencies": {
        "eslint": "^8.57.0 || ^9.0.0 || ^10.0.0",
        "typescript": ">=4.8.4 <6.0.0"
      }
    },
    "node_modules/undici-types": {
      "version": "7.16.0",
      "resolved": "https://registry.npmjs.org/undici-types/-/undici-types-7.16.0.tgz",
      "integrity": "sha512-Zz+aZWSj8LE6zoxD+xrjh4VfkIG8Ya6LvYkZqtUQGJPZjYl53ypCaUwWqo7eI0x66KBGeRo+mlBEkMSeSZ38Nw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/update-browserslist-db": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.2.3.tgz",
      "integrity": "sha512-Js0m9cx+qOgDxo0eMiFGEueWztz+d4+M3rGlmKPT+T4IS/jP4ylw3Nwpu6cpTTP8R1MAC1kF4VbdLt3ARf209w==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "escalade": "^3.2.0",
        "picocolors": "^1.1.1"
      },
      "bin": {
        "update-browserslist-db": "cli.js"
      },
      "peerDependencies": {
        "browserslist": ">= 4.21.0"
      }
    },
    "node_modules/uri-js": {
      "version": "4.4.1",
      "resolved": "https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz",
      "integrity": "sha512-7rKUyy33Q1yc98pQ1DAmLtwX109F7TIfWlW1Ydo8Wl1ii1SeHieeh0HHfPeL2fMXK6z0s8ecKs9frCuLJvndBg==",
      "dev": true,
      "license": "BSD-2-Clause",
      "dependencies": {
        "punycode": "^2.1.0"
      }
    },
    "node_modules/vite": {
      "version": "8.0.0-beta.18",
      "resolved": "https://registry.npmjs.org/vite/-/vite-8.0.0-beta.18.tgz",
      "integrity": "sha512-azgNbWdsO/WBqHQxwSCy+zd+Fq+37Fix2hn64cQuiUvaaGGSUac7f8RGQhI1aQl9OKbfWblrCFLWs+tln06c2A==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "@oxc-project/runtime": "0.115.0",
        "lightningcss": "^1.31.1",
        "picomatch": "^4.0.3",
        "postcss": "^8.5.6",
        "rolldown": "1.0.0-rc.8",
        "tinyglobby": "^0.2.15"
      },
      "bin": {
        "vite": "bin/vite.js"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "funding": {
        "url": "https://github.com/vitejs/vite?sponsor=1"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.3"
      },
      "peerDependencies": {
        "@types/node": "^20.19.0 || >=22.12.0",
        "@vitejs/devtools": "^0.0.0-alpha.31",
        "esbuild": "^0.27.0",
        "jiti": ">=1.21.0",
        "less": "^4.0.0",
        "sass": "^1.70.0",
        "sass-embedded": "^1.70.0",
        "stylus": ">=0.54.8",
        "sugarss": "^5.0.0",
        "terser": "^5.16.0",
        "tsx": "^4.8.1",
        "yaml": "^2.4.2"
      },
      "peerDependenciesMeta": {
        "@types/node": {
          "optional": true
        },
        "@vitejs/devtools": {
          "optional": true
        },
        "esbuild": {
          "optional": true
        },
        "jiti": {
          "optional": true
        },
        "less": {
          "optional": true
        },
        "sass": {
          "optional": true
        },
        "sass-embedded": {
          "optional": true
        },
        "stylus": {
          "optional": true
        },
        "sugarss": {
          "optional": true
        },
        "terser": {
          "optional": true
        },
        "tsx": {
          "optional": true
        },
        "yaml": {
          "optional": true
        }
      }
    },
    "node_modules/which": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/which/-/which-2.0.2.tgz",
      "integrity": "sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "isexe": "^2.0.0"
      },
      "bin": {
        "node-which": "bin/node-which"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/word-wrap": {
      "version": "1.2.5",
      "resolved": "https://registry.npmjs.org/word-wrap/-/word-wrap-1.2.5.tgz",
      "integrity": "sha512-BN22B5eaMMI9UMtjrGd5g5eCYPpCPDUy0FJXbYsaT5zYxjFOckS53SQDE3pWkVoWpHXVb3BrYcEN4Twa55B5cA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/yallist": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz",
      "integrity": "sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/yocto-queue": {
      "version": "0.1.0",
      "resolved": "https://registry.npmjs.org/yocto-queue/-/yocto-queue-0.1.0.tgz",
      "integrity": "sha512-rVksvsnNCdJ/ohGc6xgPwyN8eheCxsiLM8mxuE/t/mOVqJewPuO1miLpTHQiRgTKCLexL4MeAFVagts7HmNZ2Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/zod": {
      "version": "4.3.6",
      "resolved": "https://registry.npmjs.org/zod/-/zod-4.3.6.tgz",
      "integrity": "sha512-rftlrkhHZOcjDwkGlnUtZZkvaPHCsDATp4pGpuOOMDaTdDDXF91wuVDJoWoPsKX/3YPQ5fHuF3STjcYyKr+Qhg==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "funding": {
        "url": "https://github.com/sponsors/colinhacks"
      }
    },
    "node_modules/zod-validation-error": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/zod-validation-error/-/zod-validation-error-4.0.2.tgz",
      "integrity": "sha512-Q6/nZLe6jxuU80qb/4uJ4t5v2VEZ44lzQjPDhYJNztRQ4wyWc6VF3D3Kb/fAuPetZQnhS3hnajCf9CsWesghLQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18.0.0"
      },
      "peerDependencies": {
        "zod": "^3.25.0 || ^4.0.0"
      }
    }
  }
}

```

## postcss.config.js

```javascript
export default {
  plugins: {
    '@tailwindcss/postcss': {},
    autoprefixer: {},
  },
};

```

## tailwind.config.js

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [],
};

```

## eslint.config.js

```javascript
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'
import { defineConfig, globalIgnores } from 'eslint/config'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      js.configs.recommended,
      tseslint.configs.recommended,
      reactHooks.configs.flat.recommended,
      reactRefresh.configs.vite,
    ],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
  },
])

```

## tsconfig.json

```json
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}

```

## tsconfig.app.json

```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2022",
    "useDefineForClassFields": true,
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "types": ["vite/client"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["src"]
}

```

## tsconfig.node.json

```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "ES2023",
    "lib": ["ES2023"],
    "module": "ESNext",
    "types": ["node"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["vite.config.ts"]
}

```

## vite.config.ts

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})

```

## backend/main.py

```python
import json
from typing import Optional

from fastapi import Body, Depends, FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sse_starlette.sse import EventSourceResponse

from models import BeatScene, Chapter, ChatMessage, Document, Project, User
from services.auth_service import (
    create_access_token,
    get_current_user,
    get_password_hash,
    verify_password,
)
from services.database_service import get_session, init_db
from services.file_service import (
    create_file_record,
    delete_file_record,
    list_project_files,
    read_file_content,
    save_uploaded_file,
)
from services.openrouter_service import MODEL_OPTIONS, openrouter_service
from services.story_service import StoryService
from services.vector_service import add_memory, search_memory

app = FastAPI(title="Membrane + Story Engine")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProjectCreateRequest(BaseModel):
    name: str = "Untitled Project"
    description: str = ""


class ProjectUpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class DocumentUpdateRequest(BaseModel):
    content: str


class StoryCreateRequest(BaseModel):
    title: str
    genre: str = ""
    premise: str = ""


class StoryUpdateRequest(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    premise: Optional[str] = None


class ChapterCreateRequest(BaseModel):
    title: str = "Untitled Chapter"


class ChapterUpdateRequest(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    summary: Optional[str] = None


class CharacterCreateRequest(BaseModel):
    name: str
    role: str = ""
    traits: str = ""
    backstory: str = ""
    description: str = ""


class CharacterUpdateRequest(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    traits: Optional[str] = None
    backstory: Optional[str] = None
    description: Optional[str] = None


class BeatCreateRequest(BaseModel):
    story_id: int
    title: str = ""
    content: str = ""
    beat_type: str = "scene"


class BeatUpdateRequest(BaseModel):
    story_id: int
    title: Optional[str] = None
    content: Optional[str] = None
    beat_type: Optional[str] = None


class WorldbuildingCreateRequest(BaseModel):
    story_id: int
    name: str
    element_type: str = "location"
    description: str = ""


class KeyEventCreateRequest(BaseModel):
    story_id: int
    title: str
    description: str = ""


class MemoryAddRequest(BaseModel):
    content: str


class MemorySearchRequest(BaseModel):
    query: str
    top_k: int = 10


class GenerateRequest(BaseModel):
    prompt: str
    story_id: int
    chapter_id: Optional[int] = None
    context_type: str = "prose"
    model: str = "default"


@app.on_event("startup")
async def startup():
    init_db()


def require_project(project_id: int, user_id: int, db: Session) -> Project:
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == user_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@app.post("/api/auth/signup")
async def signup(
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_session),
):
    existing = db.query(User).filter((User.email == email) | (User.username == username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(email=email, username=username, password_hash=get_password_hash(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "token": create_access_token({"sub": str(user.id)}),
        "user": {"id": user.id, "email": user.email, "username": user.username},
    }


@app.post("/api/auth/login")
async def login(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_session),
):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "token": create_access_token({"sub": str(user.id)}),
        "user": {"id": user.id, "email": user.email, "username": user.username},
    }


@app.get("/api/auth/me")
async def get_me(user=Depends(get_current_user)):
    return {"id": user.id, "email": user.email, "username": user.username}


@app.get("/api/projects")
async def list_projects(user=Depends(get_current_user), db: Session = Depends(get_session)):
    return db.query(Project).filter(Project.user_id == user.id).all()


@app.post("/api/projects")
async def create_project(
    payload: ProjectCreateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    project = Project(user_id=user.id, name=payload.name, description=payload.description)
    db.add(project)
    db.commit()
    db.refresh(project)

    doc = Document(project_id=project.id)
    db.add(doc)
    db.commit()
    return project


@app.get("/api/projects/{project_id}")
async def get_project(project_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    return require_project(project_id, user.id, db)


@app.put("/api/projects/{project_id}")
async def update_project(
    project_id: int,
    payload: ProjectUpdateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    project = require_project(project_id, user.id, db)
    if payload.name is not None:
        project.name = payload.name
    if payload.description is not None:
        project.description = payload.description
    db.commit()
    db.refresh(project)
    return project


@app.delete("/api/projects/{project_id}")
async def delete_project(project_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    project = require_project(project_id, user.id, db)
    db.delete(project)
    db.commit()
    return {"status": "deleted"}


@app.get("/api/projects/{project_id}/document")
async def get_document(project_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    doc = db.query(Document).filter(Document.project_id == project_id).first()
    if not doc:
        doc = Document(project_id=project_id)
        db.add(doc)
        db.commit()
        db.refresh(doc)
    return doc


@app.put("/api/projects/{project_id}/document")
async def update_document(
    project_id: int,
    payload: DocumentUpdateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    require_project(project_id, user.id, db)
    doc = db.query(Document).filter(Document.project_id == project_id).first()
    if not doc:
        doc = Document(project_id=project_id)
        db.add(doc)
    doc.content = payload.content
    db.commit()
    db.refresh(doc)
    return doc


@app.get("/api/projects/{project_id}/chat/stream")
async def chat_stream(
    project_id: int,
    message: str,
    selected_text: str = "",
    model: str = "default",
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    require_project(project_id, user.id, db)

    doc = db.query(Document).filter(Document.project_id == project_id).first()
    doc_content = doc.content if doc else ""

    system_msg = "You are a helpful writing assistant. You help with creative writing, editing, and brainstorming."
    if selected_text:
        system_msg += f"\n\nThe user has selected this text: '{selected_text}'"

    chat_hist = [{"role": "system", "content": system_msg}]
    chat_hist.append(
        {
            "role": "user",
            "content": f"Document context:\n{doc_content}\n\nUser message: {message}",
        }
    )

    user_msg = ChatMessage(project_id=project_id, role="user", content=message)
    db.add(user_msg)
    db.commit()

    async def event_generator():
        full_response = ""
        async for chunk in openrouter_service.stream_chat(chat_hist, model=model):
            full_response += chunk
            yield {"data": json.dumps({"content": chunk})}

        ai_msg = ChatMessage(project_id=project_id, role="assistant", content=full_response)
        db.add(ai_msg)
        db.commit()
        yield {"data": "[DONE]"}

    return EventSourceResponse(event_generator())


@app.post("/api/projects/{project_id}/upload/file")
async def upload_file(
    project_id: int,
    train: bool = Form(False),
    file: UploadFile = File(...),
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    require_project(project_id, user.id, db)

    content = await file.read()
    filepath = await save_uploaded_file(project_id, file.filename, content)
    file_record = create_file_record(db, project_id, file.filename, filepath, train)

    if train:
        text = await read_file_content(filepath, file.filename)
        if text:
            await add_memory(db, project_id, text, {"filename": file.filename, "type": "upload"})

    return file_record


@app.get("/api/projects/{project_id}/upload/list")
async def list_files(project_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    return list_project_files(db, project_id)


@app.delete("/api/projects/{project_id}/upload/file/{file_id}")
async def delete_file(project_id: int, file_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    if not delete_file_record(db, file_id, project_id):
        raise HTTPException(status_code=404, detail="File not found")
    return {"status": "deleted"}


@app.post("/api/projects/{project_id}/memory/add")
async def add_to_memory(
    project_id: int,
    payload: MemoryAddRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    require_project(project_id, user.id, db)
    memory = await add_memory(db, project_id, payload.content)
    return {"id": memory.id}


@app.post("/api/projects/{project_id}/memory/search")
async def search_project_memory(
    project_id: int,
    payload: MemorySearchRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    require_project(project_id, user.id, db)
    results = await search_memory(db, project_id, payload.query, payload.top_k)
    return [{"id": item.id, "content": item.content, "metadata": item.meta} for item in results]


@app.get("/api/stories")
async def list_stories(user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    return service.list_stories(user.id)


@app.post("/api/stories")
async def create_story(
    payload: StoryCreateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    return service.create_story(user.id, payload.title, payload.genre, payload.premise)


@app.get("/api/stories/{story_id}")
async def get_story(story_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story = service.get_story(story_id, user.id)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return story


@app.put("/api/stories/{story_id}")
async def update_story(
    story_id: int,
    payload: StoryUpdateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    kwargs = {k: v for k, v in payload.model_dump().items() if v is not None}
    story = service.update_story(story_id, user.id, **kwargs)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return story


@app.delete("/api/stories/{story_id}")
async def delete_story(story_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    if not service.delete_story(story_id, user.id):
        raise HTTPException(status_code=404, detail="Story not found")
    return {"status": "deleted"}


@app.post("/api/stories/{story_id}/chapters")
async def create_chapter(
    story_id: int,
    payload: ChapterCreateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    chapter = service.create_chapter(story_id, user.id, payload.title)
    if not chapter:
        raise HTTPException(status_code=404, detail="Story not found")
    return chapter


@app.put("/api/chapters/{chapter_id}")
async def update_chapter(
    chapter_id: int,
    payload: ChapterUpdateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    story_ids = [story.id for story in service.list_stories(user.id)]

    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")

    if chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")

    if payload.title is not None:
        chapter.title = payload.title
    if payload.content is not None:
        chapter.content = payload.content
    if payload.summary is not None:
        chapter.summary = payload.summary

    db.commit()
    db.refresh(chapter)
    return chapter


@app.post("/api/chapters/{chapter_id}/summarize")
async def summarize_chapter(chapter_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [story.id for story in service.list_stories(user.id)]

    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")

    summary = await service.summarize_chapter(chapter_id, chapter.story_id, user.id)
    return {"summary": summary}


@app.get("/api/stories/{story_id}/characters")
async def list_characters(story_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    return service.list_characters(story_id, user.id)


@app.post("/api/stories/{story_id}/characters")
async def create_character(
    story_id: int,
    payload: CharacterCreateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    character = service.create_character(
        story_id,
        user.id,
        payload.name,
        role=payload.role,
        traits=payload.traits,
        backstory=payload.backstory,
        description=payload.description,
    )
    if not character:
        raise HTTPException(status_code=404, detail="Story not found")
    return character


@app.put("/api/stories/{story_id}/characters/{character_id}")
async def update_character(
    story_id: int,
    character_id: int,
    payload: CharacterUpdateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    kwargs = {k: v for k, v in payload.model_dump().items() if v is not None}
    character = service.update_character(story_id, user.id, character_id, **kwargs)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@app.delete("/api/stories/{story_id}/characters/{character_id}")
async def delete_character(
    story_id: int,
    character_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    if not service.delete_character(story_id, user.id, character_id):
        raise HTTPException(status_code=404, detail="Character not found")
    return {"status": "deleted"}


@app.get("/api/chapters/{chapter_id}/beats")
async def list_beats(chapter_id: int, story_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    return service.list_beats(chapter_id, story_id, user.id)


@app.post("/api/chapters/{chapter_id}/beats")
async def create_beat(
    chapter_id: int,
    payload: BeatCreateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    return service.create_beat(
        chapter_id,
        payload.story_id,
        user.id,
        payload.title,
        content=payload.content,
        beat_type=payload.beat_type,
    )


@app.put("/api/chapters/{chapter_id}/beats/{beat_id}")
async def update_beat(
    chapter_id: int,
    beat_id: int,
    payload: BeatUpdateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    kwargs = {k: v for k, v in payload.model_dump().items() if k != "story_id" and v is not None}
    beat = service.update_beat(chapter_id, payload.story_id, user.id, beat_id, **kwargs)
    if not beat:
        raise HTTPException(status_code=404, detail="Beat not found")
    return beat


@app.delete("/api/chapters/{chapter_id}/beats/{beat_id}")
async def delete_beat(
    chapter_id: int,
    beat_id: int,
    story_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    if not service.delete_beat(chapter_id, story_id, user.id, beat_id):
        raise HTTPException(status_code=404, detail="Beat not found")
    return {"status": "deleted"}


@app.get("/api/chapters/{chapter_id}/worldbuilding")
async def list_worldbuilding(
    chapter_id: int,
    story_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    return service.list_worldbuilding(chapter_id, story_id, user.id)


@app.post("/api/chapters/{chapter_id}/worldbuilding")
async def create_worldbuilding(
    chapter_id: int,
    payload: WorldbuildingCreateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    return service.create_worldbuilding(
        chapter_id,
        payload.story_id,
        user.id,
        payload.name,
        payload.element_type,
        description=payload.description,
    )


@app.get("/api/chapters/{chapter_id}/keyevents")
async def list_keyevents(
    chapter_id: int,
    story_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    return service.list_keyevents(chapter_id, story_id, user.id)


@app.post("/api/chapters/{chapter_id}/keyevents")
async def create_keyevent(
    chapter_id: int,
    payload: KeyEventCreateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    return service.create_keyevent(
        chapter_id,
        payload.story_id,
        user.id,
        payload.title,
        description=payload.description,
    )


@app.post("/api/ai/generate")
async def generate_content(
    payload: GenerateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_session),
):
    service = StoryService(db)
    story = service.get_story(payload.story_id, user.id)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")

    if payload.context_type == "query" and payload.chapter_id:
        result = await service.query_context(
            payload.story_id,
            user.id,
            payload.prompt,
            payload.chapter_id,
            payload.model,
        )
        return {"content": result}

    chapter = None
    if payload.chapter_id:
        chapter = (
            db.query(Chapter)
            .filter(Chapter.id == payload.chapter_id, Chapter.story_id == payload.story_id)
            .first()
        )
    elif story.chapters:
        chapter = sorted(story.chapters, key=lambda item: item.order)[0]

    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")

    characters = story.characters
    beats = chapter.beats
    key_events = chapter.key_events
    worldbuilding = chapter.worldbuilding

    if payload.context_type == "prose":
        result = await service.generate_prose(
            chapter,
            story,
            characters,
            beats,
            key_events,
            worldbuilding,
            payload.prompt,
            payload.model,
        )
    elif payload.context_type == "expand_beat":
        beat_id = int(payload.prompt) if payload.prompt.isdigit() else None
        if not beat_id:
            result = "Invalid beat ID"
        else:
            beat = db.query(BeatScene).filter(BeatScene.id == beat_id).first()
            if not beat:
                result = "Beat not found"
            else:
                result = await service.expand_beat(beat, chapter, story, characters, payload.model)
    else:
        result = await service.generate_prose(
            chapter,
            story,
            characters,
            beats,
            key_events,
            worldbuilding,
            payload.prompt,
            payload.model,
        )

    return {"content": result}


@app.get("/api/models")
async def get_models():
    return MODEL_OPTIONS


@app.get("/health")
async def health_check():
    return {"status": "ok"}

```

## backend/models.py

```python
from datetime import datetime

from sqlalchemy import JSON, Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from services.database_service import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    projects = relationship("Project", back_populates="user", cascade="all, delete-orphan")
    stories = relationship("Story", back_populates="user", cascade="all, delete-orphan")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, default="Untitled Project")
    description = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="projects")
    documents = relationship("Document", back_populates="project", cascade="all, delete-orphan")
    chat_messages = relationship("ChatMessage", back_populates="project", cascade="all, delete-orphan")
    file_uploads = relationship("FileUpload", back_populates="project", cascade="all, delete-orphan")


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    project = relationship("Project", back_populates="documents")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="chat_messages")


class FileUpload(Base):
    __tablename__ = "file_uploads"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    file_type = Column(String, default="unknown")
    train = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="file_uploads")


class VectorEmbedding(Base):
    __tablename__ = "vector_embeddings"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    content_hash = Column(String, index=True)
    embedding = Column(JSON)
    meta = Column("metadata", JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, default="Untitled Story")
    genre = Column(String, default="")
    premise = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="stories")
    chapters = relationship("Chapter", back_populates="story", cascade="all, delete-orphan")
    characters = relationship("Character", back_populates="story", cascade="all, delete-orphan")
    plot_brainstorms = relationship("PlotBrainstorm", back_populates="story", cascade="all, delete-orphan")


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, default="Untitled Chapter")
    content = Column(Text, default="")
    summary = Column(Text, default="")
    order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    story = relationship("Story", back_populates="chapters")
    beats = relationship("BeatScene", back_populates="chapter", cascade="all, delete-orphan")
    worldbuilding = relationship("WorldBuildingElement", back_populates="chapter", cascade="all, delete-orphan")
    key_events = relationship("KeyEvent", back_populates="chapter", cascade="all, delete-orphan")


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    role = Column(String, default="")
    traits = Column(Text, default="")
    backstory = Column(Text, default="")
    description = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    story = relationship("Story", back_populates="characters")


class PlotBrainstorm(Base):
    __tablename__ = "plot_brainstorms"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    story = relationship("Story", back_populates="plot_brainstorms")


class BeatScene(Base):
    __tablename__ = "beat_scenes"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, default="")
    content = Column(Text, default="")
    beat_type = Column(String, default="scene")
    order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    chapter = relationship("Chapter", back_populates="beats")


class WorldBuildingElement(Base):
    __tablename__ = "world_building_elements"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id", ondelete="CASCADE"), nullable=False)
    element_type = Column(String, default="location")
    name = Column(String, nullable=False)
    description = Column(Text, default="")
    details = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)

    chapter = relationship("Chapter", back_populates="worldbuilding")


class KeyEvent(Base):
    __tablename__ = "key_events"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, default="")
    order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    chapter = relationship("Chapter", back_populates="key_events")

```

## backend/requirements.txt

```text
fastapi
uvicorn
sqlalchemy
python-jose
passlib[bcrypt]
python-multipart
aiofiles
httpx
sse-starlette
psycopg2-binary

```

## backend/services/auth_service.py

```python
import os
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models import User
from services.database_service import get_session

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7
security = HTTPBearer(auto_error=False)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: Session = Depends(get_session),
):
    if not credentials:
        dev_user = db.query(User).filter(User.email == "dev@example.com").first()
        if dev_user:
            return dev_user

        dev_user = User(email="dev@example.com", username="dev", password_hash=get_password_hash("dev"))
        db.add(dev_user)
        db.commit()
        db.refresh(dev_user)
        return dev_user

    payload = decode_token(credentials.credentials)
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    try:
        user_id = int(user_id)
    except (TypeError, ValueError) as exc:
        raise HTTPException(status_code=401, detail="Invalid token subject") from exc

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user

```

## backend/services/database_service.py

```python
import os
from pathlib import Path
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

Base = declarative_base()
_engine = None
_SessionLocal = None


def get_database_url() -> str:
    database_url = os.environ.get("DATABASE_URL")
    if database_url and database_url.startswith("postgres://"):
        return database_url.replace("postgres://", "postgresql://", 1)
    if database_url:
        return database_url

    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return f"sqlite:///{data_dir / 'membrane.db'}"


def init_db():
    global _engine, _SessionLocal

    if _engine is not None:
        return _engine

    url = get_database_url()
    if url.startswith("sqlite"):
        _engine = create_engine(url, connect_args={"check_same_thread": False})
    else:
        _engine = create_engine(url)

    _SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
        bind=_engine,
    )

    # Ensure model metadata is imported before table creation.
    import models  # noqa: F401

    Base.metadata.create_all(bind=_engine)
    return _engine


def get_engine():
    if _engine is None:
        init_db()
    return _engine


def get_session() -> Generator[Session, None, None]:
    global _SessionLocal

    if _SessionLocal is None:
        init_db()

    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

## backend/services/file_service.py

```python
import os
from pathlib import Path
from typing import Optional

import aiofiles
from sqlalchemy.orm import Session

from models import FileUpload

UPLOAD_DIR = Path(os.environ.get("UPLOAD_DIR", Path(__file__).parent.parent / "data" / "uploads"))


def get_project_upload_dir(project_id: int) -> Path:
    project_dir = UPLOAD_DIR / str(project_id)
    project_dir.mkdir(parents=True, exist_ok=True)
    return project_dir


async def save_uploaded_file(project_id: int, filename: str, content: bytes) -> str:
    filepath = get_project_upload_dir(project_id) / filename
    async with aiofiles.open(filepath, "wb") as f:
        await f.write(content)
    return str(filepath)


async def read_file_content(filepath: str, filename: str) -> Optional[str]:
    try:
        async with aiofiles.open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return await f.read()
    except Exception:
        return None


def create_file_record(
    db: Session,
    project_id: int,
    filename: str,
    filepath: str,
    train: bool = False,
) -> FileUpload:
    file_type = filename.lower().split(".")[-1] if "." in filename else "unknown"
    record = FileUpload(
        project_id=project_id,
        filename=filename,
        filepath=filepath,
        file_type=file_type,
        train=train,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def list_project_files(db: Session, project_id: int):
    return db.query(FileUpload).filter(FileUpload.project_id == project_id).all()


def delete_file_record(db: Session, file_id: int, project_id: int) -> bool:
    file_record = (
        db.query(FileUpload)
        .filter(FileUpload.id == file_id, FileUpload.project_id == project_id)
        .first()
    )
    if not file_record:
        return False

    try:
        Path(file_record.filepath).unlink(missing_ok=True)
    except Exception:
        pass

    db.delete(file_record)
    db.commit()
    return True

```

## backend/services/openrouter_service.py

```python
import hashlib
import json
import os
from typing import AsyncGenerator, Optional

import httpx

MODELS = {
    "default": "anthropic/claude-3.5-sonnet",
    "mini-max": "minimax/minimax-m2.5",
    "gemini-flash": "google/gemini-2.0-flash-exp",
    "deepseek": "deepseek/deepseek-v4-flash",
    "moonshot": "moonshotai/kimi-k2.5",
    "grok": "xai/grok-4-fast",
}

MODEL_OPTIONS = [
    {"id": "anthropic/claude-3.5-sonnet", "name": "Claude 3.5 Sonnet"},
    {"id": "minimax/minimax-m2.5", "name": "MiniMax M2.5"},
    {"id": "google/gemini-2.0-flash-exp", "name": "Gemini 3 Flash Preview"},
    {"id": "deepseek/deepseek-v4-flash", "name": "DeepSeek V4 Flash"},
    {"id": "moonshotai/kimi-k2.5", "name": "Kimi K2.5"},
    {"id": "xai/grok-4-fast", "name": "Grok 4.1 Fast"},
]

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")


class OpenRouterService:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or OPENROUTER_API_KEY
        self.base_url = "https://openrouter.ai/api/v1"

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://membrane.app",
            "X-Title": "Membrane",
        }

    def _resolve_model(self, model: str) -> str:
        return MODELS.get(model, model) if model != "default" else MODELS["default"]

    async def stream_chat(
        self,
        messages: list,
        model: str = "default",
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> AsyncGenerator[str, None]:
        if not self.api_key:
            yield "OpenRouter API key not configured. Add OPENROUTER_API_KEY to enable AI responses."
            return

        payload = {
            "model": self._resolve_model(model),
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True,
        }

        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream(
                "POST",
                f"{self.base_url}/chat/completions",
                headers=self._get_headers(),
                json=payload,
            ) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if not line.startswith("data: "):
                        continue
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        content = chunk.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        if content:
                            yield content
                    except json.JSONDecodeError:
                        continue

    async def chat(
        self,
        messages: list,
        model: str = "default",
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> str:
        if not self.api_key:
            return "OpenRouter API key not configured. Add OPENROUTER_API_KEY to enable AI responses."

        payload = {
            "model": self._resolve_model(model),
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers=self._get_headers(),
                json=payload,
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

    async def get_embedding(self, text: str) -> list[float]:
        # Offline-safe fallback so memory features still function without API keys.
        if not self.api_key:
            digest = hashlib.sha256(text.encode("utf-8", errors="ignore")).digest()
            return [b / 255.0 for b in digest]

        payload = {"model": "text-embedding-3-small", "input": text}
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self.base_url}/embeddings",
                headers=self._get_headers(),
                json=payload,
            )
            response.raise_for_status()
            return response.json()["data"][0]["embedding"]

    async def summarize_text(self, text: str, model: str = "default") -> str:
        return await self.chat(
            [
                {"role": "system", "content": "Summarize concisely."},
                {"role": "user", "content": text},
            ],
            model=model,
            temperature=0.3,
            max_tokens=512,
        )


openrouter_service = OpenRouterService()

```

## backend/services/story_service.py

```python
from typing import Optional

from sqlalchemy.orm import Session

from models import BeatScene, Chapter, Character, KeyEvent, Story, WorldBuildingElement
from services.openrouter_service import openrouter_service


class StoryService:
    def __init__(self, db: Session):
        self.db = db

    def list_stories(self, user_id: int):
        return self.db.query(Story).filter(Story.user_id == user_id).all()

    def get_story(self, story_id: int, user_id: int) -> Optional[Story]:
        return self.db.query(Story).filter(Story.id == story_id, Story.user_id == user_id).first()

    def create_story(self, user_id: int, title: str, genre: str = "", premise: str = "") -> Story:
        story = Story(user_id=user_id, title=title, genre=genre, premise=premise)
        self.db.add(story)
        self.db.commit()
        self.db.refresh(story)

        chapter = Chapter(story_id=story.id, title="Chapter 1", order=1)
        self.db.add(chapter)
        self.db.commit()
        return story

    def update_story(self, story_id: int, user_id: int, **kwargs):
        story = self.get_story(story_id, user_id)
        if story:
            for key, value in kwargs.items():
                if hasattr(story, key):
                    setattr(story, key, value)
            self.db.commit()
            self.db.refresh(story)
        return story

    def delete_story(self, story_id: int, user_id: int) -> bool:
        story = self.get_story(story_id, user_id)
        if not story:
            return False

        self.db.delete(story)
        self.db.commit()
        return True

    def create_chapter(self, story_id: int, user_id: int, title: str = "Untitled Chapter"):
        story = self.get_story(story_id, user_id)
        if not story:
            return None

        max_order = self.db.query(Chapter).filter(Chapter.story_id == story_id).count()
        chapter = Chapter(story_id=story_id, title=title, order=max_order + 1)
        self.db.add(chapter)
        self.db.commit()
        self.db.refresh(chapter)
        return chapter

    def get_chapter(self, chapter_id: int, story_id: int, user_id: int) -> Optional[Chapter]:
        story = self.get_story(story_id, user_id)
        if not story:
            return None
        return self.db.query(Chapter).filter(Chapter.id == chapter_id, Chapter.story_id == story_id).first()

    def update_chapter(self, chapter_id: int, story_id: int, user_id: int, **kwargs):
        chapter = self.get_chapter(chapter_id, story_id, user_id)
        if chapter:
            for key, value in kwargs.items():
                if hasattr(chapter, key):
                    setattr(chapter, key, value)
            self.db.commit()
            self.db.refresh(chapter)
        return chapter

    def list_characters(self, story_id: int, user_id: int):
        story = self.get_story(story_id, user_id)
        return story.characters if story else []

    def create_character(self, story_id: int, user_id: int, name: str, **kwargs):
        story = self.get_story(story_id, user_id)
        if not story:
            return None

        character = Character(story_id=story_id, name=name, **kwargs)
        self.db.add(character)
        self.db.commit()
        self.db.refresh(character)
        return character

    def update_character(self, story_id: int, user_id: int, character_id: int, **kwargs):
        story = self.get_story(story_id, user_id)
        if not story:
            return None

        character = (
            self.db.query(Character)
            .filter(Character.id == character_id, Character.story_id == story_id)
            .first()
        )
        if character:
            for key, value in kwargs.items():
                if hasattr(character, key):
                    setattr(character, key, value)
            self.db.commit()
            self.db.refresh(character)
        return character

    def delete_character(self, story_id: int, user_id: int, character_id: int) -> bool:
        story = self.get_story(story_id, user_id)
        if not story:
            return False

        character = (
            self.db.query(Character)
            .filter(Character.id == character_id, Character.story_id == story_id)
            .first()
        )
        if not character:
            return False

        self.db.delete(character)
        self.db.commit()
        return True

    def create_beat(self, chapter_id: int, story_id: int, user_id: int, title: str = "", **kwargs):
        chapter = self.get_chapter(chapter_id, story_id, user_id)
        if not chapter:
            return None

        max_order = self.db.query(BeatScene).filter(BeatScene.chapter_id == chapter_id).count()
        beat = BeatScene(chapter_id=chapter_id, title=title, order=max_order + 1, **kwargs)
        self.db.add(beat)
        self.db.commit()
        self.db.refresh(beat)
        return beat

    def list_beats(self, chapter_id: int, story_id: int, user_id: int):
        chapter = self.get_chapter(chapter_id, story_id, user_id)
        return chapter.beats if chapter else []

    def update_beat(self, chapter_id: int, story_id: int, user_id: int, beat_id: int, **kwargs):
        chapter = self.get_chapter(chapter_id, story_id, user_id)
        if not chapter:
            return None

        beat = (
            self.db.query(BeatScene)
            .filter(BeatScene.id == beat_id, BeatScene.chapter_id == chapter_id)
            .first()
        )
        if beat:
            for key, value in kwargs.items():
                if hasattr(beat, key):
                    setattr(beat, key, value)
            self.db.commit()
            self.db.refresh(beat)
        return beat

    def delete_beat(self, chapter_id: int, story_id: int, user_id: int, beat_id: int) -> bool:
        chapter = self.get_chapter(chapter_id, story_id, user_id)
        if not chapter:
            return False

        beat = (
            self.db.query(BeatScene)
            .filter(BeatScene.id == beat_id, BeatScene.chapter_id == chapter_id)
            .first()
        )
        if not beat:
            return False

        self.db.delete(beat)
        self.db.commit()
        return True

    def create_worldbuilding(
        self,
        chapter_id: int,
        story_id: int,
        user_id: int,
        name: str,
        element_type: str = "location",
        **kwargs,
    ):
        chapter = self.get_chapter(chapter_id, story_id, user_id)
        if not chapter:
            return None

        element = WorldBuildingElement(
            chapter_id=chapter_id,
            name=name,
            element_type=element_type,
            **kwargs,
        )
        self.db.add(element)
        self.db.commit()
        self.db.refresh(element)
        return element

    def list_worldbuilding(self, chapter_id: int, story_id: int, user_id: int):
        chapter = self.get_chapter(chapter_id, story_id, user_id)
        return chapter.worldbuilding if chapter else []

    def create_keyevent(self, chapter_id: int, story_id: int, user_id: int, title: str, **kwargs):
        chapter = self.get_chapter(chapter_id, story_id, user_id)
        if not chapter:
            return None

        max_order = self.db.query(KeyEvent).filter(KeyEvent.chapter_id == chapter_id).count()
        event = KeyEvent(chapter_id=chapter_id, title=title, order=max_order + 1, **kwargs)
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event

    def list_keyevents(self, chapter_id: int, story_id: int, user_id: int):
        chapter = self.get_chapter(chapter_id, story_id, user_id)
        return chapter.key_events if chapter else []

    async def summarize_chapter(self, chapter_id: int, story_id: int, user_id: int) -> Optional[str]:
        chapter = self.get_chapter(chapter_id, story_id, user_id)
        if not chapter or not chapter.content:
            return None

        summary = await openrouter_service.summarize_text(chapter.content)
        chapter.summary = summary
        self.db.commit()
        self.db.refresh(chapter)
        return summary

    async def generate_prose(
        self,
        chapter: Chapter,
        story: Story,
        characters: list,
        beats: list,
        key_events: list,
        worldbuilding: list,
        prompt: str = "",
        model: str = "default",
    ) -> str:
        context = (
            f"Story: {story.title}\n"
            f"Premise: {story.premise}\n"
            f"Genre: {story.genre}\n\n"
            f"Chapter: {chapter.title}"
        )

        if chapter.summary:
            context += f"\nSummary: {chapter.summary}"
        if characters:
            context += "\n\nCharacters: " + ", ".join(f"{c.name} ({c.role})" for c in characters)
        if beats:
            context += "\n\nBeats: " + "; ".join(f"{b.title}: {b.content}" for b in beats)
        if key_events:
            context += "\n\nKey events: " + "; ".join(e.title for e in key_events)
        if worldbuilding:
            context += "\n\nWorld: " + "; ".join(f"{w.name} ({w.element_type})" for w in worldbuilding)
        if chapter.content:
            context += f"\n\nExisting content:\n{chapter.content}"

        messages = [
            {"role": "system", "content": "You are a creative writing assistant."},
            {"role": "user", "content": context + f"\n\n{prompt or 'Continue the story.'}"},
        ]
        return await openrouter_service.chat(messages, model=model)

    async def expand_beat(
        self,
        beat: BeatScene,
        chapter: Chapter,
        story: Story,
        characters: list,
        model: str = "default",
    ) -> str:
        context = (
            f"Story: {story.title}\n"
            f"Chapter: {chapter.title}\n\n"
            f"Beat: {beat.title}\n{beat.content}\n\n"
            f"Characters: {', '.join(c.name for c in characters)}"
        )
        messages = [
            {"role": "system", "content": "Expand this beat into a detailed scene."},
            {"role": "user", "content": context},
        ]
        return await openrouter_service.chat(messages, model=model)

    async def query_context(
        self,
        story_id: int,
        user_id: int,
        question: str,
        chapter_id: Optional[int] = None,
        model: str = "default",
    ) -> str:
        story = self.get_story(story_id, user_id)
        if not story:
            return "Story not found"

        context = f"Story: {story.title}\nPremise: {story.premise}"

        if story.characters:
            context += "\n\nCharacters: " + ", ".join(
                f"{char.name}: {char.traits}" for char in story.characters
            )

        chapters = sorted(story.chapters, key=lambda chapter: chapter.order)
        if chapter_id is not None:
            chapters = [chapter for chapter in chapters if chapter.id == chapter_id]

        for chapter in chapters:
            context += f"\n\n--- Chapter {chapter.order}: {chapter.title} ---"
            if chapter.content:
                context += "\n" + chapter.content[-2000:]

        messages = [
            {"role": "system", "content": "Answer based on story context."},
            {"role": "user", "content": context + f"\n\nQuestion: {question}"},
        ]
        return await openrouter_service.chat(messages, model=model)

```

## backend/services/vector_service.py

```python
import hashlib
from typing import Optional

from sqlalchemy.orm import Session

from models import VectorEmbedding
from services.openrouter_service import openrouter_service


async def add_memory(
    db: Session,
    project_id: int,
    content: str,
    metadata: Optional[dict] = None,
) -> VectorEmbedding:
    content_hash = hashlib.sha256(content.encode("utf-8", errors="ignore")).hexdigest()
    existing = (
        db.query(VectorEmbedding)
        .filter(VectorEmbedding.project_id == project_id, VectorEmbedding.content_hash == content_hash)
        .first()
    )
    if existing:
        return existing

    embedding = await openrouter_service.get_embedding(content)
    record = VectorEmbedding(
        project_id=project_id,
        content=content,
        content_hash=content_hash,
        embedding=embedding,
        meta=metadata or {},
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


async def search_memory(db: Session, project_id: int, query: str, top_k: int = 10) -> list[VectorEmbedding]:
    query_emb = await openrouter_service.get_embedding(query)
    memories = db.query(VectorEmbedding).filter(VectorEmbedding.project_id == project_id).all()

    def cosine(a: list[float], b: list[float]) -> float:
        if not a or not b:
            return 0.0
        length = min(len(a), len(b))
        a = a[:length]
        b = b[:length]
        dot = sum(x * y for x, y in zip(a, b))
        mag = (sum(x * x for x in a) * sum(y * y for y in b)) ** 0.5
        return dot / mag if mag else 0.0

    scored = [(memory, cosine(query_emb, memory.embedding or [])) for memory in memories]
    scored.sort(key=lambda item: item[1], reverse=True)
    return [memory for memory, _ in scored[:top_k]]


def delete_memory(db: Session, memory_id: int, project_id: int) -> bool:
    memory = (
        db.query(VectorEmbedding)
        .filter(VectorEmbedding.id == memory_id, VectorEmbedding.project_id == project_id)
        .first()
    )
    if not memory:
        return False

    db.delete(memory)
    db.commit()
    return True

```

## src/App.tsx

```tsx
import type { ReactNode } from 'react';
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';

import { AuthProvider, useAuth } from './context/AuthContext';
import LoginPage from './features/auth/LoginPage';
import Dashboard from './features/dashboard/Dashboard';
import EditorWorkspace from './features/editor/EditorWorkspace';
import LandingPage from './features/landing/LandingPage';
import StoryDashboard from './features/stories/StoryDashboard';
import StoryEditor from './features/stories/StoryEditor';

function ProtectedRoute({ children }: { children: ReactNode }) {
  const { user } = useAuth();
  return user ? <>{children}</> : <Navigate to="/login" />;
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/stories"
            element={
              <ProtectedRoute>
                <StoryDashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/story/:id"
            element={
              <ProtectedRoute>
                <StoryEditor />
              </ProtectedRoute>
            }
          />
          <Route
            path="/workspace/:projectId"
            element={
              <ProtectedRoute>
                <EditorWorkspace />
              </ProtectedRoute>
            }
          />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

```

## src/App.css

```css
#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.react:hover {
  filter: drop-shadow(0 0 2em #61dafbaa);
}

@keyframes logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: no-preference) {
  a:nth-of-type(2) .logo {
    animation: logo-spin infinite 20s linear;
  }
}

.card {
  padding: 2em;
}

.read-the-docs {
  color: #888;
}

```

## src/index.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

html,
body,
#root {
  width: 100%;
  min-height: 100%;
  margin: 0;
  padding: 0;
}

body {
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  background: #0f172a;
}

```

## src/main.tsx

```tsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)

```

## src/assets/react.svg

```xml
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="iconify iconify--logos" width="35.93" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 256 228"><path fill="#00D8FF" d="M210.483 73.824a171.49 171.49 0 0 0-8.24-2.597c.465-1.9.893-3.777 1.273-5.621c6.238-30.281 2.16-54.676-11.769-62.708c-13.355-7.7-35.196.329-57.254 19.526a171.23 171.23 0 0 0-6.375 5.848a155.866 155.866 0 0 0-4.241-3.917C100.759 3.829 77.587-4.822 63.673 3.233C50.33 10.957 46.379 33.89 51.995 62.588a170.974 170.974 0 0 0 1.892 8.48c-3.28.932-6.445 1.924-9.474 2.98C17.309 83.498 0 98.307 0 113.668c0 15.865 18.582 31.778 46.812 41.427a145.52 145.52 0 0 0 6.921 2.165a167.467 167.467 0 0 0-2.01 9.138c-5.354 28.2-1.173 50.591 12.134 58.266c13.744 7.926 36.812-.22 59.273-19.855a145.567 145.567 0 0 0 5.342-4.923a168.064 168.064 0 0 0 6.92 6.314c21.758 18.722 43.246 26.282 56.54 18.586c13.731-7.949 18.194-32.003 12.4-61.268a145.016 145.016 0 0 0-1.535-6.842c1.62-.48 3.21-.974 4.76-1.488c29.348-9.723 48.443-25.443 48.443-41.52c0-15.417-17.868-30.326-45.517-39.844Zm-6.365 70.984c-1.4.463-2.836.91-4.3 1.345c-3.24-10.257-7.612-21.163-12.963-32.432c5.106-11 9.31-21.767 12.459-31.957c2.619.758 5.16 1.557 7.61 2.4c23.69 8.156 38.14 20.213 38.14 29.504c0 9.896-15.606 22.743-40.946 31.14Zm-10.514 20.834c2.562 12.94 2.927 24.64 1.23 33.787c-1.524 8.219-4.59 13.698-8.382 15.893c-8.067 4.67-25.32-1.4-43.927-17.412a156.726 156.726 0 0 1-6.437-5.87c7.214-7.889 14.423-17.06 21.459-27.246c12.376-1.098 24.068-2.894 34.671-5.345a134.17 134.17 0 0 1 1.386 6.193ZM87.276 214.515c-7.882 2.783-14.16 2.863-17.955.675c-8.075-4.657-11.432-22.636-6.853-46.752a156.923 156.923 0 0 1 1.869-8.499c10.486 2.32 22.093 3.988 34.498 4.994c7.084 9.967 14.501 19.128 21.976 27.15a134.668 134.668 0 0 1-4.877 4.492c-9.933 8.682-19.886 14.842-28.658 17.94ZM50.35 144.747c-12.483-4.267-22.792-9.812-29.858-15.863c-6.35-5.437-9.555-10.836-9.555-15.216c0-9.322 13.897-21.212 37.076-29.293c2.813-.98 5.757-1.905 8.812-2.773c3.204 10.42 7.406 21.315 12.477 32.332c-5.137 11.18-9.399 22.249-12.634 32.792a134.718 134.718 0 0 1-6.318-1.979Zm12.378-84.26c-4.811-24.587-1.616-43.134 6.425-47.789c8.564-4.958 27.502 2.111 47.463 19.835a144.318 144.318 0 0 1 3.841 3.545c-7.438 7.987-14.787 17.08-21.808 26.988c-12.04 1.116-23.565 2.908-34.161 5.309a160.342 160.342 0 0 1-1.76-7.887Zm110.427 27.268a347.8 347.8 0 0 0-7.785-12.803c8.168 1.033 15.994 2.404 23.343 4.08c-2.206 7.072-4.956 14.465-8.193 22.045a381.151 381.151 0 0 0-7.365-13.322Zm-45.032-43.861c5.044 5.465 10.096 11.566 15.065 18.186a322.04 322.04 0 0 0-30.257-.006c4.974-6.559 10.069-12.652 15.192-18.18ZM82.802 87.83a323.167 323.167 0 0 0-7.227 13.238c-3.184-7.553-5.909-14.98-8.134-22.152c7.304-1.634 15.093-2.97 23.209-3.984a321.524 321.524 0 0 0-7.848 12.897Zm8.081 65.352c-8.385-.936-16.291-2.203-23.593-3.793c2.26-7.3 5.045-14.885 8.298-22.6a321.187 321.187 0 0 0 7.257 13.246c2.594 4.48 5.28 8.868 8.038 13.147Zm37.542 31.03c-5.184-5.592-10.354-11.779-15.403-18.433c4.902.192 9.899.29 14.978.29c5.218 0 10.376-.117 15.453-.343c-4.985 6.774-10.018 12.97-15.028 18.486Zm52.198-57.817c3.422 7.8 6.306 15.345 8.596 22.52c-7.422 1.694-15.436 3.058-23.88 4.071a382.417 382.417 0 0 0 7.859-13.026a347.403 347.403 0 0 0 7.425-13.565Zm-16.898 8.101a358.557 358.557 0 0 1-12.281 19.815a329.4 329.4 0 0 1-23.444.823c-7.967 0-15.716-.248-23.178-.732a310.202 310.202 0 0 1-12.513-19.846h.001a307.41 307.41 0 0 1-10.923-20.627a310.278 310.278 0 0 1 10.89-20.637l-.001.001a307.318 307.318 0 0 1 12.413-19.761c7.613-.576 15.42-.876 23.31-.876H128c7.926 0 15.743.303 23.354.883a329.357 329.357 0 0 1 12.335 19.695a358.489 358.489 0 0 1 11.036 20.54a329.472 329.472 0 0 1-11 20.722Zm22.56-122.124c8.572 4.944 11.906 24.881 6.52 51.026c-.344 1.668-.73 3.367-1.15 5.09c-10.622-2.452-22.155-4.275-34.23-5.408c-7.034-10.017-14.323-19.124-21.64-27.008a160.789 160.789 0 0 1 5.888-5.4c18.9-16.447 36.564-22.941 44.612-18.3ZM128 90.808c12.625 0 22.86 10.235 22.86 22.86s-10.235 22.86-22.86 22.86s-22.86-10.235-22.86-22.86s10.235-22.86 22.86-22.86Z"></path></svg>
```

## src/context/AuthContext.tsx

```tsx
import { createContext, useContext, useEffect, useState } from 'react';
import type { ReactNode } from 'react';

import { api } from '../services/api';

interface User {
  id: number;
  email: string;
  username: string;
}

interface AuthContextType {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  signup: (email: string, username: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      api
        .get<User>('/api/auth/me')
        .then(setUser)
        .catch(() => localStorage.removeItem('token'));
    }
  }, []);

  const login = async (email: string, password: string) => {
    const form = new FormData();
    form.append('email', email);
    form.append('password', password);

    const data = await api.postForm<{ token: string; user: User }>('/api/auth/login', form);
    localStorage.setItem('token', data.token);
    setUser(data.user);
  };

  const signup = async (email: string, username: string, password: string) => {
    const form = new FormData();
    form.append('email', email);
    form.append('username', username);
    form.append('password', password);

    const data = await api.postForm<{ token: string; user: User }>('/api/auth/signup', form);
    localStorage.setItem('token', data.token);
    setUser(data.user);
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
  };

  return <AuthContext.Provider value={{ user, login, signup, logout }}>{children}</AuthContext.Provider>;
}

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
};

```

## src/services/api.ts

```typescript
const getApiBase = () => {
  if (import.meta.env.VITE_API_URL) return import.meta.env.VITE_API_URL;

  const href = window.location.href;
  if (href.includes('-3000.')) return href.replace('-3000', '-8000');
  if (href.includes('.railway.') || href.includes('.up.railway.')) return '';

  return 'http://localhost:8000';
};

export const API_BASE = getApiBase();

const getAuthHeaders = (): Record<string, string> => {
  const token = localStorage.getItem('token');
  return token ? { Authorization: `Bearer ${token}` } : {};
};

export const api = {
  async get<T>(path: string): Promise<T> {
    const res = await fetch(`${API_BASE}${path}`, {
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    });
    if (!res.ok) throw new Error(await res.text());
    return res.json();
  },

  async post<T>(path: string, data?: unknown): Promise<T> {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: data ? JSON.stringify(data) : undefined,
    });
    if (!res.ok) throw new Error(await res.text());
    return res.json();
  },

  async postForm<T>(path: string, formData: FormData): Promise<T> {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: formData,
    });
    if (!res.ok) throw new Error(await res.text());
    return res.json();
  },

  async put<T>(path: string, data?: unknown): Promise<T> {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
      body: data ? JSON.stringify(data) : undefined,
    });
    if (!res.ok) throw new Error(await res.text());
    return res.json();
  },

  async delete(path: string): Promise<void> {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'DELETE',
      headers: getAuthHeaders(),
    });
    if (!res.ok) throw new Error(await res.text());
  },

  async chatStream(
    projectId: number,
    message: string,
    selectedText = '',
    model = 'default',
  ): Promise<ReadableStream<Uint8Array> | null> {
    const params = new URLSearchParams({ message, selected_text: selectedText, model });
    const response = await fetch(`${API_BASE}/api/projects/${projectId}/chat/stream?${params}`, {
      headers: getAuthHeaders(),
    });
    if (!response.ok) throw new Error('Chat failed');
    return response.body;
  },

  async generate(data: {
    prompt: string;
    story_id: number;
    chapter_id?: number;
    context_type: string;
    model?: string;
  }) {
    return this.post<{ content: string }>('/api/ai/generate', data);
  },

  async getModels() {
    return this.get<{ id: string; name: string }[]>('/api/models');
  },
};

```

## src/features/landing/LandingPage.tsx

```tsx
import { Link } from 'react-router-dom';

import { useAuth } from '../../context/AuthContext';

export default function LandingPage() {
  const { user } = useAuth();

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white">
      <nav className="flex items-center justify-between p-6">
        <h1 className="bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-3xl font-bold text-transparent">
          Membrane + Story Engine
        </h1>
        <div className="space-x-4">
          {user ? (
            <Link to="/dashboard" className="rounded-lg bg-purple-600 px-4 py-2 hover:bg-purple-500">
              Go to Dashboard
            </Link>
          ) : (
            <Link to="/login" className="rounded-lg bg-purple-600 px-4 py-2 hover:bg-purple-500">
              Sign In
            </Link>
          )}
        </div>
      </nav>
      <main className="container mx-auto px-6 py-20">
        <h2 className="mb-6 text-5xl font-bold">Write with AI-Powered Precision</h2>
        <p className="mb-8 max-w-2xl text-xl text-gray-300">
          A full-stack writing platform combining collaborative document editing with AI-powered story
          planning. Features include context-aware AI chat, semantic memory, chapter organization,
          character tracking, and beat-based scene generation.
        </p>
        <div className="mt-16 grid gap-8 md:grid-cols-2">
          <div className="rounded-xl border border-purple-500/30 bg-slate-800/50 p-6">
            <h3 className="mb-4 text-2xl font-bold text-purple-400">Membrane Workspace</h3>
            <ul className="space-y-2 text-gray-300">
              <li>Real-time document editing</li>
              <li>AI-powered chat assistance</li>
              <li>File upload with semantic indexing</li>
              <li>Vector-based memory and context</li>
            </ul>
          </div>
          <div className="rounded-xl border border-pink-500/30 bg-slate-800/50 p-6">
            <h3 className="mb-4 text-2xl font-bold text-pink-400">Story Engine</h3>
            <ul className="space-y-2 text-gray-300">
              <li>Multi-story management</li>
              <li>Chapter organization</li>
              <li>Character development</li>
              <li>AI prose generation</li>
            </ul>
          </div>
        </div>
      </main>
    </div>
  );
}

```

## src/features/auth/LoginPage.tsx

```tsx
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

import { useAuth } from '../../context/AuthContext';

export default function LoginPage() {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const { login, signup } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    try {
      if (isLogin) {
        await login(email, password);
      } else {
        await signup(email, username, password);
      }
      navigate('/dashboard');
    } catch {
      setError('Authentication failed');
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 p-4">
      <div className="w-full max-w-md rounded-2xl border border-purple-500/30 bg-slate-800/80 p-8">
        <h1 className="mb-6 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-center text-3xl font-bold text-transparent">
          {isLogin ? 'Sign In' : 'Create Account'}
        </h1>

        {error && <div className="mb-4 rounded-lg border border-red-500 bg-red-500/20 p-3 text-red-300">{error}</div>}

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full rounded-lg border border-slate-600 bg-slate-700 p-3 text-white focus:border-purple-500 focus:outline-none"
            required
          />
          {!isLogin && (
            <input
              type="text"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full rounded-lg border border-slate-600 bg-slate-700 p-3 text-white focus:border-purple-500 focus:outline-none"
              required
            />
          )}
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full rounded-lg border border-slate-600 bg-slate-700 p-3 text-white focus:border-purple-500 focus:outline-none"
            required
          />
          <button type="submit" className="w-full rounded-lg bg-gradient-to-r from-purple-600 to-pink-600 py-3 font-bold hover:opacity-90">
            {isLogin ? 'Sign In' : 'Create Account'}
          </button>
        </form>

        <p className="mt-4 text-center text-gray-400">
          {isLogin ? "Don't have an account? " : 'Already have an account? '}
          <button onClick={() => setIsLogin(!isLogin)} className="text-purple-400 hover:underline">
            {isLogin ? 'Sign up' : 'Sign in'}
          </button>
        </p>

        <Link to="/" className="mt-4 block text-center text-gray-400 hover:text-white">
          Back to Home
        </Link>
      </div>
    </div>
  );
}

```

## src/features/dashboard/Dashboard.tsx

```tsx
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

import { useAuth } from '../../context/AuthContext';
import { api } from '../../services/api';

interface Project {
  id: number;
  name: string;
  description: string;
  updated_at: string;
}

export default function Dashboard() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [newName, setNewName] = useState('');

  const { user, logout } = useAuth();

  useEffect(() => {
    void loadProjects();
  }, []);

  const loadProjects = async () => {
    setProjects(await api.get<Project[]>('/api/projects'));
  };

  const createProject = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newName.trim()) return;

    await api.post('/api/projects', { name: newName });
    setNewName('');
    await loadProjects();
  };

  const deleteProject = async (id: number) => {
    if (!window.confirm('Delete this project?')) return;
    await api.delete(`/api/projects/${id}`);
    await loadProjects();
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white">
      <nav className="flex items-center justify-between border-b border-slate-700 bg-slate-800 p-4">
        <h1 className="text-xl font-bold">Membrane Workspace</h1>
        <div className="flex items-center gap-4">
          <Link to="/stories" className="rounded-lg bg-pink-600 px-4 py-2 hover:bg-pink-500">
            Story Engine
          </Link>
          <span className="text-gray-400">{user?.email}</span>
          <button onClick={logout} className="text-gray-400 hover:text-white">
            Logout
          </button>
        </div>
      </nav>

      <main className="container mx-auto p-6">
        <form onSubmit={createProject} className="mb-8 flex gap-4">
          <input
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
            placeholder="New project name..."
            className="flex-1 rounded-lg border border-slate-700 bg-slate-800 p-3 focus:border-purple-500 focus:outline-none"
          />
          <button type="submit" className="rounded-lg bg-purple-600 px-6 hover:bg-purple-500">
            Create
          </button>
        </form>

        <div className="grid gap-4 md:grid-cols-3">
          {projects.map((project) => (
            <div
              key={project.id}
              className="rounded-lg border border-slate-700 bg-slate-800 p-4 transition hover:border-purple-500"
            >
              <Link to={`/workspace/${project.id}`} className="text-lg font-bold hover:text-purple-400">
                {project.name}
              </Link>
              <p className="mt-1 text-sm text-gray-400">{project.description || 'No description'}</p>
              <div className="mt-3 flex gap-2">
                <Link to={`/workspace/${project.id}`} className="text-sm text-purple-400 hover:underline">
                  Open
                </Link>
                <button onClick={() => deleteProject(project.id)} className="text-sm text-red-400 hover:underline">
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}

```

## src/features/editor/EditorWorkspace.tsx

```tsx
import { useEffect, useRef, useState } from 'react';
import { Link, useParams } from 'react-router-dom';

import { api } from '../../services/api';

interface Project {
  id: number;
  name: string;
  description: string;
}

interface Document {
  id: number;
  content: string;
}

interface ChatMessage {
  role: string;
  content: string;
}

interface FileItem {
  id: number;
  filename: string;
  train: boolean;
}

export default function EditorWorkspace() {
  const { projectId } = useParams<{ projectId: string }>();

  const [project, setProject] = useState<Project | null>(null);
  const [content, setContent] = useState('');
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState('');
  const [selectedText, setSelectedText] = useState('');
  const [streaming, setStreaming] = useState(false);
  const [models, setModels] = useState<{ id: string; name: string }[]>([]);
  const [model, setModel] = useState('default');
  const [files, setFiles] = useState<FileItem[]>([]);

  const messagesEnd = useRef<HTMLDivElement>(null);
  const saveTimeout = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    if (projectId) {
      void loadProject();
      void loadFiles();
    }
    void loadModels();
  }, [projectId]);

  useEffect(() => {
    messagesEnd.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const loadProject = async () => {
    const projectData = await api.get<Project>(`/api/projects/${projectId}`);
    const docData = await api.get<Document>(`/api/projects/${projectId}/document`);
    setProject(projectData);
    setContent(docData.content || '');
  };

  const loadFiles = async () => {
    setFiles(await api.get<FileItem[]>(`/api/projects/${projectId}/upload/list`));
  };

  const loadModels = async () => {
    setModels(await api.getModels());
  };

  const saveContent = (newContent: string) => {
    setContent(newContent);

    if (saveTimeout.current) {
      clearTimeout(saveTimeout.current);
    }

    saveTimeout.current = setTimeout(() => {
      void api.put(`/api/projects/${projectId}/document`, { content: newContent });
    }, 1000);
  };

  const handleSelect = () => {
    const sel = window.getSelection()?.toString() || '';
    if (sel) setSelectedText(sel);
  };

  const sendMessage = async () => {
    if (!input.trim() || streaming || !projectId) return;

    const userMsg: ChatMessage = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setStreaming(true);

    try {
      const stream = await api.chatStream(parseInt(projectId, 10), input, selectedText, model);
      const reader = stream?.getReader();
      const decoder = new TextDecoder();
      const assistantMsg: ChatMessage = { role: 'assistant', content: '' };
      setMessages((prev) => [...prev, assistantMsg]);

      while (reader) {
        const { done, value } = await reader.read();
        if (done) break;

        const text = decoder.decode(value);
        const lines = text.split('\n');

        for (const line of lines) {
          if (!line.startsWith('data: ')) continue;

          const data = line.slice(6);
          if (data === '[DONE]') continue;

          try {
            const chunk = JSON.parse(data) as { content?: string };
            if (chunk.content) {
              assistantMsg.content += chunk.content;
              setMessages((prev) => [...prev.slice(0, -1), { ...assistantMsg }]);
            }
          } catch {
            // Ignore malformed stream chunks.
          }
        }
      }
    } finally {
      setStreaming(false);
      setSelectedText('');
    }
  };

  const uploadFile = async (e: React.ChangeEvent<HTMLInputElement>, train: boolean) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const form = new FormData();
    form.append('file', file);
    form.append('train', String(train));

    await api.postForm(`/api/projects/${projectId}/upload/file`, form);
    await loadFiles();
  };

  return (
    <div className="flex h-screen flex-col bg-slate-900 text-white">
      <nav className="flex items-center justify-between border-b border-slate-700 bg-slate-800 p-3">
        <div className="flex items-center gap-4">
          <Link to="/dashboard" className="text-gray-400 hover:text-white">
            Back
          </Link>
          <span className="font-bold">{project?.name}</span>
        </div>
        <select value={model} onChange={(e) => setModel(e.target.value)} className="rounded bg-slate-700 p-2">
          {models.map((modelItem) => (
            <option key={modelItem.id} value={modelItem.id}>
              {modelItem.name}
            </option>
          ))}
        </select>
      </nav>

      <div className="flex flex-1 overflow-hidden">
        <div className="flex flex-1 flex-col">
          <div className="flex items-center justify-between border-b border-slate-700 bg-slate-800/50 p-2">
            <span className="text-sm text-gray-400">Document</span>
            <span className="text-xs text-gray-500">Auto-saving...</span>
          </div>
          <textarea
            value={content}
            onChange={(e) => saveContent(e.target.value)}
            onSelect={handleSelect}
            className="flex-1 resize-none bg-slate-900 p-6 font-mono text-sm leading-relaxed focus:outline-none"
            placeholder="Start writing..."
          />
          {selectedText && (
            <div className="border-t border-purple-500/50 bg-purple-900/30 p-2 text-sm">
              Selected: "{selectedText.slice(0, 100)}..."
            </div>
          )}
        </div>

        <div className="flex w-80 flex-col border-l border-slate-700 bg-slate-800">
          <div className="border-b border-slate-700 p-3">
            <h3 className="font-bold">AI Chat</h3>
          </div>
          <div className="flex-1 space-y-3 overflow-y-auto p-3">
            {messages.map((message, index) => (
              <div
                key={index}
                className={`rounded-lg p-3 ${
                  message.role === 'user' ? 'ml-8 bg-purple-900/50' : 'mr-8 bg-slate-700'
                }`}
              >
                <div className="mb-1 text-xs text-gray-400">{message.role}</div>
                <div className="whitespace-pre-wrap text-sm">{message.content}</div>
              </div>
            ))}
            <div ref={messagesEnd} />
          </div>

          <div className="border-t border-slate-700 p-3">
            <div className="flex gap-2">
              <input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    void sendMessage();
                  }
                }}
                placeholder="Ask AI..."
                className="flex-1 rounded bg-slate-700 p-2 text-sm"
                disabled={streaming}
              />
              <button
                onClick={() => {
                  void sendMessage();
                }}
                disabled={streaming || !input.trim()}
                className="rounded bg-purple-600 px-4 text-sm disabled:opacity-50"
              >
                {streaming ? '...' : 'Send'}
              </button>
            </div>
            <div className="mt-2 flex gap-2">
              <button
                onClick={() => setInput(`/improve ${selectedText}`)}
                disabled={!selectedText}
                className="rounded bg-slate-700 px-2 py-1 text-xs disabled:opacity-50"
              >
                Improve
              </button>
              <button
                onClick={() => setInput(`/expand ${selectedText}`)}
                disabled={!selectedText}
                className="rounded bg-slate-700 px-2 py-1 text-xs disabled:opacity-50"
              >
                Expand
              </button>
              <button
                onClick={() => setInput(`/simplify ${selectedText}`)}
                disabled={!selectedText}
                className="rounded bg-slate-700 px-2 py-1 text-xs disabled:opacity-50"
              >
                Simplify
              </button>
            </div>
          </div>
        </div>
      </div>

      <div className="flex gap-4 border-t border-slate-700 bg-slate-800 p-2 text-xs">
        <div>
          <span className="text-gray-400">Files: </span>
          <label className="cursor-pointer text-purple-400 hover:underline">
            Upload
            <input
              type="file"
              className="hidden"
              onChange={(e) => {
                void uploadFile(e, false);
              }}
            />
          </label>
        </div>
        <div>
          <span className="text-gray-400">Train: </span>
          <label className="cursor-pointer text-pink-400 hover:underline">
            Upload
            <input
              type="file"
              className="hidden"
              onChange={(e) => {
                void uploadFile(e, true);
              }}
            />
          </label>
        </div>
        {files.map((file) => (
          <span key={file.id} className="text-gray-500">
            {file.filename}
          </span>
        ))}
      </div>
    </div>
  );
}

```

## src/features/stories/StoryDashboard.tsx

```tsx
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

import { useAuth } from '../../context/AuthContext';
import { api } from '../../services/api';

interface Story {
  id: number;
  title: string;
  genre: string;
  premise: string;
  updated_at: string;
}

export default function StoryDashboard() {
  const [stories, setStories] = useState<Story[]>([]);
  const [showForm, setShowForm] = useState(false);
  const [newStory, setNewStory] = useState({ title: '', genre: '', premise: '' });

  const { user, logout } = useAuth();

  useEffect(() => {
    void loadStories();
  }, []);

  const loadStories = async () => {
    setStories(await api.get<Story[]>('/api/stories'));
  };

  const createStory = async (e: React.FormEvent) => {
    e.preventDefault();
    await api.post('/api/stories', newStory);
    setShowForm(false);
    setNewStory({ title: '', genre: '', premise: '' });
    await loadStories();
  };

  const deleteStory = async (id: number) => {
    if (!window.confirm('Delete this story?')) return;
    await api.delete(`/api/stories/${id}`);
    await loadStories();
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white">
      <nav className="flex items-center justify-between border-b border-slate-700 bg-slate-800 p-4">
        <h1 className="text-xl font-bold">Story Engine</h1>
        <div className="flex items-center gap-4">
          <Link to="/dashboard" className="rounded-lg bg-slate-700 px-4 py-2 hover:bg-slate-600">
            Membrane
          </Link>
          <span className="text-gray-400">{user?.email}</span>
          <button onClick={logout} className="text-gray-400 hover:text-white">
            Logout
          </button>
        </div>
      </nav>

      <main className="container mx-auto p-6">
        <button onClick={() => setShowForm(!showForm)} className="mb-6 rounded-lg bg-pink-600 px-6 py-2 hover:bg-pink-500">
          + New Story
        </button>

        {showForm && (
          <form onSubmit={createStory} className="mb-8 rounded-lg border border-pink-500/30 bg-slate-800 p-6">
            <input
              value={newStory.title}
              onChange={(e) => setNewStory({ ...newStory, title: e.target.value })}
              placeholder="Story title"
              className="mb-3 w-full rounded-lg border border-slate-600 bg-slate-700 p-3"
              required
            />
            <input
              value={newStory.genre}
              onChange={(e) => setNewStory({ ...newStory, genre: e.target.value })}
              placeholder="Genre"
              className="mb-3 w-full rounded-lg border border-slate-600 bg-slate-700 p-3"
            />
            <textarea
              value={newStory.premise}
              onChange={(e) => setNewStory({ ...newStory, premise: e.target.value })}
              placeholder="Premise"
              className="mb-3 w-full rounded-lg border border-slate-600 bg-slate-700 p-3"
              rows={3}
            />
            <button type="submit" className="rounded-lg bg-pink-600 px-6 py-2 hover:bg-pink-500">
              Create Story
            </button>
          </form>
        )}

        <div className="grid gap-4 md:grid-cols-3">
          {stories.map((story) => (
            <div
              key={story.id}
              className="rounded-lg border border-slate-700 bg-slate-800 p-4 transition hover:border-pink-500"
            >
              <Link to={`/story/${story.id}`} className="text-lg font-bold hover:text-pink-400">
                {story.title}
              </Link>
              <p className="mt-1 text-sm text-gray-400">{story.genre || 'No genre'}</p>
              <p className="mt-2 line-clamp-2 text-sm text-gray-500">{story.premise || 'No premise'}</p>
              <div className="mt-3 flex gap-2">
                <Link to={`/story/${story.id}`} className="text-sm text-pink-400 hover:underline">
                  Open
                </Link>
                <button onClick={() => deleteStory(story.id)} className="text-sm text-red-400 hover:underline">
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}

```

## src/features/stories/StoryEditor.tsx

```tsx
import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';

import { api } from '../../services/api';

interface Story {
  id: number;
  title: string;
  genre: string;
  premise: string;
  chapters: Chapter[];
  characters: Character[];
}

interface Chapter {
  id: number;
  title: string;
  content: string;
  summary: string;
  order: number;
  beats: Beat[];
  key_events: KeyEvent[];
  worldbuilding: WorldElement[];
}

interface Character {
  id: number;
  name: string;
  role: string;
  traits: string;
  backstory: string;
}

interface Beat {
  id: number;
  title: string;
  content: string;
  beat_type: string;
}

interface KeyEvent {
  id: number;
  title: string;
  description: string;
}

interface WorldElement {
  id: number;
  name: string;
  element_type: string;
  description: string;
}

export default function StoryEditor() {
  const { id } = useParams<{ id: string }>();

  const [story, setStory] = useState<Story | null>(null);
  const [activeChapter, setActiveChapter] = useState<number | null>(null);
  const [generating, setGenerating] = useState(false);
  const [showCharacters, setShowCharacters] = useState(false);
  const [newCharacter, setNewCharacter] = useState({ name: '', role: '', traits: '', backstory: '' });

  useEffect(() => {
    if (!id) return;
    void loadStory();
  }, [id]);

  const loadStory = async () => {
    const data = await api.get<Story>(`/api/stories/${id}`);
    setStory(data);
    if (data.chapters?.length && !activeChapter) {
      setActiveChapter(data.chapters[0].id);
    }
  };

  const updateChapter = async (content: string) => {
    if (!activeChapter) return;
    await api.put(`/api/chapters/${activeChapter}`, { content });
    await loadStory();
  };

  const createChapter = async () => {
    await api.post(`/api/stories/${id}/chapters`, {
      title: `Chapter ${(story?.chapters.length || 0) + 1}`,
    });
    await loadStory();
  };

  const generate = async (type: string, prompt = '') => {
    if (!story || !activeChapter) return;

    setGenerating(true);
    try {
      const result = await api.generate({
        prompt,
        story_id: story.id,
        chapter_id: activeChapter,
        context_type: type,
      });

      if (type === 'prose') {
        const chapter = story.chapters.find((item) => item.id === activeChapter);
        await updateChapter(`${chapter?.content || ''}\n\n${result.content}`);
      }
    } finally {
      setGenerating(false);
    }
  };

  const summarizeChapter = async () => {
    if (!activeChapter) return;
    await api.post(`/api/chapters/${activeChapter}/summarize`);
    await loadStory();
  };

  const createCharacter = async (e: React.FormEvent) => {
    e.preventDefault();
    await api.post(`/api/stories/${id}/characters`, newCharacter);
    setNewCharacter({ name: '', role: '', traits: '', backstory: '' });
    setShowCharacters(false);
    await loadStory();
  };

  if (!story) {
    return <div className="min-h-screen bg-slate-900 p-6 text-white">Loading...</div>;
  }

  const chapter = story.chapters.find((item) => item.id === activeChapter);

  return (
    <div className="min-h-screen bg-slate-900 text-white">
      <nav className="flex items-center justify-between border-b border-slate-700 bg-slate-800 p-3">
        <div className="flex items-center gap-4">
          <Link to="/stories" className="text-gray-400 hover:text-white">
            Back
          </Link>
          <span className="font-bold">{story.title}</span>
          <span className="text-sm text-gray-500">({story.genre})</span>
        </div>
        <div className="flex gap-2">
          <button onClick={() => setShowCharacters(!showCharacters)} className="rounded bg-slate-700 px-3 py-1 hover:bg-slate-600">
            Characters
          </button>
        </div>
      </nav>

      <div className="flex">
        <aside className="w-64 border-r border-slate-700 bg-slate-800/50 p-4">
          <h3 className="mb-3 font-bold">Chapters</h3>
          {story.chapters.map((chapterItem) => (
            <button
              key={chapterItem.id}
              onClick={() => setActiveChapter(chapterItem.id)}
              className={`mb-1 w-full rounded p-2 text-left ${
                chapterItem.id === activeChapter ? 'bg-purple-600' : 'bg-slate-700 hover:bg-slate-600'
              }`}
            >
              {chapterItem.title}
            </button>
          ))}
          <button
            onClick={createChapter}
            className="mt-2 w-full rounded border border-dashed border-slate-600 p-2 hover:border-purple-500"
          >
            + Add Chapter
          </button>
        </aside>

        <main className="flex-1 p-6">
          {chapter && (
            <>
              <div className="mb-4 flex items-center justify-between">
                <h2 className="text-2xl font-bold">{chapter.title}</h2>
                <div className="flex gap-2">
                  <button onClick={summarizeChapter} className="rounded bg-slate-700 px-3 py-1 text-sm hover:bg-slate-600">
                    Summarize
                  </button>
                  <button
                    onClick={() => generate('prose')}
                    disabled={generating}
                    className="rounded bg-pink-600 px-3 py-1 text-sm hover:bg-pink-500 disabled:opacity-50"
                  >
                    {generating ? 'Generating...' : 'Generate Prose'}
                  </button>
                </div>
              </div>
              {chapter.summary && (
                <div className="mb-4 rounded bg-slate-800 p-3 text-sm text-gray-400">
                  <strong>Summary:</strong> {chapter.summary}
                </div>
              )}
              <textarea
                value={chapter.content}
                onChange={(e) => {
                  void updateChapter(e.target.value);
                }}
                className="h-96 w-full rounded-lg border border-slate-700 bg-slate-800 p-4 font-mono focus:border-purple-500 focus:outline-none"
                placeholder="Start writing..."
              />
            </>
          )}
        </main>

        {showCharacters && (
          <aside className="w-72 border-l border-slate-700 bg-slate-800/50 p-4">
            <h3 className="mb-3 font-bold">Characters</h3>
            <form onSubmit={createCharacter} className="mb-4 rounded bg-slate-700 p-3">
              <input
                value={newCharacter.name}
                onChange={(e) => setNewCharacter({ ...newCharacter, name: e.target.value })}
                placeholder="Name"
                className="mb-2 w-full rounded bg-slate-600 p-2 text-sm"
                required
              />
              <input
                value={newCharacter.role}
                onChange={(e) => setNewCharacter({ ...newCharacter, role: e.target.value })}
                placeholder="Role"
                className="mb-2 w-full rounded bg-slate-600 p-2 text-sm"
              />
              <input
                value={newCharacter.traits}
                onChange={(e) => setNewCharacter({ ...newCharacter, traits: e.target.value })}
                placeholder="Traits"
                className="mb-2 w-full rounded bg-slate-600 p-2 text-sm"
              />
              <button type="submit" className="w-full rounded bg-pink-600 py-1 text-sm">
                Add
              </button>
            </form>
            {story.characters?.map((character) => (
              <div key={character.id} className="mb-2 rounded bg-slate-700 p-2">
                <div className="font-bold">{character.name}</div>
                <div className="text-xs text-gray-400">{character.role}</div>
              </div>
            ))}
          </aside>
        )}
      </div>
    </div>
  );
}

```

