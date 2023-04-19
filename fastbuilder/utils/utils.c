#include <stdlib.h>

int compareVersion(char *latestVersion,char *currentVersion) {
	char *latestVersionParts[3];
	int vpi=1;
	latestVersionParts[0]=latestVersion;
	for(char *p=latestVersion;*p!=0;p++) {
		if(*p<'0'||*p>'9') {
			if(vpi>=3)break;
			*p=0;
			latestVersionParts[vpi]=p+1;
			vpi++;
		}
	}
	int lvMajor=atoi(latestVersionParts[0]);
	int lvMinor=atoi(latestVersionParts[1]);
	int lvPatch=atoi(latestVersionParts[2]);
	char *currentVersionParts[3];
	vpi=1;
	currentVersionParts[0]=currentVersion;
	for(char *p=currentVersion;*p!=0;p++) {
		if(*p<'0'||*p>'9') {
			if(vpi>=3)break;
			*p=0;
			currentVersionParts[vpi]=p+1;
			vpi++;
		}
	}
	int cMajor=atoi(currentVersionParts[0]);
	int cMinor=atoi(currentVersionParts[1]);
	int cPatch=atoi(currentVersionParts[2]);
	free(latestVersion);
	free(currentVersion);
	if(cMajor<lvMajor) {
		return 1;
	}else if(cMinor<lvMinor) {
		return 1;
	}else if(cPatch<lvPatch) {
		return 1;
	}
	return 0;
}
