const withMT = require("@material-tailwind/html/utils/withMT");

module.exports = withMT({
  content: [
    "./src/**/*.{html,njk}",
    //"./node_modules/tw-elements/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        // Custom color used for Bronze sponsors
        'bronze': '#ca8a04'
      },
      fontSize: {
        'h1': '3rem',
        'h2': '2.25rem',
        'h3': '1.875rem',
        'h4': '1.5rem',
        'h5': '1.25rem',
        'h6': '1rem',
      },
      fontWeight: {
        'h1': '800',
        'h2': '700',
        'h3': '600',
        'h4': '600',
        'h5': '600',
        'h6': '600',
      }
    },
  },
  //plugins: [ require("tw-elements/plugin.cjs") ],
  darkMode: "class"
});
