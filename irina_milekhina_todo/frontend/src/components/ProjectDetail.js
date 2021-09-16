import React from "react";
import { useParams } from 'react-router-dom'
import UsersList from "./Users";

const ProjectDetailItem = ({projects}) => {
    let {id} = useParams();
    let projectItem = projects.find((item) => item.id === +id)
    return (
        <div>
            <h1>{projectItem.name}</h1>
            <h3>Репозиторий:</h3>
            <p>
                {(projectItem.repoLink === '') ? 'Ссылка не указана':
                    <a href={projectItem.repoLink} className="link" target="_blank">{projectItem.repoLink}</a>}
            </p>
            <h3>Участники:</h3>
            <UsersList users={projectItem.users}/>
        </div>
    );
}


export default ProjectDetailItem;