import React from 'react'
import axios from 'axios'
export default function ImageSearch() {
  const [datasets, setDatasets] = React.useState([]);
  const [toggle, setToggle] = React.useState(false);
  const [image, setImage] = React.useState();
  const [uploadProgress, setUploadProgress] = React.useState();
  const [loadedImage, setLoadedImage] = React.useState();
  const [searchLoading, setSearchLoading] = React.useState(false);
  const [result, setResult] = React.useState();
  const inputRef = React.useRef();

  async function uploadDataset() {
    if(!datasets.length) alert('Pilih gambar dulu')

    for (let i = 0; i < datasets.length; i++) {
      const fileContent = await new Promise((resolve) => {
        const fileReader = new FileReader()
        fileReader.readAsBinaryString(datasets[i])
        fileReader.onload = () => {
          resolve(fileReader.result)
        }
      })
      await axios.post('/api/upload', {
        name: datasets[i].name,
        content: window.btoa(fileContent)
      })
      setUploadProgress(Math.round((i/datasets.length) * 100))
    }
    setUploadProgress(100)
  }

  React.useEffect(() => {
    const fileReader = new FileReader()
    if(image) {
      fileReader.readAsDataURL(image)
      fileReader.onload = () => {
        setLoadedImage(fileReader.result)
        console.log(fileReader.result)
      }
    }
  }, [image]);

  async function searchImage() {
    if(!image) {
      alert('Pilih file dulu')
      return
    }
    const fileContent = await new Promise((resolve) => {
      const fileReader = new FileReader()
      fileReader.readAsBinaryString(image)
      fileReader.onload = () => {
        resolve(fileReader.result)
      }
    })
    setSearchLoading(true)
    let result
    if (!toggle){
      result = await axios.post('/api/search_texture', {
        image: window.btoa(fileContent)
      })
    }
    else{
      result = await axios.post('/api/search_color', {
        path_image: window.btoa(fileContent)
      })
    }
    setSearchLoading(false)
    // const result = {data: {
    //   "files": [
    //     {
    //       "filename": "perforated_0001.jpg",
    //       "similarity": 1
    //     },
    //     {
    //       "filename": "perforated_0013.jpg",
    //       "similarity": 0.9999999914058237
    //     },
    //     {
    //       "filename": "perforated_0003.jpg",
    //       "similarity": 0.9999995431729115
    //     },
    //     {
    //       "filename": "perforated_0004.jpg",
    //       "similarity": 0.9999964466001358
    //     },
    //     {
    //       "filename": "perforated_0012.jpg",
    //       "similarity": 0.9999957387518099
    //     }
    //   ],
    //   "time": 3.011603593826294
    // }}
    setResult(result.data)
  }



  return <div className="main">
    <div className="dataset" id="home">
      <div className="header_dataset">
        <h2>Upload Dataset</h2>
      </div>
      <div className="select_dataset">
        <input type="file" id="select_dataset" directory="" webkitdirectory="" onChange={(e) => {
          console.log(e.target.files)
          setDatasets(e.target.files)
        }} />
        <label htmlFor="select_dataset"><i className="fa-solid fa-upload"></i> Select Dataset File</label>
        <br/>
      </div>
      <div>{datasets?.length} file selected</div>
      <div>Uploading: {uploadProgress}%</div>
      <div className="upload_dataset">
        <input type="button" name="upload_dataset" value="Upload" onClick={() => {
          uploadDataset().then(() => setDatasets([]))
        }}/>
      </div>
    </div>

    <div className="container">
      <h2>Upload Image</h2>
      <div className="wrapper">
        <div className="image">
          <img src={loadedImage} alt="" />
        </div>

        <div className="content">
          <div className="icon">
            <i className="fas fa-upload"></i>
          </div>

          <div className="text">
            No File Chosen
          </div>
        </div>

        <div id="cancel-btn">
          <i className="fas fa-times"></i>
        </div>

        <div className="file-name">
          File Name
        </div>
      </div>
      <input id="default-btn" type="file" hidden accept="image/*" ref={inputRef} onChange={(e) => {
        setImage(e.target.files[0])
      }}/>
      <button onClick={() => inputRef.current.click()} id="custom-btn">Choose a file</button>
    </div>

    {/* {toggle&&"true"} */}
    <div className="search">
      <div className="type_search">
        <input type="checkbox" checked = {toggle} className="toggle" id="rounded" onChange={(e) => {
          setToggle(e.target.checked)
          // console.log(e.target.files)
          // setDatasets(e.target.files)
        }} />
        <label for="rounded" colors="Colors" className="rounded" textures="Textures" ></label>
        <br/>
      </div>

      <div className="select_search">
        <input type="button" name="search" value="Search" onClick={searchImage}/>
      </div>

    </div>
    <div>
      <div className="result">
        <div className="header_result">
          <h2>Result:</h2>
        </div>
      </div>
      <div>
        {searchLoading && 'Searching...'}
        {result &&
          <div>Found {result.files.length} results in {result.time.toFixed(3)}</div>
        }
      </div>
      <div style={{display: 'flex'}}>
      {result && result.files.map(file => { //menampilkan gmbr
        return <div key={file.filename}>
          <img src={"http://localhost:5000/image?name="+file.filename} width={'100'} />
          <div>{(file.similarity*100).toFixed(4)}</div>
        </div>
      })}
      </div>
    </div>

    <div className="pagination">
      <div className="page">
        <a href="#">&laquo;</a>
        <a href="#">1</a>
        <a className="active" href="#">2</a>
        <a href="#">3</a>
        <a href="#">4</a>
        <a href="#">5</a>
        <a href="#">6</a>
        <a href="#">7</a>
        <a href="#">8</a>
        <a href="#">9</a>
        <a href="#">&raquo;</a>
      </div>
    </div>
  </div>
}