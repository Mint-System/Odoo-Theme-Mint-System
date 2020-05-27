# TODO

## Review

- [ ] Optimize website: https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Fwww.mint-system.ch%2F&hl=en_GB
    - [ ] lazy loading images -> https://apps.odoo.com/apps/modules/12.0/website_lazy_load_image/ does not work; thought about adding loading="lazy" to all img tags. Not so easy -> layout_column may hold the key
    - [x] enable gzip and compression -> find best practice
    - [x] remove css -> maybee common.css -> removed theme_Common
    - [ ] add alternative font -> fix fontawesome include

## Design

- [ ] Review new adobe designs from Jeanette
- [ ] set letter spacing
- [ ] Add new font .lead or subtitle
- [ ] Move footer logo inwards
- [ ] Readmore links on same level
- [ ] Add sans-serif alternative font

## Content

- [ ] Create odoo styled screenshots
- [ ] Create offer subsites for management and software-engineering

## Functional

- [ ] Scroll link with arrows
- [ ] Override menubar styles f.g. h1 is 62px by default

## Bugs

- [ ] Remove active frame for button
- [ ] Delete logo on edit footer required
- [ ] header nav bottom border rounded https://stackoverflow.com/questions/34211941/curved-end-of-border-bottom-in-css -> add svg?
- [ ] Inserting text_form triggers params form 4x times

# BACKLOG

- [ ] Remove .lead
- [ ] Logo im Footer entfernen?
- [ ] Footer elements must be on the same line
- [ ] Rotate people list -> we do not have a hierarchy
- [ ] Buy the font
- [ ] Remove google map link

# DONE

- [x] Fix padding top on blog
- [x] Create custom menu toolbar with transaprent background. Logo switch from monochrome to normal
- [x] add 80% transparency to menu bar
- [x] Style blog
- [x] Fix lineheight for ul > li > p -> override
- [-] Background urls are not relative
- [x] Underline blog breadcrumb links
- [x] style the blog https://www.mint-system.ch/blog
- [x] Add icons to odoo page -> copy from odoo brand assets https://www.odoo.com/de_DE/page/brand-assets
- [x] Feature grid boxes min-height
- [x] Remove theme common
- [x] Button outlined hover margin is wack
- [x] Copyright is too big
- [x] Galaxy S8/9 cuts off cover title. Make font width dynamic
- [x] Line height removes bottom border https://www.mint-system.ch/odoo
- [-] margin bottom navbar
- [x] Discuss rem font sizes and dynamic resizing with Blatthirsch
- [x] fix outlined button opacity on dark background
- [x] Add animations to readmore links
- [x] Adjust breakpoints for offer
    Icons smaller, text mobile and ipad smaller
- [x] Remove icons from footer
- [x] Menu toolbar should show up earlier #prio1 -> disable fixed header and build myself?
- [x] lead inserted in text_block -> can be deleted
- [-] JavaScript to set onepage anchor as active menu
- [x] Resize feature icons
- [x] change burger menu color
- [x] Dynamic resize font
- [x] Make design more mobile friendly -> convert from px to rem;
- [x] Update contact page: form field, submit text and Google Maps
- [x] Init blog
- [x] Update contact form mail address
- [x] Fix list items default size
- [x] Set logo and favicon
- [x] setup logo
- [x] Increase bottom and top margin for text_form heading
- [x] Style Kontaktformular
- [-] Try to define a overflow background for Unser Angebot
- [x] Set background images
- [x] Override img.shadow with default shadow
- [x] Animate links from dot to full button
- [-] Create draft for contact form
- [-] Mobile nav should fill the page with semi transparent background
- [x] Button hover effect
- [x] Link hover effect
- [x] use css variables
- [x] Update typography
- [x] nav border bottom 3px
- [x] Hover effects for all link
- [x] Style inverted links
- [x] Add style option to s_image_text and s_text_image for inverted
- [x] Remove link text-decoration from footer
- [x] Enable google analytics
- [x] Register unsplash
- [x] Background vanishes on mobile browsers -> Url pointed to localhost
- [x] Remove odoo promotion
- [x] Remove button border
- [x] Remove border from burger menu
- [x] Style text_image
- [x] Button font type bold
- [x] Decrease footer max-width 996px with media quey
- [x] Unlisted typography page http://localhost:8069/typography
- [x] Insert two column layout for offer sites
- [x] Install theme_common snippets
- [x] Apply border bottom to menu span tag instead a
- [x] Icrease gab between menu items
- [x] Footer insert block is removed after update -> https://stackoverflow.com/questions/43081580/odoo-template-page-doesnt-update-when-xml-changes/43650510 -> template is overriden by default. However Odoo makes a copy for the footer. By inserting an tag into the footer we can insert content that is persisted
- [-] Create custom cover snippet without background image.
- [x] Add block insert space above footer
- [x] Create a block that inserts a contact form
