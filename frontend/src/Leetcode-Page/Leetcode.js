import React from 'react'
import DataGrid from '@mui/material/Grid';

function Leetcode() {
  const columns = [
    {title:"leetcode", field:'leetcode'},
    {title:"Pattern", field:'Pattern'},
    {title:"Difficulty", field:'Difficulty'},
    {title:"Language", field:'language'},
    {title:"Company", field:'Company'},
  ]
  const rows = [
    {id:1,
    Name: "Two Sum",
    Difficulty: "Easy"},{
    id:2, 
    Name: "Invert Binary Search",
    Difficulty: "Easy"
    },{
    id:3, 
    Name: "Find The Duplicate Number",
    Difficulty: "Medium"},{
    id:4, 
    Name: "Trapping Rain Water",
    Difficulty: "Hard"
    },{
    id:5, 
    Name: "Linked List Cycle",
    Difficulty: "Easy"},{
    id:6, 
    Name: "Coin Change",
    Difficulty: "Medium",
    },{
    id:7, 
    Name: "Find The Duplicate Number",
    Difficulty: "Medium"},{
    id:8, 
    Name: "Trapping Rain Water",
    Difficulty: "Hard"}
    ]
  return (
    <div>
      <div className='Nav_Bar'>
       
       <DataGrid
        rows={rows}
        columns={columns}
        
      />
      </div>
    
    </div>
  )
}
//Fake Json with 7 Questions
//Create -> Form -> Enter question -> Create leetcode Qs on MUI with the 
//associated Difficulty level


export default Leetcode