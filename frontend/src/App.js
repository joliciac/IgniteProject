import Hackathons from './Hackathon-Page /Hackathons.js';
import Internships from './Internships-Page/Internships';
import Leetcode from './Leetcode-Page/Leetcode';
import Home from './Home.js';
import { createBrowserRouter, RouterProvider, Route, Link, createRoutesFromElements,Outlet} from "react-router-dom";

function App() {
  const router = createBrowserRouter(
      createRoutesFromElements(
        <Route path="/" element={<Root/>}>
          <Route index element={<Home/>}/> 
          <Route  path="/hackathons" element={<Hackathons/>}/>
          <Route path="/Internships" element={<Internships/>}/>
          <Route path="/Leetcode" element={<Leetcode/>}/>         
        </Route>
      )
    );
 


  return (
    <div className="App">
      <RouterProvider router={router}/>
    </div>
  );
}

const Root = () =>{
  return (
  <>
    <div>
      <Link to="/"> Home </Link>
      <Link to="/Hackathons">Hackathons</Link>
      <Link to="/Internships">Interships</Link>
      <Link to="/Leetcode">Leetcode</Link>

    </div>
    <div><Outlet/></div>
  </>
)}

export default App;
