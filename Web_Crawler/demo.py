import os
 
def create_project_dir(directory):                         # making our own directory
    if not os.path.exists(directory):                      # check if the directory doesnt already exist
        print('Creating the directory' + directory)
        os.makedirs(directory)                             # creating the directory
 
def create_data_files(project_name, base_url):             # creating queue.txt and crawl.txt files   base_url-first url which crawler would start crawling
    queue = os.path.join(project_name,'queue.txt')         
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue):                          # check if queue file exists or not
        write_file(queue,base_url)                         # function to write base url in queue file
    if not os.path.isfile(crawled):
        write_file(crawled,'')
 
def write_file(path,data):                                 # function to write in the file
    with open(path,'w') as f:                              
        f.write(data)
 
def append_to_file(path,data):                             # to write data into the file , it wont delete the previous content put append the new data into the file
    with open(path,'a') as f:                              
        f.write(data,'\n')
 
def delete_file_contents(path):                            # deletes the contents of a particular file 
    open(path,'w').close()
 
def file_to_set(file_name):                                #Storing elements into the set so they are accessible easily and in a time efficient manner
    results= set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results
 
def set_to_file(links,file_name):                          # storing the set elements back into the the file
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")
