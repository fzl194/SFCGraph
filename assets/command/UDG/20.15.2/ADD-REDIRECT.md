---
id: UDG@20.15.2@MMLCommand@ADD REDIRECT
type: MMLCommand
name: ADD REDIRECT（增加重定向）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: REDIRECT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- URL重定向控制
- 重定向
status: active
---

# ADD REDIRECT（增加重定向）

## 功能

**适用NF：PGW-U、UPF**

此命令用于运营商配置新的URL重定向策略。当运营商需要对HTTP/WAP（包括WAP1.X和WAP2.0版本）等协议的业务流做重定向处理则应用该命令。可以选择在URL重定向的报文中是否包含重定向携带信息名称。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 对于URL，特殊字符的输入要求：
    - 对于普通字符?必须使用%3f代替；例如：www.huawei.com/a?c 输入应该是：www.huawei.com/a%3fc。
    - 对于空格必须使用%20代替；例如：www.hua wei.com 输入应该是：www.hua%20wei.com。
    - 对于逗号必须使用％2c代替；例如：www.hua,wei.com 输入应该是：www.hua%2cwei.com。
    - 对于加号尽量使用％2b代替，可以直接输入连续一到两个的加号，但在查询时都会以%2b显示，在业务处理时会转义成加号，例如：www.hua+++wei.com 输入应该是：www.hua%2b%2b%2bwei.com。
    - 当字符串中出现%3f、%2c、%20、%2b或者%25本身时，对于%必须使用%25代替；例如：www.hua%3fwei.com 输入应该是：www.hua%253fwei.com。
    - 其他情况下，%就认为是%本身，可以保持原有实现即可，也可以使用%25替代%；例如：www.hua%wei.com 输入应该是：www.hua%wei.com或者是www.hua%25wei.com。
    - 对于分号使用\;代替；例如：www.hua;wei.com 输入应该是：www.hua\;wei.com。
    - 对于双引号使用\"代替；例如：www.hua"wei.com 输入应该是：www.hua\"wei.com。
    - 对于反斜杠使用\\代替；例如：www.hua\wei.com 输入应该是：www.hua\\wei.com。
    - 输入“\”只支持上述三种转义字符，不支持其他情况下输入“\”，如果要使用“\”本身，请输入“\\”代替。
    - 不能包含ASCII码值为0x00~0x1F和0x7F的非法字符。
    - URL不允许以“/”开头，可以支持配置“http://”或者“https://”scheme信息，如果没有配置scheme信息，重定向url的scheme默认为“http://”。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REDIRECTNAME | 重定向名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置重定向配置名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| URL | URL | 可选必选说明：必选参数<br>参数含义：该参数用于设定重定向URL。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～119。<br>默认值：无<br>配置原则：无 |
| FLOWCONTROL | 流控标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置重定向的流控开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：<br>- 如果重定向不开启流控功能，则设置该参数为DISABLE。<br>- 如果重定向要开启流控功能，则设置该参数为ENABLE。 |
| ACTIONINTERVAL | 流控时间间隔（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“FLOWCONTROL”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置重定向流控处理的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～3600，单位是秒。<br>默认值：5<br>配置原则：由于重定向成功率会下降，请现网根据重定向频次配置此参数。 |
| DEFAULTACT | 重定向缺省动作 | 可选必选说明：可选参数<br>参数含义：该参数用于设置不满足重定向条件时报文的缺省动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BLOCK：阻塞。<br>- PASS：通过。<br>默认值：BLOCK<br>配置原则：<br>- 当运营商在做重定向业务时，对于不满足条件的业务需要放通，配置PASS。<br>- 当运营商在做重定向业务时，对于不满足条件的业务需要阻塞，配置BLOCK。 |
| APPENDINFONAME | 重定向携带信息名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定重定向携带信息名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD REDIRAPPENDINFO命令配置生成。<br>- 设置的AppendInfoName必须是系统已经存在的名称。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/REDIRECT]] · 重定向（REDIRECT）

## 使用实例

运营商规划定义一个名为“testredirect2”的URL重定向策略，重定向URL为“www.huawei.com”，需要携带重定向携带信息名称为test：

```
ADD REDIRECT: REDIRECTNAME="testredirect2", URL="www.huawei.com", FLOWCONTROL=DISABLE, APPENDINFONAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加重定向（ADD-REDIRECT）_82837528.md`
