class Father:
    def __init__(self, choose_dir):
        print(choose_dir)
        self.choose_dir = choose_dir


if __name__ == '__main__':
    import re
    ss = re.split(r'([()+*/])|((?<=\d)-)', '(-12+(4+5+2)-3)+(-6+8)')
    s = [s for s in ss if s]
    print(s)
