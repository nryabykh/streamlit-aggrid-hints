from dataclasses import dataclass


@dataclass
class Badge:
    alt: str
    img_link: str
    link: str

    @property
    def url(self):
        return f'[![{self.alt}]({self.img_link})]({self.link})'


_github = Badge(
    alt='GitHub',
    img_link='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white',
    link='https://github.com/nryabykh/streamlit-aggrid-hints'
)

_linkedin = Badge(
    alt='LinkedIn',
    img_link='https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white',
    link='https://www.linkedin.com/in/nriabykh/'
)

badges = {
    'github': _github,
    'linkedin': _linkedin,
}
