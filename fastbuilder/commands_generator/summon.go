// +build do_not_add_this_tag__not_implemented

package commands_generator

import (
	"fmt"
	"phoenixbuilder/fastbuilder/types"
)


func SummonRequest(module *types.Module, config *types.MainConfig) string {
	Entity := module.Entity
	Point := module.Point
	Method := config.Method
	if Entity != nil {
		return fmt.Sprintf("summon %s %v %v %v", *Entity, Point.X, Point.Y, Point.Z)
	} else {
		return fmt.Sprintf("summon %s %v %v %v", *Entity, Point.X, Point.Y, Point.Z)
	}
}

