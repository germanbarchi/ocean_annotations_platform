function showChoices(dim) {
    document.getElementById(dim).hidden = !document.getElementById(dim).hidden;
}

const selects = document.querySelectorAll('[name$=hidden]');
for (let i = 0; i < selects.length; i++) {
    const id = selects[i].id.replace('_hidden', '').replace('id_', '');
    if (selects[i].checked) {
        document.getElementById(id).hidden = false;
    }else{
        document.getElementById(id).hidden = true;
    }
}

status = status.split(',')
let selectList = document.getElementById("moreAudios");

for (let i = 1; i < status.length + 1; i++) {
    let a = document.createElement("a");
    a.href = '/annotations/ann/form/' + i.toString();
    a.className = "dropdown-item"
    a.text = 'Audio ' + i.toString();
    a.style.fontSize = 'larger';
    a.style.color = 'white'
    if (status[i - 1] === 'False') {
        a.style.backgroundColor = "#606D80";
    } else {
        a.style.backgroundColor = "#567EBB";
    }
    selectList.appendChild(a);
}

if (status.every((s) => s === 'True')) {
    document.getElementById('end_block').hidden = false;
}


