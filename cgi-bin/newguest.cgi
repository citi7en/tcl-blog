#!/bin/sh
# \
exec tclsh "$0" ${1+"$@"}

# Для обработки данных формы используется пакет ncgi из tcllib

package require ncgi
ncgi::parse

# Загрузка файла данных и процедур поддержки

set dir [file dirname [info script]]
set datafile [file join $dir guestbook.data]
source [file join $dir cgihacks.tcl]

# Открытие базы данных в режиме, допускающем включение информации

if {[catch {open $datafile a} out]} {
  Cgi_Header "Guestbook Registration Error" \
    {bgcolor=black text=red}
  puts "<p>Cannot open the data file</p>"
  puts $out;# the error message
  exit 0;
}

# Добавление Tcl-команды set, определяющей запись для посетителя

puts $out ""
puts $out [list set Guestbook([ncgi::value name]) \
  [list [ncgi::value url] [ncgi::value html]]]
close $out

# Формирование Web-страницы для передачи браузеру

Cgi_Header "Guestbook Registration Confirmed" \
  {bgcolor=white text=black}

puts "
<table border=1>
  <tr>
    <td>
      Name
    </td>
    <td>
      [ncgi::value name]
    </td>
  </tr>
  <tr>
    <td>
      Url
    </td>
    <td>
      <a href='[ncgi::value url]'>[ncgi::value url]</a>
    </td>
  </tr>
  <tr>
    <td>
      Extra
    </td>
    <td>
      [ncgi::value html]
    </td>
  </tr>
</table>
"
