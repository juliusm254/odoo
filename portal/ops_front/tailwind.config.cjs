/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  mode:'jit',
  theme: {
    extend: {},
    fontFamily: {
      'sans': ['Inter', 'Avenir', 'Helvetica',  'system-ui', 'Arial',],
      'serif': ['Georgia', 'ui-sans-serif', 'sans-serif'],
      'mono': ['ui-monospace', 'SFMono-Regular',],
      'display': ['Oswald',],
      'body': ['"Open Sans"',],
    }
  },
  plugins: [],
}
