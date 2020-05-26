function scrolled () {
    scrollpos = window.scrollY

    if (scrollpos >= 1) {
        document.documentElement.classList.add('scrolled')
    } else {
        document.documentElement.classList.remove('scrolled')
    }
}

window.addEventListener('scroll', function () {
    scrolled()
})

scrolled()