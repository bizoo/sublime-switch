# Intro

Switch for Sublime Text 2 was inspired by Andrew Radev's [switch.vim](https://github.com/AndrewRadev/switch.vim).

The main entry point of the plugin is a single command, **Switch**. When the command is executed, the plugin looks for one of a few specific patterns under the cursor and performs a substition depending on the pattern.

# Install

* Clone this git repository into your packages folder
* Restart Sublime Text 2 editor

Or with package control:

* Package Control: Add Repository https://github.com/robbl/Switch
* Package Control: Install Package Switch
* Restart Sublime Text 2 editor

# Usage

If the cursor is on the keyword "true" in the following Ruby example, and the command is executed the "true" will turn into "false"  and the other way around.

```ruby
attribute = true
hash = { key: true }
```

## Key Bindings

* OSX: <super+ctrl+s>
* Linux: <ctrl+alt+s>
* Windows: <ctrl+alt+s>

# Cusomization

The following examples show how to customize the available switches. Switches are grouped together and should be considered as toggle groups. Your **are required** to do so for the full experience of this plugin.

There are two types of toggle groups:

*   Simple toggle groups

    ``` json
    ["true", "false"]
    ```

    The first string comparison that matches a group item will substituted by the following item. (Note: If the end is reached it starts at the beginning.)

*   Advanced toggle groups

    ``` json
    {
      ":(\\w+)\\s=>": "\\1:",
      "(\\w+):":      ":\\1 =>"
    }
    ```

    The first regular expression (the **key**) that matches the current **line** will be substituted by the replacement (the **value**).

Toggle groups are defined in the sublime-settings files as follows:

``` json
{
  "switch_custom_definitions": [
    ["if", "unless"],
    {
      "def (\\w+)\\s(.*)":    "def \\1(\\2)",
      "def (\\w+)\\((.*)\\)": "def \\1 \\2"
    },
  ]
}
```

And its possible to overwrite the builtin switches as follows. Sometimes you need or want to do that, because builtin switches overrule custom switches.

``` json
{
  "switch_builtin_definitions": [
    ["foo", "bar", "baz"],
  ]
}
```

Your also can have a look at your current or the default settings through the Sublime Text 2 Menu under `Preferences / Package Settings / Switch`. As usual User specific settings overrule Switch Package specific settings. The defined switches are prioritized in the following order (Note: Last weighs heaviest.) and grouped syntax specific.

* Packages/Switch/Ruby.sublime-settings
* Packages/User/Ruby.sublime-settings

## Key Bindings

Include the following key binding definition in your sublime-keymap file and customize the keys.

``` json
[
    {
        "keys": ["super+ctrl+s"], "command": "switch"
    }
]

```

# Builtins

Here's a list of all the built-in switch definitions. To see the actual
definitions with their patterns and replacements, look at the corresponding sublime-settings file.

## Ruby

[Ruby.sublime-settings](https://github.com/robbl/Switch/blob/master/Ruby.sublime-settings) and [Ruby on Rails.sublime-settings](https://github.com/robbl/Switch/blob/master/Ruby on Rails.sublime-settings)


* Boolean conditions:
  ``` ruby
  foo && bar
  foo || bar
  ```

* Boolean constants:
  ``` ruby
  flag = true
  flag = false
  ```

* Hash style:
  ``` ruby
  foo = { :one => 'two' }
  foo = { one: 'two' }
  ```

* If-clauses:
  ``` ruby
  if predicate?
    puts 'Hello, World!'
  end

  if true and (predicate?)
    puts 'Hello, World!'
  end

  if false or (predicate?)
    puts 'Hello, World!'
  end
  ```

## RSpec

[RSpec.sublime-settings](https://github.com/robbl/Switch/blob/master/RSpec.sublime-settings)

* should/should_not:
  ``` rspec
  1.should eq 1
  1.should_not eq 1
  ```

## Python

[Python.sublime-settings](https://github.com/robbl/Switch/blob/master/Python.sublime-settings)

* Boolean constants:
  ``` python
  flag = True
  flag = False
  ```

# Issues

Any issues and suggestions are very welcome on the
[github bugtracker](https://github.com/robbl/Switch/issues).
