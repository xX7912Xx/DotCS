package offline

import (
	"crypto/md5"
	"github.com/google/uuid"
)

// NameToUUID return the UUID from player name in offline mode
func NameToUUID(name string) uuid.UUID {
	var version = 3
	h := md5.New()
	h.Write([]byte("OfflinePlayer:"))
	h.Write([]byte(name))
	s := h.Sum(nil)
	var id uuid.UUID
	copy(id[:], s)
	id[6] = (id[6] & 0x0f) | uint8((version&0xf)<<4)
	id[8] = (id[8] & 0x3f) | 0x80 // RFC 4122 variant
	return id
}
