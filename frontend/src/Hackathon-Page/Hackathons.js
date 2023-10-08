import React from 'react'
import'./Hackathons.css'
function Hackathons() {
  return (
    <div>
      <div className='Current_Hacks'>
        <p>Past Hackathons</p>
        <div className='Current_Bar'>
          <p>3rd November</p>
          <p>Hackfest</p>
          <p>[remote]</p>
        </div>
         
      </div>
      <div className='Past_Hacks'>
        <p className='Text'>Current Hackathons</p>
        <div className='pastHackOne'></div>
        <div className='pastHackTwo'></div>
        <div className='pastHackThree'></div>
        <div className='pastHackFour'></div>

      </div>
    </div>
  )
}
// add React Router
export default Hackathons