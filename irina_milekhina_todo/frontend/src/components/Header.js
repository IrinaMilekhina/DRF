import React from "react";
import {Link} from 'react-router-dom'

const Header = () => {
    return (<div className="header">
            <ul className="header_list">
                <li className="header_text"><Link to='/'>Пользователи</Link></li>
                <li className="header_text"><Link to='/projects/'>Проекты</Link></li>
                <li className="header_text"><Link to='/todos/'>Заметки</Link></li>
            </ul>
        </div>
    );
}

export default Header;
