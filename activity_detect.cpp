#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <sstream>

using namespace std;


map<string, vector<int>* > authors_papers;

vector<string> split(const string& s, char delimiter) {
	vector<string> tokens;
	string token;
	istringstream tokenStream(s);
	while (getline(tokenStream, token, delimiter)) {
		tokens.push_back(token);
	}
	return tokens;
}

double calc_activity(vector<int> *hist) {
	double tot = 0;
	for (int i = 0; i < 11; i++)
		tot += (*hist)[i];
	double recent = 0;
	recent += (*hist)[10] + (*hist)[9] + (*hist)[8];
	return recent / tot;
}

int main() {
	FILE *input = fopen("data/papers.csv", "r");
	char *buffer = new char[10010];
	fgets(buffer, 1000, input);
	string last_conf = "null";
	FILE *output = NULL;
	int line_cnt = 0;
	while (fgets(buffer, 10000, input) != NULL) {
		string str = buffer;
		line_cnt ++;
		//printf("line_cnt=%d\n", line_cnt);
		vector<string> tokens = split(str, ',');
		if (tokens.size() != 4) {
			printf("Error!\n");
			for (int i = 0; i < tokens.size(); i++)
				printf("item[%d]=%s\n", i, tokens[i].c_str());
			exit(0);
		}
		vector<string> authors = split(tokens[0], '_');
		string conf = tokens[3];
		if (conf != last_conf) {
			if (last_conf != "null") {	
				fprintf(output, "author,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,total,ratio\n");
				map<string, vector<int>* >::iterator iter = authors_papers.begin();
				for (; iter != authors_papers.end(); iter++) {
					string author = iter->first;
					vector<int>* hist = iter->second;
					fprintf(output, "%s", author.c_str());
					int tot = 0;
					for (int i = 0; i < 11; i++) {
						fprintf(output, ",%d", (*hist)[i]);
						tot += (*hist)[i];
					}
					fprintf(output, ",%d,%.3lf\n", tot, calc_activity(hist));
				} 
				fclose(output);
			}
			char filename[100];
			sprintf(filename, "data/activity_%s.csv", conf.c_str());
			output = fopen(filename, "w");
			last_conf = conf;
		}
		if (tokens[2] == "") continue;
		printf("stoi: %s\n", tokens[2].c_str());
		int year = stoi(tokens[2]);
		for (int i = 0; i < authors.size(); i++) {
			string author = authors[i];
			if (authors_papers.find(author) == authors_papers.end()) {
				authors_papers.insert(pair<string, vector<int>* >(author, new vector<int>(11)));
			}
			vector<int> *hist = authors_papers[author];
			(*hist)[year - 2007] ++;
		}
	}
	return 0;
}