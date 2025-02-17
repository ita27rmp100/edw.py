# edw.py
<strong>edw.py</strong> is a python project based on os library and some minds in order to make -almost- a terminal with understandable command names.

<strong>Created on January 2021 (4 years ago).</strong>
<strong>Latest  update on February 2025.</strong>

<h2>What's new ?</h2>
<ul>
    <li>Code more cleaner, by orgnize the structure of edw.py.</li>
    <li>Some changes on the old commands.</li>
    <li>Add new commands <b>I note it in the code</b>.</li>
    <li>Connected with a database <q>- using sqlite3 library -</q> to store the history of using.</li>
</ul>

<q>I hope you like this mini project, and I'm so excited to see your pull requests on it! &#128516;&#128293;</q><br>
<b>Notes :</b> 
<ul>
    <li>Some commands are available only for windows and Linux, it may not work in iOS (See the comments included in code).</li>
    <li>When you want to execute command you have to write it with this format : <command>$<more_party> like 'write$ hello world' .</li>
    <li>As same as we fined in linux, some commands display nothing when you execute it, thus when you want to redirect the result to a file (overwritting), the file will be empty.</li>
    <li>For <b>reboot$</b> and <b>chrome$</b> commands, they work only in windows.</li>
    <li>If there is any errors or suggestion, please tell me about that in reviews.</li>
</ul>
<h2>Documentation :</h2>
<table>
  <thead>
    <tr>
      <th>The command</th>
      <th>Its purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>write</td>
      <td>print a text in console</td>
    </tr>
    <tr>
      <td>open</td>
      <td>open a script or program</td>
    </tr>
    <tr>
      <td>where</td>
      <td>display the current path</td>
    </tr>
    <tr>
      <td>rename</td>
      <td>rename a file or directory</td>
    </tr>
    <tr>
      <td>rfo</td>
      <td>remove empty folder</td>
    </tr>
    <tr>
      <td>cfo</td>
      <td>create new folder</td>
    </tr>
    <tr>
      <td>rfi</td>
      <td>remove a file</td>
    </tr>
    <tr>
      <td>quit</td>
      <td>exit the console</td>
    </tr>
    <tr>
      <td>reboot</td>
      <td>shut down the device</td>
    </tr>
    <tr>
      <td>dir</td>
      <td>display the content list of a directory</td>
    </tr>
    <tr>
      <td>time</td>
      <td>display the current time (with details)</td>
    </tr>
    <tr>
      <td>clear</td>
      <td>clear the console</td>
    </tr>
    <tr>
      <td>chrome</td>
      <td>open google chrome browser</td>
    </tr>
    <tr>
      <td>exist</td>
      <td>check if a file or folder exists</td>
    </tr>
    <tr>
      <td>read</td>
      <td>print the content of a file</td>
    </tr>
    <tr>
      <td>calendar</td>
      <td>print the calendar of a specific month</td>
    </tr>
    <tr>
      <td>calc</td>
      <td>do math calculations</td>
    </tr>
    <tr>
      <td>help</td>
      <td>display the list of available commands in this project</td>
    </tr>
    <tr>
      <td>redirect</td>
      <td>save the result of a command in a file</td>
    </tr>
    <tr>
      <td>redirect -ow</td>
      <td>append the result instead of overwriting</td>
    </tr>
    <tr>
      <td>save</td>
      <td>save the history of the current session in a file</td>
    </tr>
    <tr>
      <td>history</td>
      <td>display the history of commands used</td>
    </tr>
    <tr>
      <td>delhis</td>
      <td>delete the history</td>
    </tr>
    <tr>
      <td>chtime</td>
      <td>change the device time</td>
    </tr>
    <tr>
      <td>restart</td>
      <td>restart the device</td>
    </tr>
    <tr>
      <td>sysinfo</td>
      <td>display system information (-r for release, -s for system name, -v for version)</td>
    </tr>
  </tbody>
</table>