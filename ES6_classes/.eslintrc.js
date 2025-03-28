module.exports = {
  env: {
    browser: true,
    es6: true,
    node: true,
  },
  extends: 'airbnb-base',
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  rules: {
    'no-underscore-dangle': 'off',
    'import/extensions': ['error', 'always'],
    'max-classes-per-file': 'off',
    'no-unused-vars': ['error', { 'args': 'none' }]
  },
}; 