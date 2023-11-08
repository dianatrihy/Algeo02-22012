import classes from './Main.module.css'
// import uploadimage from './hook/uploadimage'


export default function Main() {
    return(
        <div className={classes.all}>
            {/* navigation bar */}
            <nav className={classes.navbar}>
                <a href="#main" className={classes.logo}>Allens
                    <p>Reverse Image Search</p>
                </a>

                <div className={classes.option}>
                    <a href="#home">Home</a>
                    <a href="#how">How to Use</a>
                    <a href="#concepts">Basic Concepts</a>
                    <a href="#about">About Us</a>
                </div>
            </nav>

            {/* menu utama */}
            <section className={classes.main} id='home'>
                <main className={classes.content}>
                    <div className={classes.dataset}>
                        <h3>Upload Dataset</h3>
                        <button>Insert Dataset</button>
                        <p>nama_folder</p>
                    </div>

                    <div className={classes.image}>
                        <div className={classes.inputimage}>
                            <h3>Image Input</h3>
                            <input type="file"/>
                            <p>nama_file.jpg</p>
                        </div>
                        <div className={classes.previewimage}>
                            <p>preview image</p>
                        </div>
                    </div>

                    <div className={classes.optionsearch}>
                        <p>Color</p>
                        <label class="switch">
                            <input type="checkbox" name="" id="" />
                            <span class="slider round"></span>
                        </label>
                        <p>Texture</p>
                    </div>
                </main>

            </section>
        </div>

        



    )
}