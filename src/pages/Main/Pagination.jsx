import React from "react"
const Pagination = ({totalPosts,itemperpage,setcurrentPage,currentPage}) =>{
    let pages = [];
    for (let i=1;i<=Math.ceil(totalPosts/itemperpage);i++){
        pages.push(i)
    }
    return(
        <div className="pagi">
            {pages.map((page,index)=>{
                return <button className={page==currentPage ? 'active': ''} onClick={() => setcurrentPage(page)} key={index}>{page}</button>
            })}
        </div>
    )
}
export default Pagination;