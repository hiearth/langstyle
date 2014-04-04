
format_file = r"E:\Projects\langstyle\population\english\dictionary\basic_format.txt"
source_file = r"E:\Projects\langstyle\population\english\dictionary\basic.txt"

def remove_yinbiao(line):
    if line:
        line = line.strip()
        l_index = line.find("[")
        if l_index>-1:
            r_index = line.find("]", l_index)
            if r_index>-1:
                line = line[0:l_index] + line[r_index+1:]
    return line

def _format_line(line):
    parts = line.split()
    if parts:
        parts[0] = parts[0] + "".join((25-len(parts[0]))*([" "]))
        line = "".join(parts)
    return line

def format():
    with open(source_file, "r", encoding="utf-8") as fs, open(format_file, "a", encoding="utf-8") as fd:
        while True:
            line = fs.readline()
            if not line:
                break
            line = remove_yinbiao(line)
            line = _format_line(line)
            fd.write(line+"\r\n")

if __name__ == "__main__":
    format()
