import React from "react";
import "./Pagination.css";

const Pagination = ({totalPosts,itemperpage,setcurrentPage,currentPage}) =>{
    let pages = [];
    for (let i=1;i<=Math.ceil(totalPosts/itemperpage);i++){
        pages.push(i)
    }
    return(
        <div className="pagi">
            <button className='navbtn' onClick={()=> {setcurrentPage(pages[0])}} >First</button>
            <button className="navbtn" onClick={()=> {setcurrentPage(currentPage===1?currentPage:currentPage-1)}} >Prev</button>
            {pages.map((page,index)=>{
                return <button className={page==currentPage ? 'active': ''} onClick={() => setcurrentPage(page)} key={index}>{page}</button>
            })}
            <button className="navbtn" onClick={()=> {setcurrentPage(currentPage===pages.length?currentPage:currentPage+1)}} >Next</button>
            <button className="navbtn" onClick={()=> { setcurrentPage(pages.length)}}  >Last</button>
        </div>
    )
}
export default Pagination;