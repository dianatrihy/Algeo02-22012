import './App.css';
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import Main from './pagezz';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Main />,
  }
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;