module.exports = {
  extends: [
    'stylelint-config-standard',
    'stylelint-config-tailwindcss',
  ],
  rules: {
    // Allow Tailwind directives
    'at-rule-no-unknown': [
      true,
      { ignoreAtRules: ['tailwind', 'apply', 'variants', 'responsive', 'screen'] },
    ],
    'no-descending-specificity': null,
  },
};