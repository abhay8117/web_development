let counter=0;
// Check local storage and if data present load it
keys=Object.keys(localStorage).sort((a,b)=>{
    return a-b;
});
// If data present in the local storage then pick the last element and put
// it in the counter
if(keys.length>0){
    counter=keys.slice(-1);
};

// Check whether todo is added in the list
const check_todo=()=>{
    const ls_values=Object.values(localStorage);
    const ls_values_upper=ls_values.map(value=>value.toUpperCase());
    const input_value=document.querySelector('#text').value.toUpperCase().trim();
    const idx=ls_values_upper.indexOf(input_value);
    console.log(`Index:${idx},Value:${ls_values[idx]}`);
    return idx;
};

const update_ul=(key,input_value)=>{
    const ul=document.querySelector('.list-group');
    const li=document.createElement('li');
    li.className="list-group-item col-sm-6 mb-2 bg-dark text-white";
    li.setAttribute('draggable','true');
    li.setAttribute('todo_id',key);
    console.log(`Value of counter=${counter}`);
    const btn=document.createElement('button');
    btn.className="btn btn-danger btn-sm float-right delete-todo";
    btn.appendChild(document.createTextNode('X'));
    li.appendChild(document.createTextNode(input_value));
    li.appendChild(btn);
    ul.appendChild(li);
};


if(keys.length>0){
  document.querySelector('#submit_form').style.display='contents';
  keys.map(key=>{
    const input_value=localStorage.getItem(key);
    update_ul(key,input_value);
  })
};

const add_items=()=>{
    const input_data=document.querySelector('#text');
    const input_value=input_data.value;
    if(input_value.length>0){
        const idx=check_todo();
        if(idx<0){
            update_ul(counter,input_value);
            document.querySelector('#submit_form').style.display='contents';
            input_data.value='';
            localStorage.setItem(counter,input_value);
            counter++;
        }
        else{
            alert('Todo already in the list');
        }
    }
};

const delete_items=()=>{
    if(event.target.classList.contains('delete-todo')){
        const ul=document.querySelector('.list-group');
        const li=event.target.parentElement;
        const ls_key=li.getAttribute('todo_id');
        localStorage.removeItem(ls_key);
        ul.removeChild(li);               
        const child_length=ul.children.length;
        if(child_length<=0){
            document.querySelector('#submit_form').style.display='none';
            counter=0;
        }
}
};

document.querySelector('#text').addEventListener('keyup',(event)=>{
  const sub=document.querySelector('#submit');
  sub.disabled=false;
  if(event.keyCode===13){
    add_items();
    sub.disabled=true;
  }
});
document.querySelector('#submit').addEventListener('click',add_items);

// Get all todos list
document.querySelector('.list-group')
.addEventListener('click',delete_items);