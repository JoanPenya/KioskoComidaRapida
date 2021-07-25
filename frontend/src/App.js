import logo from './logo.svg';
import './App.css';
import Footer from './componentes/footer';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Crud from './router/Crud';
import Menu from './router/Menu';
import Cajero from './router/Cajero';
import Lista from './router/Lista';
import Index from './router/Index';
import Espera from './router/Espera';

function App() {
  return (
    <div className="App">
      <header className="App-header text-center my-4">
        <h1 class="text-5xl">Le Burger</h1>
      </header>

      <Router>
        <div>
          <Switch>
            <Route path="/Crud">
              <Crud />
            </Route>
            <Route path="/Menu">
              <Menu />
            </Route>
            <Route path="/Cajero">
              <Cajero />
            </Route>
            <Route path="/Lista">
              <Lista />
            </Route>

            <Route path="/Espera">
              <Espera />
            </Route>
            <Route path="/">
              <Index />
            </Route>
          </Switch>
        </div>
      </Router>

      <Footer />
    </div>
  );
}



export default App;
