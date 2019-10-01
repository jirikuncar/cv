"""Personal page."""

Person = Organization = Occupation = object
OwnershipInfo = EducationalOrganization = object


class JiriKuncar(Person):
    """Code alchemist, Python enthusiast, database expert
    and visionary architect who sets high standards. I know
    many cool buzz words but I try to use them carefully.
    I like to help people around and I am not afraid to ask
    for help.
    """

    name = "Jiří Kunčar"

    knowsLanguage = ["cs_CZ", "en_US", "es_ES", "fr_FR"]

    class StubHub(Organization):

        name = "StubHub (the eBay Company)"

        class SoftwareEngineer(Occupation):
            """Developing data information pipeline."""

            address = "Bilbao, Spain"

            skills = ["Python", "SQL", "Docker", "Concourse"]

    class SwissDataScienceCenter(Organization):
        """The Center’s mission is to accelerate the use of data science
        and machine learning techniques within academic disciplines
        of the ETH Domain, the Swiss academic community at large,
        and the industrial sector.
        """

        class SeniorSoftwareEngineer(Occupation):
            """Contributing to the design and development of the center’s
            Insights-as-a-Service platform, a hosted one-stop-shop for accessing,
            exchanging and exploring possibly anonymized data at scale,
            and for building and deploying data science workflows.
            """

            address = "Zurich, Switzerland"

            skills = [
                "Python",
                "Jupyter",
                "GitLab",
                "Kubernetes",
                "Helm",
                "Docker",
                "System Design",
                "DevOps",
            ]

    class CERN(Organization):
        class SoftwareEngineer(Occupation):
            """Design and development of 70+ modules for Invenio digital library
            framework that handles scientific publications, multimedia material,
            or research data.

            Reviewing and integrating code contributed by project partners.
            Providing support to collaborating institutions (DESY, EPFS, SLAC).
            Participating on DevOps for CERN Open Data Portal, and Zenodo.org services.
            Planning project strategy and strengthening community relations.
            Leading dynamic team of developers.
            """

            address = "Geneva, Switzerland"

            skills = [
                "Python",
                "Flask",
                "JavaScript",
                "AngularJS",
                "HTML5",
                "CSS3",
                "GitHub",
                "ElasticSearch",
                "PostgreSQL",
            ]

    class OpenAgency(Organization, OwnershipInfo):

        name = "Open Agency s.r.o."

        ownedFrom = "2008-01-01"

        class SoftwareArchitect(Occupation):
            """Design and development of web application for specialized
            language courses and leading a team of people running
            and constantly improving our service.
            """

            skills = ["PHP", "CakePHP", "MySQL", "AWS", "S3", "Git"]

    class MalardalenUniversity(EducationalOrganization):
        class Master:
            pass

    class CharlesUniverity(EducationalOrganization):
        class Master:
            pass

        class Bachelor:
            pass

        class Assistent(Occupation):
            pass
