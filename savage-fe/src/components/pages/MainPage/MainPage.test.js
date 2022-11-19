import { render, screen } from '@testing-library/react';
import MainPage from './MainPage';

test('renders logo', () => {
  render(<MainPage />);
  const logoElement = screen.getByAltText("logo");
  expect(logoElement).toBeInTheDocument();
});
