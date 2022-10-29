import React from "react";
import "../styles/left.css";
import { ImHeadphones } from "react-icons/im";
import { FaEllipsisH } from "react-icons/fa";
import { BiSearchAlt } from "react-icons/bi";

function Leftmenu() {
  return <div className="left">
     <div className="logocontainer">
     <i>
      <ImHeadphones />
     </i>
     <h2>Musixon</h2>
     <i>
      <FaEllipsisH />
     </i>
     </div>
     <div className="searchbox">
        <input type="text" placeholder="Search" />
        <i>
            <BiSearchAlt />
        </i>
     </div>
    </div>;
}

export { Leftmenu };