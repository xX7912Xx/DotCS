// +build !fyne_gui

package I18n

import (
	"fmt"
	"io/ioutil"
	"os"
)

func Init() {
	config:=loadConfigPath()
	if _, err:=os.Stat(config); os.IsNotExist(err) {
		SelectLanguage()
	}else{
		content, err:=ioutil.ReadFile(config)
		if (err != nil) {
			fmt.Printf("WARNING: Language config file isn't accessible\n")
			I18nDict=LangDict["en_US"]
			return
		}
		langCode:=string(content)
		SelectedLanguage=langCode
	}
	langdict, aru := LangDict[SelectedLanguage]
	if(!aru) {
		fmt.Printf("Ordered language doesn't exist.\nPlease reselect one:\n")
		SelectLanguage()
		langdict, aru=LangDict[SelectedLanguage]
		if !aru {
			panic("Language still unexists after reselection")
			return
		}
	}
	I18nDict=langdict
}