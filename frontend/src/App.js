
import './App.css';
import { Leftmenu } from "./components/Leftmenu";
import { Middlemenu } from "./components/Middlemenu";
import { Rightmenu } from "./components/Rightmenu";



function App() {
  return (
    <div className="App">
    <Leftmenu />
    <Middlemenu />
    <Rightmenu />

    <div className="background"></div>
    </div>
  );
}

export default App;
