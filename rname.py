import random
import re
class Mocker(object):
    def __init__(self) -> None:
        with open("c:\\temp\\firstname.txt", "r") as file:
            self.firstnames = list(map(lambda x: x.strip(), file.readlines()))
        with open("c:\\temp\\lastname.txt", "r") as file:
            self.lastnames = list(map(lambda x: x.strip(), file.readlines()))
        self.domains = ["abc.com", "def.org", "ghi.edu", "jkl.io", "mno.me", "pqr.tv", "stu.us", "vw.xyz"]
        text = """Download the CLI tool from the official site and extract the zip file
        The bin folder present in the Spring setup is used to execute the Spring Boot application
        Since Spring Boot CLI executes groovy files you need to create a groovy file for Spring Boot application 
        So to do that open terminal and change the current directory to the bin folder Now, open a groovy file
        In this file create a controller as follows api 404 file not found 500 Interal Error RestController"""
        self.tokens = re.split("\\s", text)
        self.separators = list(";,\n")
    def noise(self):
        res = []
        for i in range(random.randint(1, 5)):
            x = random.choice(self.tokens)
            res.append(x)
        return " ".join(res)
    def makename(self):
        first = random.choice(self.firstnames)
        last = random.choice(self.lastnames)
        domain = random.choice(self.domains)
        user = ("%s.%s" % (last, first)).lower()
        return "\"%s %s\"<%s@%s>" % (first, last, user, domain)
    def makeline(self):
        names = [self.makename() for _ in range(10)] + [self.noise() for _ in range(2)]
        weights = [3 for _ in range(10)] + [1 for _ in range(2)]
        items = random.choices(names, weights=weights, k=5)
        s = random.choice(self.separators)
        return s.join(items) + "\n"
    def build(self, path, size=1000):
        with open(path, "w") as file:
            for _ in range(size):
                line = self.makeline()
                file.write(line)
m = Mocker()
for i in range(5):
    path = "c:\\temp\\csv%d.txt" % i
    m.build(path)
    print(path, "is ready")