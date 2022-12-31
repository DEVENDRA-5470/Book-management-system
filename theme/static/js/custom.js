window.addEventListener('DOMContentLoaded',()=>{
    const menu_btn=document.getElementById('menu-btn')
    const dropdown=document.getElementById('dropdown')
    menu_btn.addEventListener('click',()=>{
        dropdown.classList.toggle('flex')
        dropdown.classList.toggle('hidden')
    })
})
