import React from "react";
import {Link} from "react-router-dom";

const NotFound = () => {
    return (
        <div className="not_found_text">
            <p>К сожалению, запрашиваемая Вами страница не найдена..</p>
            <p>Почему?</p>
            <ol>
                <li className="not_found_list">Ссылка, по которой Вы пришли, неверна.</li>
                <li className="not_found_list">Вы неправильно указали путь или название страницы.</li>
                <li className="not_found_list">Страница была удалёна со времени Вашего последнего посещения.</li>
            </ol>
        </div>
    );
};

export default NotFound;