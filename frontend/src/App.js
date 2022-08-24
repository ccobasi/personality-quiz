import { Routes,Route } from 'react-router-dom';
import Home from './components/Home';
import Quiz from './services/Quiz';

function App() {
  return (
    <div className="App">
      <Routes>
      <Route path="/" element={<Home />}/>
      <Route path="/q/:topic" element={<Quiz />}/>
      </Routes>
    </div>
  );
}

export default App;
