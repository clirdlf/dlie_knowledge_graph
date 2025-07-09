const themeToggle = document.querySelector('#toggle-theme');
const sunIcon = document.querySelector('#sun-icon');
const moonIcon = document.querySelector('#moon-icon');

// Function to set the theme
const setTheme = (theme) => {
  if (theme === 'dark') {
    document.documentElement.classList.add('dark');
    sunIcon.classList.add('hidden');
    moonIcon.classList.remove('hidden');
    localStorage.setItem('color-theme', 'dark');
  } else {
    document.documentElement.classList.remove('dark');
    sunIcon.classList.remove('hidden');
    moonIcon.classList.add('hidden');
    localStorage.setItem('color-theme', 'light');
  }
};

// Check for saved theme on page load
const savedTheme = localStorage.getItem('color-theme');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

if (savedTheme) {
  setTheme(savedTheme);
} else if (prefersDark) {
  setTheme('dark');
} else {
  setTheme('light');
}

themeToggle.addEventListener('click', () => {
  const currentTheme = localStorage.getItem('color-theme');
  if (currentTheme === 'dark') {
    setTheme('light');
  } else {
    setTheme('dark');
  }
});