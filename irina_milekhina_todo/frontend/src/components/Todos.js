import React from "react";


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.project.name}</td>
            <td>{todo.text}</td>
            <td>{todo.created}</td>
            <td>{todo.updated}</td>
            <td>{todo.isActive? 'Активна' : 'Закрыта' }</td>
        </tr>
    )
}

const TodoList = ({todos}) => {
    return (
         <table className={'tab'}>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Project</th>
                    <th>Text</th>
                    <th>Created</th>
                    <th>Updates</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {todos.map((todo) => <TodoItem key={todo.id} todo={todo}/>)}
            </tbody>
        </table>
    )
}
export default TodoList;
