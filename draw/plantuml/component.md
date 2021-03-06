# 组件图 #

## 组件 ##

组件需要使用中括号包含, 也可以使用 component 关键字来定义组件, 使用 as 关键字定义别名.

将以下内容保存为 [component01](./component/component01.pum):

```
@startuml

[First component]
[Another component] as Comp2
component Comp3
component [Last\ncomponent] as Comp4

@enduml
```

生成的效果图如下:

![component01.png](./component/component01.png)

## interface ##

interface 的定义需要使用小括号包含, 也可以使用 interface 关键字定义, 使用 as 关键字定义别名.

将以下内容保存为 [component02](./component/component02.pum):

```
@startuml

() "First Interface"
() "Another interface" as Interf2

interface Interf3
interface "Last\ninterface" as Interf4

@enduml
```

生成的效果图如下:

![component02.png](./component/component02.png)

## 简单例子 ##

对于各个元素之间的关系, 可以使用 .. 符号表示虚线, -- 符号表示实线, > 符号表示箭头.

将以下内容保存为 [component03](./component/component03.pum):

```
@startuml

DataAccess - [First Component]
[First Component] ..> HTTP : use

@enduml
```

生成的效果图如下:

![component03.png](./component/component03.png)

## 注解 ##

可以使用 note left, note right, note top 或者 note bottom 等关键字来定义注解. 注解也可以使用 note 关键字定义, 然后使用 .. 符号连接到具体的节点.

将以下内容保存为 [component04](./component/component04.pum):

```
@startuml

interface "Data Access" as DA

DA - [First Component]
[First Component] ..> HTTP : use

note left of HTTP : Web Service only

note right of [First Component]
A note can also
be on several lines
end note

@enduml
```

生成的效果图如下:

![component04.png](./component/component04.png)

## 分组 ##

可以使用  package, folder, frame, cloud, database 等关键字来定义分组.

将以下内容保存为 [component05](./component/component05.pum):

```
@startuml

package "Some Group" {
HTTP - [First Component]
[Another Component]
}

node "Other Groups" {
FTP - [Second Component]
[First Component] --> FTP
}

cloud {
[Example 1]
}

database "MySql" {
folder "This is my folder" {
[Folder 3]
}
frame "Foo" {
[Frame 4]
}
}

[Another Component] --> [Example 1]
[Example 1] --> [Folder 3]
[Folder 3] --> [Frame 4]

@enduml
```

生成的效果图如下:

![component05.png](./component/component05.png)

## 修改箭头方向 ##

默认的, 使用 -- 的箭头方向是水平的, 可以使用单个 - 符号或者 . 符号来修改为垂直方向. 也可以使用 left, right, up 和 down 等关键字来定义方向, 可以只使用关键字的一个或二个字母.

将以下内容保存为 [component06](./component/component06.pum):
```
@startuml

[Component1] --> Interface1
[Component1] -> Interface2

Interface3 <-- [Component2]
Interface4 <- [Component2]

[Component4] -left-> left
[Component4] -right-> right
[Component4] -up-> up
[Component4] -down-> down

@enduml
```

生成的效果图如下:

![component06.png](./component/component06.png)

## UML2 notation ##

可以使用 skinparam componentStype uml2 命令来切换到 UML2 notation.

将以下内容保存为 [component07](./component/component07.pum):
```
@startuml

skinparam componentStyle uml2

interface "Data Access" as DA

DA - [First Component]
[First Component] ..> HTTP : use

@enduml
```

生成的效果图如下:

![component07.png](./component/component07.png)

## 长描述文本和颜色 ##

将以下内容保存为 [component08](./component/component08.pum):
```
@startuml

component comp1 [
This component
has a long comment
on several lines
]

component [Web Server] #Yellow

@enduml
```

生成的效果图如下:

![component08.png](./component/component08.png)

## sprite ##

将以下内容保存为 [component09](./component/component09.pum):
```
@startuml

sprite $businessProcess [16x16/16] {
FFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFF
FFFFFFFFFF0FFFFF
FFFFFFFFFF00FFFF
FF00000000000FFF
FF000000000000FF
FF00000000000FFF
FFFFFFFFFF00FFFF
FFFFFFFFFF0FFFFF
FFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFF
}

rectangle " End to End\nbusiness process" <<$businessProcess>> {
rectangle "inner process 1" <<$businessProcess>> as src
rectangle "inner process 2" <<$businessProcess>> as tgt
src -> tgt
}

@enduml
```

生成的效果图如下:

![component09.png](./component/component09.png)

## skinparam ##

可以使用 skinparam 命令来修改颜色和字体, 使用方式包括以下几种:

- 在图形的定义中
- 在一个包含文件中
- 在一个配置文件中

将以下内容保存为 [component10](./component/component10.pum):
```
@startuml

skinparam interface {
backgroundColor RosyBrown
borderColor orange
}

skinparam component {
FontSize 13
BackgroundColor<<Apache>> Red
BorderColor<<Apache>> #FF6655
FontName Courier
BorderColor black
BackgroundColor gold
ArrowFontName Impact
ArrowColor #FF6655
ArrowFontColor #777777
}

() "Data Access" as DA

DA - [First Component]
[First Component] ..> () HTTP : use
HTTP - [Web Server] << Apache >>

[AA] <<static lib>>
[BB] <<shared lib>>
[CC] <<static lib>>

node node1
node node2 <<shared node>>
database Production

skinparam component {
backgroundColor<<static lib>> DarkKhaki
backgroundColor<<shared lib>> Green
}

skinparam node {
borderColor Green
backgroundColor Yellow
backgroundColor<<shared node>> Magenta
}

skinparam databaseBackgroundColor Aqua

@enduml
```

生成的效果图如下:

![component10.png](./component/component10.png)
