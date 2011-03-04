#!/bin/sh
# guestbook.cgi
# Данный сценарий реализует простую гостевую книгу.
# Информация о посетителях хранится в базе.
# Для обновления базы используется сценарий newguest.cgi.
# \
exec tclsh "$0" ${1+"$@"}

# База данных содержится в файле guestbook.data.
# Этот файл находится в том же каталоге, что и сценарий.

set dir [file dirname [info script]]
set datafile [file join $dir guestbook.data]

# Загрузка Tcl-процедур поддержки

source [file join $dir cgihacks.tcl]

Cgi_Header "Ivan's Guestbook"

if {![file exists $datafile]} {
  puts "
    <h3>No registered guests, yet.</h3>
    <p>
      Be the first
      <a href='newguest.html'>registered guest!</a>
    </p>"
} else {
    puts "<h3>The following folks have registered in my GuestBook.</h3>
      <p>
        <a href='newguest.html'>Register</a>
        <h2>Guests</h2>"
    catch {source $datafile}
    foreach name [lsort [array names Guestbook]] {
      set item $Guestbook($name)
      set homepage [lindex $item 0]
      set markup [lindex $item 1]
      puts "<h3><a href=$homepage>$name</a></h3>"
      puts $markup
    }
}
puts "  </body>
</html>"
