import './Header.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faEnvelope, faLock, faUser} from '@fortawesome/free-solid-svg-icons';
import logo from "../../assets/images/logoMini.png";
export default function Header() {
    return(
        <nav className="navbar">
                <div className="navbar-header">
                    <img className="images" src={logo} alt="Logo" />
                </div>
                <div className='User'>
                    <div className='containUser'>
                        <FontAwesomeIcon icon={faUser} className="icon"/>
                    </div> 
                    <p>Usuário</p>
                </div>
        </nav>
    )
}