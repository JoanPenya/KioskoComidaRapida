module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      height: {

        sm: '50px',
 
        md: '100px',
 
        lg: '200px',
 
        xl: '600px',
       }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}